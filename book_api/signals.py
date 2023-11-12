from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, post_delete
from django.contrib.auth.models import User

from book_app.settings import EMAIL_HOST_USER
from .models import SubscribersModel
from .views import Email


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        SubscribersModel.objects.create(user=instance)
        to_mail = [Email]
        send_mail('Welcome New Subscriber',
                  'Assalomu alaykum xurmatli mijoz, siz bizni blog postlarimizga obuna bo’ldingiz va tez orada biz sizga eng yaxshi postlarimizni yuboramiz',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_mail,
                  fail_silently=False
                  )
        print(f'Message sent to {Email}')
        instance.save()


@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    instance.profile.delete()
    print("Profile deleted")
