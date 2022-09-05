from django.db import models


# Create your models here.


class Book(models.Model):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='books/%Y-%m-%d/')
    url_img = models.TextField(max_length=50)
    price = models.IntegerField()
    realise_date = models.DateTimeField()
    descriptions = models.TextField(max_length=350)
    full_descriptions = models.TextField()
    amount = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        db_table = 'Book'
        ordering = ['name']

    def __str__(self):
        return self.name        # Метод __str__() возвращает отображение объекта, понятное человеку.

