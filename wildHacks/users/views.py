from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View

from .forms import *
from .models import *

def logout_view(request):
    """
    Logouts user and redirects to the hompage
    """
    logout(request)
    messages.success(request,
            """ It's okay that you logged out. I don't like you either. """
            )
    return HttpResponseRedirect(reverse('home'))

class SignUpView(View):
    """
    Has the GET and POST methods for the signing up to be a user
    """
    template_name = 'users/sign_up.html'
    form = UserCreationForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form' : self.form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST or None)
        
        if form.is_valid():
            save_it = form.save(commit=True)
            save_it.save()
            messages.success(request, 
                    """
                    Thanks for joining. This could possibly be the most life
                    changing event of your young life.
                    """
                    )
            return HttpResponseRedirect(reverse('thanks'))
        else:
            messages.error(request,
                    """
                    There seems to be an error with your application please try
                    again.
                    """
                    )
            return HttpReponseRedirect(reverse('users:sign_up'))

class LoginView(View):
    """
    Logs user into the website
    """
    template_name = 'users/login.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 
                    """
                    Seems someone made a mistake please try again
                    """
                    )
            return HttpResponseRedirect(reverse('users:login'))
        else:
            if user.is_active:
                login(request, user)
                messages.success(request,
                        """
                        You did it! You successfully logged in. I bet your
                        mother would be so proud of you right now.
                        """
                        )
                return HttpResponseRedirect(reverse('thanks'))
            else:
                messages.success(request,
                        """
                        Looks like your not considered an active user.
                        Please leave no one wants you here. 
                        """
                        )
                return HttpResponseRedirect(reverse('thanks'))


