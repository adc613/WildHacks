from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import *
from .forms import *
class IdeaDetailView(DetailView):
    """
    Detailed view of an individual idea
    """
    model = Idea
    template_name = "ideas/detail.html"

class IdeaListView(ListView):
    """
    List view of all the ideas
    """
    model = Idea
    template_name = "ideas/list.html"

class IdeaCreationView(View):
    """
    A view to allow you to create an idea
    """
    template_name = 'ideas/create.html'
    model = Idea
    form = IdeaCreationForm

    def get(self, request):
      return render(request, self.template_name, {'form' : self.form})

    def post(self, request, *args, **kwargs):
      form = self.form(request.POST or None)

      if form.is_valid():
        save_it = form.save(commit=True)
        save_it.save()
        messages.success(request,
                   """
                   This could lead to the creation of the next google. Every 
                   redwood tree starts out as a seed planted somewhere.
                   """
                   )
        return HttpResponseRedirect(reverse('thanks'))
      else:
        messages.error(request,
                    """
                    There semes to have been a problem with your form. Plese try
                    resubmitting.
                    """
                    )
        return HttpReponseRedirect(reverse('thanks'))

