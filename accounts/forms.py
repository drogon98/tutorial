from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User  # user is our model to extend


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # overriding and making the email field a required field

    class Meta:  # class meta gives us general information about the form
        model = User
        # ordering="email"
        # proxy=True
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
        # by default email first_name and last_name are not saved in our user models
        # we have to first save them before doing anything else

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]
