# Generated by Django 4.1 on 2022-09-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_book_full_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='media/books/%Y-%m-%d/'),
        ),
    ]
