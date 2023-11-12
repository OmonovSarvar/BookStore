import json
import datetime

from django.contrib.auth.models import User
from selenium import webdriver
from django.test import TestCase
from book_api.models import BookStoreModel

d = '2018-01-10T08:14:00'

# User = {
#     "username": "victus",
#     "password": "qwErt1928"
# }


# Test for Model

class BookStoreTest(TestCase):
    def setUp(self) -> None:
        BookStoreModel.objects.create(user=User.objects.create_user(username='qodirbek', password='qwErt1928'), title='Wick', category='Romance', is_available=True, published=d,
                                      ISO=123123123)
        BookStoreModel.objects.create(user=User.objects.create_user(username='qodirbek', password='qwErt1928'), title='Bro', category='Fantasy', is_available=False, published=d,
                                      ISO=129823123)
        BookStoreModel.objects.create(user=User.objects.create_user(username='qodirbek', password='qwErt1928'), title='Hello', category='Comics', is_available=True, published=d,
                                      ISO=123343123)
        BookStoreModel.objects.create(user=User.objects.create_user(username='qodirbek', password='qwErt1928'), title='Luck', category='Adventure', is_available=False,
                                      published=d, ISO=123124523)
        BookStoreModel.objects.create(user=User.objects.create_user(username='qodirbek', password='qwErt1928'), title='Lucky Man', category='Fiction', is_available=True,
                                      published=d, ISO=123125123)

    def test_models(self):
        var1 = BookStoreModel.objects.get(title='Wick').title
        var2 = BookStoreModel.objects.get(category='Romance').category
        var3 = BookStoreModel.objects.get(is_available=True).is_available
        var4 = BookStoreModel.objects.get(ISO=123123123).ISO

        var5 = BookStoreModel.objects.get(title='Bro').title
        var6 = BookStoreModel.objects.get(category='Fantasy').category
        var7 = BookStoreModel.objects.get(is_available=False).is_available
        var8 = BookStoreModel.objects.get(ISO=129823123).ISO

        var9 = BookStoreModel.objects.get(title='Hello').title
        var10 = BookStoreModel.objects.get(category='Comics').category
        var11 = BookStoreModel.objects.get(is_available=True).is_available
        var12 = BookStoreModel.objects.get(ISO=123343123).ISO

        var13 = BookStoreModel.objects.get(title='Luck').title
        var14 = BookStoreModel.objects.get(category='Adventure').category
        var15 = BookStoreModel.objects.get(is_available=False).is_available
        var16 = BookStoreModel.objects.get(ISO=123124523).ISO

        var17 = BookStoreModel.objects.get(title='Lucky Man').title
        var18 = BookStoreModel.objects.get(category='Fiction').category
        var19 = BookStoreModel.objects.get(is_available=True).is_available
        var20 = BookStoreModel.objects.get(ISO=123125123).ISO

        self.assertEqual(var1, 'Wick')
        self.assertEqual(var2, 'Romance')
        self.assertEqual(var3, True)
        self.assertEqual(var4, 123123123)

        self.assertEqual(var5, 'Bro')
        self.assertEqual(var6, 'Fantasy')
        self.assertEqual(var7, False)
        self.assertEqual(var8, 129823123)

        self.assertEqual(var9, 'Hello')
        self.assertEqual(var10, 'Comics')
        self.assertEqual(var11, True)
        self.assertEqual(var12, 123343123)

        self.assertEqual(var13, 'Luck')
        self.assertEqual(var14, 'Adventure')
        self.assertEqual(var15, False)
        self.assertEqual(var16, 123124523)

        self.assertEqual(var17, 'Lucky Man')
        self.assertEqual(var18, 'Fiction')
        self.assertEqual(var19, True)
        self.assertEqual(var20, 123125123)
