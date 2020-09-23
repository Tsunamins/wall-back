from django.test import TestCase
from .models import Message, User


class ModelTestCase(TestCase):

    def setUp(self):
        self.newuser = User.objects.create(username='newuser')
        self.content = 'Message from the tests!!!'
        self.message = Message(
            content=self.content, user=self.newuser)

    def test_model_can_create_a_message(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Message.objects.count()
        self.message.save()
        new_count = Message.objects.count()
        self.assertNotEqual(old_count, new_count)

