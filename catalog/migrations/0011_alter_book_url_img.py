# Generated by Django 4.1 on 2022-09-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_book_url_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='url_img',
            field=models.TextField(max_length=50),
        ),
    ]
