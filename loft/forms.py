from django import forms

class CommentForm(forms.Form):
    username = forms.CharField(label="Name", max_length=50)
    description = forms.CharField(label="Comment", widget=forms.Textarea,  max_length=300)
    username.widget.attrs.update({"class": "form-control"})
    description.widget.attrs.update({"class": "form-control"})
