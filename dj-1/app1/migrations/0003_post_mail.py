# Generated by Django 5.1.7 on 2025-04-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_post_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
