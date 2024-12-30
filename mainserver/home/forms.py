# forms.py
from django import forms
from home.models import Feedback,ContactServices
from allauth.account.forms import SignupForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
# -------------------------------------------------------------------------------------------------

class FormWithCaptcha(SignupForm):
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
            'data-size': 'compact',
        }
    ))

    def save(self, request):
        user = super().save(request)
        return user

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content', 'rating','real']

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your feedback content (e.g., product or post)',
                'rows': 4,
                'required':False
            }),
            'rating': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'content': 'Feedback Message',
            'rating': 'Rating (1 to 5)',
        }

    # Custom validation (optional)
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactServices
        fields = ['name','email','subject','message']

        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message...',
                'rows': 9,
                'cols':25,
                'required':True
            }),
            'subject': forms.Select(attrs={
                'class': 'form-select',
            }),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),

        }
        

