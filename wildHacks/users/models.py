from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """
    The manager class for user
    """
    def create_user(self, email, first_name="John", last_name="Doe", password=None):
        if not email:
            raise ValueError('User must ahve email')

        user = self.model(
                email=self.normalize_email(email),
                first_name = first_name,
                last_name = last_name
                )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name='super', last_name='user'):
        user = self.create_user(email, first_name, last_name, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_active = False
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    Represents any user of the website
    """
    #date that user join
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    email = models.EmailField(max_length=100, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100, default="John")
    last_name = models.CharField(max_length=100, default="Doe")

    #Determins whether a person is an admin or not
    is_admin = models.BooleanField(default=False)
    is_superuser = False
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

