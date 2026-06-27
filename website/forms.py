from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField
from simplemathcaptcha.fields import MathCaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
class ContactForm(forms.ModelForm):
    # captcha = CaptchaField()
    captcha = MathCaptchaField()
    
    class Meta:
        model = Contact
        fields = '__all__'
        
class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = "__all__"