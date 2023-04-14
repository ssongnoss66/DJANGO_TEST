from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label="리뷰 제목",
        widget=forms.TextInput(attrs={
            "placeholder": "리뷰 제목을 입력하세요"
        }),
    )
    content = forms.CharField(
        label="리뷰 내용",
        widget=forms.Textarea(attrs={
            "placeholder": "리뷰 내용을 입력하세요"
        }),
    )
    movie = forms.CharField(
        label="영화 제목",
        widget=forms.TextInput(attrs={
            "placeholder": "영화 제목을 입력하세요"
        }),
    )
    image = forms.ImageField(
        label="관련 이미지",
        widget=forms.FileInput(attrs={
            "placeholder": "관련 이미지를 업로드하세요"
        })
    )
    class Meta():
        model = Review
        fields = ('title', 'content', 'movie', 'image')

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="새 댓글",
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "placeholder": "새로운 댓글을 입력하세요",
            "aria-label": "새로운 댓글을 입력하세요",
            "aria-describedby": "basic-addon2",
        }),
    )
    class Meta():
        model = Comment
        fields = ('content', )