

from django import forms
from .models import Proposal, Authority,ClubHead

from django import forms
from .models import Proposal, Authority

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        exclude = ['date', 'time']  # Exclude date and time fields from the form

    authorities = forms.ModelMultipleChoiceField(queryset=Authority.objects.all(), widget=forms.CheckboxSelectMultiple)

class ClubHeadLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class AuthorityLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)