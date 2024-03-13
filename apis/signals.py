# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Post, Project, Notification


# @receiver(post_save, sender=Post)
# def create_post_notification(sender, instance, created, **kwargs):
#     if created:
#         message = f'New post "{instance.content}" has been created.'
#         Notification.objects.create(recipient=instance.user, message=message)


# @receiver(post_save, sender=Project)
# def created_project_notification(sender, instance, created, **kwargs):
#     if created:
#         message = f'A new project has been added "{instance.name}".'
#         Notification.objects.create(
#             recipient=instance.creator, message=message)
