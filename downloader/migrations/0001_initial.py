# Generated by Django 4.0.3 on 2022-03-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('download_link', models.URLField()),
                ('subtitle_link', models.URLField()),
            ],
        ),
    ]
