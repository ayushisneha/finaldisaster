# Generated by Django 2.1.2 on 2018-10-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0004_auto_20181026_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found',
            name='pic',
            field=models.ImageField(blank=True, default='media/profile_pics/def.jpg', upload_to='profile_pics'),
        ),
    ]
