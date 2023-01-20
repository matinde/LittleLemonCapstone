from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializer import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(name='pizza', price=20)
        self.menu2 = Menu.objects.create(name='burger', price=10)
        self.menu3 = Menu.objects.create(name='pasta', price=15)

    def test_getall(self):
        response = self.client.get('/menus/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

