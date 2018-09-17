# Create your tests here.
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from . import models


# Make an authenticated request to the view...


# Create your tests here.
class AccountTests(APITestCase):

    def test_account_post_(self):
        url = reverse('register-user')
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data, format='json')
        thi = models.User.objects.get(pk=1)
        print(thi)
        tk = Token.objects.create(user=thi)
        print(tk.key)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(models.User.objects.count(), 1)


class ViewTests(APITestCase):

    def setUp(self):
        for i in range(1, 6):
            models.Dog.objects.create(name='test{}'.format(i),
                                      image_filename='test.jpg',
                                      size='l',
                                      age=20,
                                      gender='f')
        url = reverse('register-user')
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data, format='json')
        thi = models.User.objects.get(pk=1)
        tk = Token.objects.create(user=thi)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(models.User.objects.count(), 1)

        self.client2 = APIClient()
        self.client2.credentials(HTTP_AUTHORIZATION='Token ' + tk.key)

    def test_dog_view_get(self):
        resp = self.client2.get('/api/dog/-1/undecided/next/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('test1', str(resp.data))
        print(resp.data)

    def test_liked_dog_view_get(self):
        first_resp = self.client2.put('/api/dog/2/liked/')
        self.assertEqual(first_resp.status_code, 200)
        resp = self.client2.get('/api/dog/1/liked/next/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('test2', str(resp.data))
        print(resp.data)

    def test_disliked_dog_view_get(self):
        first_resp = self.client2.put('/api/dog/3/disliked/')
        self.assertEqual(first_resp.status_code, 200)
        resp = self.client2.get('/api/dog/1/disliked/next/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('test3', str(resp.data))
        print(resp.data)

    def test_user_preference(self):
        url = reverse('user_preferences')
        data = {'age': 'b,y,a,s', 'gender': 'm,f', 'size': 'xl,s,m,l'}
        resp = self.client2.put(url, data, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('y', models.UserPref.objects.get(pk=1).age)
        print(resp)
