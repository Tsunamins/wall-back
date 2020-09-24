from django.test import TestCase
from .models import Message, User
from .serializers import MessageSerializer

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import force_authenticate


class ModelTestCase(TestCase):

    def setUp(self):
        self.newuser = User.objects.create(username='newuser')
        self.content = 'Message from the tests!!!'
        self.message = Message(
            content=self.content, user=self.newuser)

    def test_model_can_create_a_message(self):
        """Test if message model creates a message."""
        old_count = Message.objects.count()
        self.message.save()
        new_count = Message.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username='apitestuser')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.message_data = {'content': 'New message from tests', 'user': user.id}
        self.response = self.client.post('/wall-api/messages/create/', self.message_data, format='json')
      

    def test_api_can_create_a_message(self):
        """Test if api has message creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    

class GetAllMessagesTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        user = User.objects.create(username='apitestuser')
        Message.objects.create(
            content='Message for get all messages tests', user=user)
        Message.objects.create(
            content='Another message for the tests', user=user)
        Message.objects.create(
            content='Another creative test message', user=user)
     

    def test_get_all_messages(self):
        response = self.client.get('/wall-api/messages/', format="json")
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)