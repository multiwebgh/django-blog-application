from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from authentication.models import UserProfile



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove default help texts (password rules, username hints)
        for name in ("username", "password1", "password2"):
            if name in self.fields:
                self.fields[name].help_text = ""
        # Add Bootstrap form-control class to widgets
        for field_name, field in self.fields.items():
            css_class = field.widget.attrs.get("class", "")
            classes = (css_class + " form-control").strip()
            field.widget.attrs.update({"class": classes})
            # Use the field label as placeholder when not provided
            placeholder = field.widget.attrs.get("placeholder")
            if not placeholder:
                label = getattr(field, 'label', '') or ''
                if not label:
                    # sensible fallback from field name
                    label = field_name.replace('_', ' ').capitalize()
                # explicit nicer text for email
                if field_name == 'email':
                    label = 'Email address'
                field.widget.attrs.update({"placeholder": label})

    class Meta:
        model = User
        fields = ("username", "email") # password1 and password2 are included automatically



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("photo", "bio")
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        
class UpdateProfile(UserChangeForm):        
    password = None  # Exclude the password field

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")   