# Generated by Django 4.1 on 2022-09-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='media/books/%Y-%m-%d/'),
        ),
    ]
