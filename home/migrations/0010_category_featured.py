# Generated by Django 4.2.2 on 2023-06-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
