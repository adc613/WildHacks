from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(UserAdmin):
	"""
	User admin class controls what is shown in he admin page
	"""
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('email', 'first_name','last_name',
		'is_active', 'is_superuser')
	list_filter = ('is_superuser','is_admin')

	fieldsets = (
		(None, {'fields' : (
		'email', 'first_name','last_name', 'password', 'is_superuser', 'is_active'
		 )
		}), ('Groups', {'fields' :('groups',)})
		)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields' : {'email', 'first_name','last_name', 'password1', 'password2'}
			}
		),
	)

	search_fields = ('email', 'first_name', 'last_name')
	ordering = ('last_name',)

admin.site.register(User, UserAdmin)

