# Generated by Django 5.0.1 on 2024-01-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_initial'),
        ('user', '0002_alter_ownerprofile_passport_no_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='managers',
            field=models.ManyToManyField(blank=True, related_name='restaurant_managers', to='user.employeeprofile'),
        ),
    ]
