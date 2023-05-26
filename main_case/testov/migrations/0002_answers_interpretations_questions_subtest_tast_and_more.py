# Generated by Django 4.2.1 on 2023-05-24 12:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testov', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('queue', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('count_of_scale', models.IntegerField()),
                ('right', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Interpretations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('queue', models.IntegerField()),
                ('text', models.CharField(max_length=255)),
                ('count_s', models.IntegerField()),
                ('count_f', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('queue', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('obligatory', models.IntegerField()),
                ('mixq', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.answers')),
            ],
        ),
        migrations.CreateModel(
            name='SubTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description_1', models.CharField(max_length=255)),
                ('description_2', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
                ('time_for_solve', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.questions')),
            ],
        ),
        migrations.CreateModel(
            name='Tast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description_1', models.CharField(max_length=255)),
                ('description_2', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
                ('time_for_solve', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('subtest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.subtest')),
            ],
        ),
        migrations.CreateModel(
            name='Scales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('queue', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('interpretation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.interpretations')),
            ],
        ),
        migrations.CreateModel(
            name='Atemption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('time_s', models.DateTimeField(auto_now=True)),
                ('answers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testov.answers')),
                ('interpretation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testov.interpretations')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testov.questions')),
                ('scale', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testov.scales')),
                ('tast', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testov.tast')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testov.user')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.scales'),
        ),
    ]