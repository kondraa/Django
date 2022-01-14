from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserLoginForm(AuthenticationForm):

    class Meta():
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Fill out username'
        self.fields['password'].widget.attrs['placeholder'] = 'Fill out password'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Fill out firstname'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Fill out lastname'
        self.fields['email'].widget.attrs['placeholder'] = 'Fill out email'
        self.fields['username'].widget.attrs['placeholder'] = 'Fill out username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Fill out password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Fill out password one more time '
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'