from wagtail.tests.utils import WagtailPageTests


from ..models import HomePage


class HomePageTest(WagtailPageTests):

	def test_it_have_a_title(self):
		page = HomePage(title='BarberCachets')

		self.assertIsNotNone(page.title)
		self.assertEqual('BarberCachets', page.title)