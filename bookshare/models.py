from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    BOOK_STATUS = [
        ('NEW', 'новая'),
        ('OLD', 'старая'),
        ('GOOD', 'хорошая'),
        ('BAD', 'плохая')
    ]
    RATINGS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    poster = models.FileField(blank=True, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=BOOK_STATUS)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null = True)
    rating = models.SmallIntegerField(choices=RATINGS)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()


class Share(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField()

