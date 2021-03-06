# Generated by Django 4.0.2 on 2022-02-28 04:37

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.BooleanField(default=False)),
                ('good_at', models.CharField(max_length=300)),
                ('style', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('myUser', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
