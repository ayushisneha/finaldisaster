# Generated by Django 2.1.2 on 2018-10-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0011_auto_20181026_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found',
            name='pic',
            field=models.ImageField(blank=True, default='def.jpg', upload_to=''),
        ),
    ]