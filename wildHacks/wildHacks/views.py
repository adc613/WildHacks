<<<<<<< HEAD
from django.http import HttpResponse
from django.template.loader import get_template


def homepage(request):
	return 
	"""
	displays homepage
	"""

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
=======
from django.views.generic.base import TemplateView

class HomePageView (TemplateView):
	template_name = 'wild_hacks/homepage.html'
>>>>>>> 68b07be05c7a5c9d75667dd3e6956d24a518a298
