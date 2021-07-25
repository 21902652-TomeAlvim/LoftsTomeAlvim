from django import forms

class CommentForm(forms.Form):
    username = forms.CharField(label="Name", max_length=50)
    description = forms.CharField(label="Comment", widget=forms.Textarea,  max_length=300)
    username.widget.attrs.update({"class": "form-control"})
    description.widget.attrs.update({"class": "form-control"})

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", max_length=100)

class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", max_length=100)
    password_confirmation = forms.CharField(label="Password Confirmation", max_length=100)

class ContactForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    phone_number = forms.CharField(max_length=25, label="Phone Number")
    email = forms.EmailField(label="Email")
    date_of_birth = forms.DateField(label="Date of Birth", required=False)
    message = forms.CharField(label="Message", widget=forms.Textarea,  max_length=500)
    message.widget.attrs.update({"class": "form-control"})
