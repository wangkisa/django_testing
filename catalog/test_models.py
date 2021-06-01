from django.test import TestCase

from catalog.models import Author


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')
        # pass

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        print('author:', author)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')
        # self.assertEquals('first name', 'first name')
        # self.assertEquals('2', '2')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_object_1_is_correct_name(self):
        author = Author.objects.get(id=1)
        self.assertEquals('mozila', author.first_name)

    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEquals(author.get_absolute_url(), '/catalog/author/1')
