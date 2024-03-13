# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Post, Project, Notification


# class NotificationTestCase(TestCase):
#     def test_create_post_notification(self):
#         user = User.objects.create(username='testuser', password='password')
#         post = Post.objects.create(
#             user=user, content='This is a test post.')  # Use 'user' instead of 'creator'
#         notifications = Notification.objects.filter(recipient=user)
#         self.assertEqual(notifications.count(), 1)
#         self.assertEqual(
#             notifications[0].message, f'New post "{post.content}" has been created.')

#     def test_create_project_notification(self):
#         user = User.objects.create(username='testuser', password='password')
#         project = Project.objects.create(
#             name='Test Project', description='This is a test project.', creator=user)
#         notifications = Notification.objects.filter(recipient=user)
#         self.assertEqual(notifications.count(), 1)
#         self.assertEqual(
#             notifications[0].message, f'A new project has been added "{project.name}".')
#         print(notifications[0].message, f'A new project has been added "{project.name}".')
