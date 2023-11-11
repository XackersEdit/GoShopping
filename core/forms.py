from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from .models import Region, Cities
from .models import CustomUser

style = 'w-full px-6 py-4 rounded-xl border !important'


class ProfileEditForm(forms.ModelForm):
    regions = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Select a region",
                                     widget=forms.Select(attrs={
                                         'class': style
                                     }))
    cities = forms.ModelChoiceField(queryset=Cities.objects.none(), empty_label="Select a city",
                                    widget=forms.Select(attrs={
                                        'class': style
                                    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': style,
        'placeholder': '+998 90 999 9999'
    }))
    fname = forms.CharField(widget=forms.TextInput(attrs={
        'class': style,
        'placeholder': 'Abdurashid'
    }))
    lname = forms.CharField(widget=forms.TextInput(attrs={
        'class': style,
        'placeholder': "Jo'rayev"
    }))

    class Meta:
        model = CustomUser
        fields = ('regions', 'cities', 'address', 'phone_number', 'fname', 'lname', 'avatar', 'bio')
        widgets = {
            'address': forms.TextInput(attrs={
                'class': style,
                'placeholder': 'Alisher 31, Bahor MFY'
            }),
            'bio': forms.Textarea(attrs={
                'class': style,
                'placeholder': 'Alisher 31, Bahor MFY'
            }),
            'avatar': forms.FileInput(attrs={
                'class': style,
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'regions' in self.data:
            try:
                region_id = int(self.data.get('regions'))
                self.fields['cities'].queryset = Cities.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['cities'].queryset = Cities.objects.filter(region_id=self.instance.regions_id).order_by(
                'name')

        # fields = ['regions', 'cities', 'address', 'phone_number', 'fname', 'lname', 'avatar', 'bio']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': style,
        'placeholder': 'username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': style,
        'placeholder': 'Password'
    }))


User = get_user_model()


class SignupForm(UserCreationForm):
    regions = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Select a region", widget=forms.Select(attrs={
                                                                                                                     'class': style
    }))
    cities = forms.ModelChoiceField(queryset=Cities.objects.none(), empty_label="Select a city", widget=forms.Select(attrs={
                                                                                                                     'class': style
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': style,
        'placeholder': '+998 90 999 9999'
    }))
    fname = forms.CharField(widget=forms.TextInput(attrs={
        'class': style,
        'placeholder': 'Abdurashid'
    }))
    lname = forms.CharField(widget=forms.TextInput(attrs={
        'class': style,
        'placeholder': "Jo'rayev"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': style,
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': style,
        'placeholder': 'Re-type password'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'address', 'password1', 'password2', 'fname', 'lname', 'regions',
                  'avatar', 'cities', 'bio')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': style,
                'placeholder': 'username'
            }),
            'address': forms.TextInput(attrs={
                'class': style,
                'placeholder': 'Alisher 31, Bahor MFY'
            }),
            'bio': forms.Textarea(attrs={
                'class': style,
                'placeholder': 'Alisher 31, Bahor MFY'
            }),
            'email': forms.EmailInput(attrs={
                'class': style,
                'placeholder': 'example@gmail.com',
            }),
        'avatar': forms.FileInput(attrs={
            'class': style,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'regions' in self.data:
            try:
                region_id = int(self.data.get('regions'))
                self.fields['cities'].queryset = Cities.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['cities'].queryset = Cities.objects.filter(region_id=self.instance.regions_id).order_by(
                'name')
            
class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    phonenumber = forms.CharField(max_length=15, required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

