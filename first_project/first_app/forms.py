from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower()!='a':
        raise forms.ValidationError("NAME NEEDS TO START WITH a")

class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_a])
    Email=forms.EmailField()
    vemail=forms.EmailField(label='Enter your email Again:')
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_data=super().clean()
        email=all_data['Email']
        Vemail=all_data['vemail']

        if email!=Vemail:
            raise forms.ValidationError("EMAILS DO NOT MATCH")
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("ROBOT CATCHED!!!!")
    #     return botcatcher
