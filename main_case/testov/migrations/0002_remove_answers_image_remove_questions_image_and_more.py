# Generated by Django 4.2.1 on 2023-06-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testov', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='image',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='image',
        ),
        migrations.RemoveField(
            model_name='scales',
            name='image',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='files/covers'),
        ),
    ]
