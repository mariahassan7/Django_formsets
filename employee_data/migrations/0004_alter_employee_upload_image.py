# Generated by Django 4.2.4 on 2023-08-22 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data', '0003_alter_employee_upload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='upload_image',
            field=models.ImageField(upload_to='./uploads/images/'),
        ),
    ]
