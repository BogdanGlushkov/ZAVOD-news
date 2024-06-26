# Generated by Django 5.0.6 on 2024-05-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_news_options_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Картинка'),
        ),
    ]
