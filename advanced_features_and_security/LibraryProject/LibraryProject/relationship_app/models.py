from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from bookshelf.models import CustomUser





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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile')
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
    try:
        instance.profile.save()  # Accessing via the related_name
    except UserProfile.DoesNotExist:
        # If the profile does not exist, create it
        UserProfile.objects.create(user=instance)


