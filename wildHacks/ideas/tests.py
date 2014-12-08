from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .models import *
from users.models import *

class test_views(TestCase):
    def set_up(self):
        user = User.objects.create_user(
                email="adc82@case.edu",
                first_name="Ron",
                last_name="Burgundy",
                password="baxter"
                )

        Idea.objects.create(
                title="Hey guys",
                short_discription="What up",
                long_discription="what is up?",
                creator = user
                )

        user2 = User.objects.create_user(
                email="adc82@cim.edu",
                first_name="Will",
                last_name="Ferrell",
                password="baxter"
                )

        Idea.objects.create(
                title="Hello people",
                short_discription="How are you",
                long_discription="what is up?",
                creator = user2
                )

    def test_vote(self):
        self.set_up() 
        idea = Idea.objects.get(title="Hello people")
        c = Client()
        c.login(email="adc82@case.edu", password="baxter")
        r = c.post(reverse("ideas:up_vote", kwargs={'pk':idea.pk}))
        self.assertEqual(r.status_code, 302)
        idea = Idea.objects.get(pk=idea.pk)
        self.assertEqual(idea.votes, 1)
        r = c.post(reverse("ideas:down_vote", kwargs={'pk':idea.pk}))
        self.assertEqual(r.status_code, 302)
        idea = Idea.objects.get(pk=idea.pk)
        self.assertEqual(idea.votes, 0)

    def test_detail_view(self):
        self.set_up()
        c = Client()
        resp = c.get(reverse('ideas:detail', kwargs={'pk':1}))
        self.assertTemplateUsed(c, "ideas/detail.html")
        self.assertEqual(resp.status_code, 200)
        resp = c.get(reverse('ideas:detail', kwargs={'pk':99}))
        self.assertEqual(resp.status_code, 404)

    def test_idea_list_view(self):
        self.set_up()
        c = Client()
        resp = c.get(reverse('ideas:list'))
        self.assertTemplateUsed(resp, "ideas/list.html")
