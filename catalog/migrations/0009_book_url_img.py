# Generated by Django 4.1 on 2022-09-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url_img',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
