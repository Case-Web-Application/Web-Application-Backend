# Generated by Django 4.2.1 on 2023-06-08 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testov', '0003_alter_answers_right_alter_interpretations_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='scale',
        ),
    ]
