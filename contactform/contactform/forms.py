from django import forms

class contactformemail(forms.Form):
    Name=forms.CharField(max_length=50)
    contact=forms.CharField()
    fromemail=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message=forms.CharField(widget=forms.Textarea,max_length=2000)