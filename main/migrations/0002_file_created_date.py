# Generated by Django 3.1.6 on 2021-02-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default='2020-11-02'),
            preserve_default=False,
        ),
    ]
