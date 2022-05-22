# Generated by Django 4.0.4 on 2022-05-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.IntegerField(default='', primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('user_name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
