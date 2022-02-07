from django import forms
from captcha.fields import ReCaptchaField


class AskForFormCaptcha(forms.Form):
    captcha = ReCaptchaField()
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    message = forms.Textarea()


class GetSampleFormCaptcha(forms.Form):
    captcha = ReCaptchaField()
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)

