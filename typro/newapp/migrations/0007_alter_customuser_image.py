# Generated by Django 5.0 on 2024-02-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_adddoctor_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
