from django.test import TestCase

from mainapp.views import MainPageView


class MainPageViewTest(TestCase):
    def test_context_data(self):
        view = MainPageView()
        context = view.get_context_data()
        self.assertIn("cat_img", context)
        self.assertIn("title", context)
        self.assertEqual(context["title"], "cats")
