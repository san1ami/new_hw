from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=CustomUser.GENDER, required=True)
    city = forms.CharField(required=True)

    class Meta: 
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'gender',
            'city'
        )
    def save(self, commit = True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user