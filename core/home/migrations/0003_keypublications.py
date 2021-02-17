# Generated by Django 3.0.8 on 2021-02-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200731_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyPublications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
                ('journal', models.TextField(blank=True, null=True)),
                ('publicationUrl', models.URLField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/keypublications')),
            ],
            options={
                'verbose_name_plural': 'Основные публикации',
            },
        ),
    ]