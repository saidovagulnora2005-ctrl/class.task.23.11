from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    

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
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Share(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Ожидание'),
        ('ACCEPTED', 'Принят'),
        ('REJECTED', 'Отклонён'),
        ('CANCELLED', 'Отменён')
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} , {self.book.title}'



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    message = models.TextField(blank=True)



