from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(label = 'Enter your prompt:',
                             max_length = 500,
                             widget=forms.Textarea)

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         fields = ['']