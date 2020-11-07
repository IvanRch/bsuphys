# Generated by Django 3.0.8 on 2020-11-07 15:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200719_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteInMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('body', ckeditor.fields.RichTextField()),
                ('status', models.TextField(blank=True, choices=[('draft', 'Черновик'), ('published', 'Опубликовать')], help_text='Обязательное поле!', max_length=10, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Новые заметки в СМИ',
                'ordering': ('-publish',),
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
