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

    def test_api_can_get_a_message(self):
        """Test if api can get a given message."""
        message = Message.objects.get()
        response = self.client.get('/wall-api/messages/{}/'.format(message.id), format="json")
        serializer = MessageSerializer(message)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_api_can_update_message(self):
        """Test if api can update a given message."""
        message = Message.objects.get()
        change_message = {'content': 'Test updating an article in this message'}
        response = self.client.put('/wall-api/messages/{}/update/'.format(message.id), change_message, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_message(self):
        """Test the api can delete a message."""
        message = Message.objects.get()
        response = self.client.delete('/wall-api/messages/{}/delete/'.format(message.id), format="json", follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class GetAllMessagesTest(TestCase):
    """ Test module for GET all the wall API """

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
        print(response.data)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class UnauthedCreateViewTestCase(TestCase):
    """Test suite user cannot create if not logged in."""
    def setUp(self):
        user = User.objects.create(username='apitestuser')
        self.client = APIClient()
        self.message_data = {'content': 'Non-legit message from tests', 'user': user.id}
        self.response = self.client.post('/wall-api/messages/create/', self.message_data, format='json')   

    def test_api_cannot_create_a_message(self):
        """Test if unauthed will not allow new message creation."""
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)



class UnauthenticatedUpdateDeleteViewTestCase(TestCase):
    """Test suite user cannot update/delete if not logged in/authenticated."""
    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username='apitestuser')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.message_data = {'content': 'New message from tests', 'user': user.id}
        self.response = self.client.post('/wall-api/messages/create/', self.message_data, format='json')

    def test_api_cannot_update_message(self):
        """Test if api cannot update a given message."""
        self.client.force_authenticate(user=None)
        message = Message.objects.get()
        change_message = {'content': 'Test updating an article in this message'}
        response = self.client.put('/wall-api/messages/{}/update/'.format(message.id), change_message, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_cannot_delete_message(self):
        """Test the api cannot delete a message."""
        self.client.force_authenticate(user=None)
        message = Message.objects.get()
        response = self.client.delete('/wall-api/messages/{}/delete/'.format(message.id), format="json", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UnauthorizedUpdateDeleteViewTestCase(TestCase):
    """Test suite logged in user cannot update/delete if not authorized/not their message"""
    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username='apitestuser')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.message_data = {'content': 'New message from tests', 'user': user.id}
        self.response = self.client.post('/wall-api/messages/create/', self.message_data, format='json')
        self.client.force_authenticate(user=None)
        wronguser = User.objects.create(username='wrongapitestuser')
        self.client.force_authenticate(user=wronguser)

    def test_api_cannot_update_message(self):
        """Test if api cannot update a given message."""
        message = Message.objects.get()
        change_message = {'content': 'Test updating an article in this message'}
        response = self.client.put('/wall-api/messages/{}/update/'.format(message.id), change_message, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_cannot_delete_message(self):
        """Test the api cannot delete a message."""
        self.client.force_authenticate(user=None)
        message = Message.objects.get()
        response = self.client.delete('/wall-api/messages/{}/delete/'.format(message.id), format="json", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)