# Generated by Django 5.1.3 on 2024-12-04 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add book'), ('can_change_book', 'Can edit book'), ('can_delete_book', 'Can delete book')]},
        ),
    ]