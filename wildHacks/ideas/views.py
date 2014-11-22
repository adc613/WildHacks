from django.shortcuts import render
from django.genric import View
from djanog.genric.list import ListView
from django.generic.detail import DetailView
from django.generic import UpdateView

class IdeaDetailView(DetailView):
    """
    Detailed view of an individual idea
    """
    model = Idea
    template = "idea_detail.html"

class IdeaListView(ListView):
    """
    List view of all the ideas
    """
    model = Idea
    template = "idea_list.html"
