from django.forms import ModelForm
from django.template.defaulttags import comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = comment
        fields = ['content']

