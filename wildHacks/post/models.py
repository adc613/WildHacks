from django.db import models

class Idea (models.Model):
    """
    A class that represents a single start up idea
    """
    #A complete discrition of the start up idea
    long_discription = models.TextField(blank=False, max_length=1000)
    #The title of the idea 
    title = models.CharField(blank=False, max_length=100)
    #The short sort of "one sentence" discrition of the idea
    short_discription = modes.TextField(blank=False, max_length=140)
    #A field that represents all the contributors of the project
    contributors = models.OneToManyField(blank=False)
    #A field that represents the numbers of upvotes a downvote is -1
    likes = models.IntegerField(default = 0)
    
