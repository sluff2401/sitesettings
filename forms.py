from django                                 import forms
#from django.forms.widgets                   import CheckboxSelectMultiple
#from django.utils                           import timezone
#from django.contrib.auth.models             import User
from .models                                import StSt
#from django.contrib.auth.forms              import SetPasswordForm, PasswordChangeForm


class UpdateAdvertForm(forms.ModelForm):
    class Meta:
        model = StSt
        fields = ('advert', 'contact_info')

class InsertAdvertForm(forms.ModelForm):
    class Meta:
        model = StSt
        fields = ('advert', 'contact_info')