from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)
        # # 위젯 설정 1
        # widgets = {
        #     'title' : forms.TextInput(
        #         attrs={
        #             'placeholder' : '제목을 입력바랍니다.',
        #         }
        #     ),
        #     'content' : forms.Textarea(
        #         attrs={
        #             'class' : 'my-content',
        #             'placeholder' : '내용을 입력바랍니다.',
        #             'row' : 5,
        #             'col' : 60
        #         }
        #     )
        # }
    
# 위젯 설정 2
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder' : '제목을 입력바랍니다.',
#             }
#         )
#     )
#     content = forms.CharField(
#         # Django form에서 HTML 속성 지정 -> widget
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class' : 'my-content',
#                 'placeholder' : '내용을 입력바랍니다.',
#                 'row' : 5,
#                 'col' : 60
#             }
#         )
#     )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', )