from django.db import models
from django.contrib.auth.models import CustomUser, AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='authors')

    def __str__(self):
        return self.name
    
    #tuple that includes permissions
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book,related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
#UserProfile model with a role  
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

#Django Signal to Automatically Create Profiles
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Custom User model

# login with email and password
# create Usermanager taht creates USERS and SUPERUSERS

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email,date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.create_user(username, email, password, date_of_birth, **extra_fields)
        user.save(User=self._db)

        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email