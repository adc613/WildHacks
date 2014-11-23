from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic.base import TemplateView


class HomePageView (TemplateView):
	template_name = 'wild_hacks/homepage.html'

def about_us(request):
	return 
	"""
	displays homepage
	"""

def thank_you(request):
	return 
	"""
	displays homepage
	"""

