# Generated by Django 4.0.4 on 2022-05-23 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_match_id_user_alter_usermatch_id_user'),
        ('statistic', '0002_alter_rating_id_user_alter_userscore_id_user'),
        ('users', '0004_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]