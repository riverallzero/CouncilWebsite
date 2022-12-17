from django import forms
from room.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'head_image']
        labels = {
            'subject': '제목',
            'content': '내용',
            'head_image': '이미지',
        }

