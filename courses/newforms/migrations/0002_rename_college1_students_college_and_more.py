# Generated by Django 5.0.6 on 2024-06-19 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newforms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='college1',
            new_name='College',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='phone1',
            new_name='Contact_Number',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='course1',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='name1',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='usn1',
            new_name='USN',
        ),
    ]
