from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class ContactForm(forms.Form):
    fname = forms.CharField(label="First Name", required=False)
    lname = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'fname',
            'lname',
            'email',
            'body',
            Submit('submit', 'Submit', css_class='btn-success'),
        )


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('fname', 'lname', 'email', 'body')
