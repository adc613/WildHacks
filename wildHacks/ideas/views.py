from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import View

from .forms import *
from .models import *

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

    @method_decorator(login_required)
    def get(self, request):
      return render(request, self.template_name, {'form' : self.form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
      form = self.form(request.POST or None)

      if form.is_valid():
        save_it = form.save(commit=True)
        save_it.creator = request.user
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
        return HttpResponseRedirect(reverse('thanks'))

def like_view(request, **kwargs):
    idea = Idea.objects.get(pk = kwargs['pk'])
    idea.up_vote()
    return HttpResponseRedirect(reverse('ideas:list'))

def dislike_view(request, **kwargs):
  idea = Idea.objects.get(pk = kwargs['pk'])
  idea.votes -= 1
  idea.save()

  return HttpResponseRedirect(reverse('ideas:list'))

class SearchView(View):
    template_name = 'ideas/search.html'
    results_name = 'ideas/results.html'

    def get(self, request):
        c = {}
        #c.update(csrf(request))
        return render(request, self.template_name, c)

    def post(self, request, *args, **kwargs):
        if request.POST['search']:
            search = request.POST['search']
        else:
            search = ''

        search_results = Idea.objects.filter(title__contains=search)

        return render(request,
                self.results_name,
                {'search_results':search_results})
