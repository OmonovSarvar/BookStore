from django.contrib.auth.models import User
from django.db import models

user = str


class BookStoreModel(models.Model):
    categories = (
        ('Fiction', 'Fiction'),
        ('Romance', 'Romance'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Science fiction', 'Science fiction'),
        ('History', 'History'),
        ('Thriller', 'Thriller'),
        ('Comics', 'Comics'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    photo = models.ImageField(upload_to='photos')
    category = models.CharField(max_length=70, choices=categories)
    is_available = models.BooleanField()
    published = models.DateTimeField()
    ISO = models.CharField(max_length=50)

    class Meta:
        db_table = 'django'

    def __str__(self):
        return f'Added new book {self.title}'


class SubscribersModel(models.Model):
    email = models.EmailField(max_length=60)

    def __str__(self):
        return f'{self.email} new subscriber '
