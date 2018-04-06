from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        send_mail(
            'Hi '+ self.cleaned_data.get("name"),
            self.cleaned_data.get("message"),
            'leninmishra92@gmail.com',
            ['l.mishra@talkingpotato.nl'],
            fail_silently=False,
        )