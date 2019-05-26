from django import forms

class CreatePostForm(forms.Form):
    title = forms.CharField(label='title',max_length=255)
    content = forms.CharField(label='content')

class ContactForm(forms.Form):
    contact_name = forms.CharField(label='contactName',required = True)
    contact_email = forms.EmailField(label='contactEmail',required = True)
    content = forms.CharField(required = True, widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Your message: "
