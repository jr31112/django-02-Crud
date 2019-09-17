from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '제목을 입력바랍니다.',
            }
        )
    )
    content = forms.CharField(
        # Django form에서 HTML 속성 지정 -> widget
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content',
                'placeholder' : '내용을 입력바랍니다.',
                'row' : 5,
                'col' : 60
            }
        )
    )