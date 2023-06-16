<<<<<<< HEAD
# Generated by Django 4.2.1 on 2023-06-15 15:25
=======
# Generated by Django 4.2.1 on 2023-06-16 08:05
>>>>>>> 5795b49bfe4b75e35d461ec5f74949583922c01a

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('right', models.BooleanField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
=======
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
>>>>>>> 5795b49bfe4b75e35d461ec5f74949583922c01a
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
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token1', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testov.user')),
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
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.tast')),
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
                ('answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.answers')),
<<<<<<< HEAD
=======
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.images')),
>>>>>>> 5795b49bfe4b75e35d461ec5f74949583922c01a
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
                ('obligatory', models.BooleanField()),
                ('mixq', models.BooleanField()),
                ('status', models.CharField(max_length=255)),
<<<<<<< HEAD
=======
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.images')),
>>>>>>> 5795b49bfe4b75e35d461ec5f74949583922c01a
                ('subtest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.subtest')),
            ],
        ),
        migrations.CreateModel(
            name='Interpretations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('queue', models.IntegerField()),
                ('text', models.CharField(max_length=255)),
<<<<<<< HEAD
                ('image', models.ImageField(null=True, upload_to='img/')),
                ('count_s', models.IntegerField()),
                ('count_f', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
=======
                ('count_s', models.IntegerField()),
                ('count_f', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.images')),
>>>>>>> 5795b49bfe4b75e35d461ec5f74949583922c01a
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.scales')),
            ],
        ),
        migrations.CreateModel(
            name='Attemption',
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
<<<<<<< HEAD
=======
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.images'),
        ),
        migrations.AddField(
            model_name='answers',
>>>>>>> 5795b49bfe4b75e35d461ec5f74949583922c01a
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testov.questions'),
        ),
    ]
