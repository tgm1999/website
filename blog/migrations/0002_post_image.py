# Generated by Django 2.2.14 on 2020-08-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='img/'),
            preserve_default=False,
        ),
    ]
