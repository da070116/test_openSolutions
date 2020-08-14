from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import VisitorCreationForm, VisitorChangeForm
from .models import Visitor


class Manager(UserAdmin):
    add_form = VisitorCreationForm
    form = VisitorChangeForm
    model = Visitor
    list_display = ['email', 'username',]


admin.site.register(Visitor, Manager)
