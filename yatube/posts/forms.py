from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].help_text = "Напишите текст сообщения"
        self.fields['group'].help_text = "Выберите сообщество"

    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': 'Текс сообщения',
            'group': 'Сообщество',
        }
