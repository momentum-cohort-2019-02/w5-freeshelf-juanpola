# Generated by Django 2.1.7 on 2019-03-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelfapp', '0003_auto_20190313_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank='true', upload_to='book_image'),
        ),
    ]
