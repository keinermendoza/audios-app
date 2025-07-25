# Generated by Django 5.2 on 2025-06-09 15:19

import custom_auth.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('apellido', models.CharField(blank=True, max_length=80)),
                ('nombre', models.CharField(blank=True, max_length=80)),
                ('telefono', models.CharField(blank=True, max_length=80)),
                ('_profile_image', models.ImageField(blank=True, max_length=300, upload_to=custom_auth.models.get_profile_image_path)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('ultimo_login', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=80, unique=True)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
