from django import forms

from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'mt-2 w-full px-3 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Write your text here . . .',
                'rows': '3',
            }),
        }
