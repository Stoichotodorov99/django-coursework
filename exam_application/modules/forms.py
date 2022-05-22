from django import forms

from modules.models import ExamRegistration

class ExamRegistrationForm(forms.Form):
    payment_method = forms.ChoiceField(choices=(
        ('cash', 'В брой'),
        ('card', 'С карта'),
        ('bank', 'Банков превод'),
    ))
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(ExamRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Име'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Имейл'
        self.fields['payment_method'].label = 'Начин на плащане'
        self.fields['payment_method'].choices = exam.get_payment_method_choices()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('Моля въведете име')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError('Моля въведете фамилия')
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Моля въведете имейл')
        return email
    
    
