from django import forms

from newspaper.models import EmailSubscribe


class EmailSubscribeForm(forms.ModelForm):
    class Meta:
        model = EmailSubscribe
        fields = ('email', )
