from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
        widgets = {
            'item': forms.TextInput(attrs={'placeholder': 'Enter your task'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'  # Specify form method if necessary
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))
