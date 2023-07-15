# Generated by Django 4.2.2 on 2023-07-15 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_delete_breakings'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desktop_ad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destop_ad', to='home.advertisement'),
        ),
        migrations.AddField(
            model_name='category',
            name='mobile_ad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobile_ad', to='home.advertisement'),
        ),
    ]
