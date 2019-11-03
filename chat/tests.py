from django.test import TestCase, Client
from django.contrib.auth.models import User
from chat.models import UserProfile, Message
from chat.serializers import MessageSerializer, UserSerializer
from django.http.response import JsonResponse
from django.test.utils import setup_test_environment

# Create your tests here.


class UsersTestCase(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username='user01', password='password')
        UserProfile.objects.create(user=user)
        user = User.objects.create_user(username='user02', password='password')
        UserProfile.objects.create(user=user)
        self.client = Client()

    def test_user_list(self):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        usersjson = JsonResponse(users.data, safe=False)
        response = self.client.get('/api/users')
        self.assertTrue(response.status_code == 200)
        self.assertEqual(usersjson.content, response.content)

