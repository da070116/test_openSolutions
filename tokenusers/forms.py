from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Visitor


class VisitorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Visitor
        fields = ('username', 'email')


class VisitorChangeForm(UserChangeForm):
    class Meta:
        model = Visitor
        fields = UserChangeForm.Meta.fields
