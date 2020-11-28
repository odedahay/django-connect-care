from django import forms

# class EmailForm(forms.Form):
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=100)
#     attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     message = forms.CharField(widget = forms.Textarea)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()