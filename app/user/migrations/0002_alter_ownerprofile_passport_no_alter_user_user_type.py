# Generated by Django 5.0.1 on 2024-01-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerprofile',
            name='passport_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('OWNER', 'OWNER'), ('EMPLOYEE', 'EMPLOYEE'), ('CUSTOMER', 'CUSTOMER')], max_length=100),
        ),
    ]
