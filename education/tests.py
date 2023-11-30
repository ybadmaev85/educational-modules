import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Module


class ModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.module = Module.objects.create(
            title='test'
        )

    def test_get_list(self):
        """
        Тестирование просмотра уроков
        """

        response = self.client.get(
            reverse('education:module-list')
        )

        print(response.json)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
