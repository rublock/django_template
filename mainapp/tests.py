from django.test import TestCase

from mainapp.views import CatList


class CatListTest(TestCase):
    def test_context_data(self):
        view = CatList()
        context = view.get_queryset()
        self.assertEqual(len(context), 8)