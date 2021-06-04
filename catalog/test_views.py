import json

from django.test import TestCase
from django.urls import reverse

from catalog.models import Author


class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_authors = 13

        for author_id in range(number_of_authors):
            Author.objects.create(
                first_name=f'Christian {author_id}',
                last_name=f'Surname {author_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/catalog_list/')
        # print(response)
        json_content = json.loads(response.content)
        # print('content:', response.content)
        # print('content:', json_content)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(13, len(json_content))

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('catalog_list'))
        self.assertEqual(response.status_code, 200)
