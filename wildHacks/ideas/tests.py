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

    def test_ideas_creation_view(self):
        self.set_up()
        c = Client()
        resp = c.get(reverse('ideas:create'))
        self.assertEqual(resp.status_code, 302)

        resp = c.get(reverse('ideas:create'), follow=True)
        self.assertEqual(resp.status_code, 200)

        c.login(email="adc82@case.edu", password="baxter")
        resp = c.get(reverse('ideas:create'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "ideas/create.html")
        
        c.logout()
        resp = c.post(reverse('ideas:create'),
                {'long_discription': "mmmmm lady",
                'short_discription': "my lady",
                'title': "GoT" }
                )
        self.assertEqual(resp.status_code, 302)
        #checks to make sure the object does not exist after the post request
        #Kind of a hack but it works
        try:
            Idea.objects.get(title="GoT")
        except Idea.DoesNotExist:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)

        c.login(email="adc82@case.edu", password="baxter")
        resp = c.post(reverse('ideas:create'),
                {'long_discription': "mmmmm lady",
                'short_discription': "my lady",
                'title': "GoT" }
                )
        self.assertEqual(resp.status_code, 302)
        #Checks to make sure that the object exist after the post request
        try:
            idea = Idea.objects.get(title="GoT")           
        except Idea.DoesNotExist:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)
        self.assertEqual(idea.creator.email, "adc82@case.edu") 

    def test_search_view(self):
        self.set_up()
        c = Client()
        
        resp = c.get(reverse('ideas:search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(c, 'ideas/search.html')

        resp = c.post(reverse('ideas:search'), {'search':'hey'})
        results = resp.context['search_results']
        correct = Idea.objects.filter(title__contains='hey')
        """
        bad code but it'll work for now maybe I'll come back and change it later
        couldn't get self.assertQuersetEqual to work for some reason so I did
        this to replace it.
        """
        i = 0
        for res in results:
            self.assertEqual(res, correct[i])
            i += 1
        i = 0
        for res in correct:
            self.assertEqual(res, results[i])
            i += 1
        
