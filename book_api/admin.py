from django.contrib import admin
from book_api.models import BookStoreModel, SubscribersModel

# Register your models here.
admin.site.register(BookStoreModel)
admin.site.register(SubscribersModel)
