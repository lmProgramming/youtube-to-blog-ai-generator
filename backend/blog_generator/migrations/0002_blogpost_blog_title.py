# Generated by Django 5.1.1 on 2024-10-06 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_title',
            field=models.CharField(default='blog title', max_length=300),
            preserve_default=False,
        ),
    ]
