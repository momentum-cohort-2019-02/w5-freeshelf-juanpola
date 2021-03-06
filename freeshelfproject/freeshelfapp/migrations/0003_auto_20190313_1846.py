# Generated by Django 2.1.7 on 2019-03-13 18:46

from django.db import migrations, models
import django.db.models.deletion
import slugger.fields


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelfapp', '0002_auto_20190312_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('programming_language', models.CharField(blank=True, max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='freeshelfapp.Author')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='slugger',
            field=slugger.fields.AutoSlugField(blank=True, null=True, populate_from='title', unique=True),
        ),
    ]
