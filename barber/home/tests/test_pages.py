import wagtail_factories

from wagtail.tests.utils import WagtailPageTests

from ..factories import HomeFactory


class HomePageTest(WagtailPageTests):

	def test_it_have_a_title(self):
		page = HomeFactory(
			title='BarberCachets',
			parent=wagtail_factories.PageFactory(parent=None)
		)

		self.assertIsNotNone(page.title)
		self.assertEqual('BarberCachets', page.title)
