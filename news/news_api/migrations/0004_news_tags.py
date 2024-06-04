# Generated by Django 5.0.6 on 2024-06-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0003_remove_news_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(related_name='news', to='news_api.tag'),
        ),
    ]