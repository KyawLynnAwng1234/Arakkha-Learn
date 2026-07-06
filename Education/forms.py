from django import forms
from .models import Lesson, Course
from django_ckeditor_5.widgets import CKEditor5Widget

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        # Exclude metadata fields that are auto-generated
        fields = ['course', 'title', 'summary', 'content', 'video_material', 'attachment']

        widgets = {
        "content": CKEditor5Widget(config_name="default"),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Match class formatting to keep your HTML clean
        for field in self.fields.values():
            field.required = True
        
        # Summary and files can be optional
        self.fields['summary'].required = False
        self.fields['video_material'].required = False
        self.fields['attachment'].required = False