from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Blog

#triggered before saving a blog
@receiver(pre_save, sender=Blog)
def before_save(sender, instance, **kwargs):
    print(f"About to save[pre-save] : {instance.title}")

#triggered after saving a blog
@receiver(post_save, sender=Blog)
def after_save(sender, instance, created, **kwargs):
    if created:
        print(f"New blog created [post-save] : {instance.title}")
    else:
        print(f"Blog updated [post-save]: {instance.title}")