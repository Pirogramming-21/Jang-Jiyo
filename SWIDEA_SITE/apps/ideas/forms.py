from django import forms
from .models import Idea
from apps.devtools.models import DevTool

class IdeaForm(forms.ModelForm):
   devtool = forms.ModelChoiceField(queryset=DevTool.objects.all(), required=True, label="예상 개발툴")

   class Meta():
      model = Idea
      fields = ('__all__')