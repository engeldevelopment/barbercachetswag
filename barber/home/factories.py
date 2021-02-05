import wagtail_factories

from .models import HomePage


class HomeFactory(wagtail_factories.PageFactory):
	class Meta:
		model = HomePage

	title = 'BarberCachet\'s'
