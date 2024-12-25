from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



User = get_user_model()

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = 'Your email address'
        self.fields['email'].required = True
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''



    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_qs = User.objects.filter(email=email)
        if email_qs.exists() and len(email) > 254:
            raise forms.ValidationError('This email has already been registered or is too long')
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Your email address'
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_qs = User.objects.filter(email=email).exclude(id=self.instance.id)
        if email_qs.exists() or len(email) > 254:
            raise forms.ValidationError('This email already in use or is too long')
        return email