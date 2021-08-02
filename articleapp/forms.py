from django.forms import ModelForm

from articleapp.models import Article


class ArtileCreationForm(ModelForm):
    class Meta:
        model = Article
        fields= ['title','image','content']