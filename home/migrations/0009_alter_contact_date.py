# Generated by Django 5.1.4 on 2025-07-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_travelphoto_user_delete_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
