# Generated by Django 5.1.7 on 2025-04-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title_des', models.CharField(max_length=255)),
                ('post_date', models.DateField()),
                ('post_text_1', models.CharField(max_length=255)),
                ('post_text_2', models.CharField(max_length=255)),
            ],
        ),
    ]
