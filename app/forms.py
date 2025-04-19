from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(ladel = 'Enter your prompt:', max_length = 500)