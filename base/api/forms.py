from django import forms
from .models import UploadModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        fields = ('title', 'caption', 'image')
        widgets = {
            'image': forms.ClearableFileInput(attrs={"class": "file-area"}),
        }
    # def __init__(self, *args, **kwargs):
    #     super(UploadForm, self).__init__(*args, **kwargs)
    #     self.fields['title','caption'].required = False