from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail

# Create your models here.
# 1. 모델(스키마) 정의
# DB 테이블을 정의하고,
# 각각의 컬럼(or 필드) 정의
class Article(models.Model):
    # CharField - 필수인자로 max_length 지정
    # id : integer 자동으로 정의(Primary Key)
    # id = models.AutoField(primary_key=True) -> Integer 값들이 자동으로 하나씩 증가(AUTOCREMENT)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # ImageSpecField : Input 하나만 받고 처리해서 저장
    # ProcessedImageField : Input 받은 것을 처리해서 저장
    # ResizeToFill: 300 * 300
    # ResizeToFit : 긴쪽을(너비 혹은 높이) 300에 맞추고 비율에 맞게 자름
    image_thumbnail = ImageSpecField(
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 80}
    )
    # image_thumbnail = ProcessedImageField(
    #     blank=True,
    #     processors=[ResizeToFill(300, 300)],
    #     format='JPEG',
    #     options={'quality': 80}
    # )
    # DateTimeField
    #     auto_now_add : 생성시 자동으로 저장
    #     auto_now : 수정시마다 자동으로 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.id}-{self.title}>'

# models.py : python 클래스 정의
#           : 모델 설계도
# makemigrations : migragtion 파일 생성
#                : DB 설계도 작성
# migrate : migrate 파일 DB 반영 

class Comment(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # on_delete
    # 1. CASCADE : 글이 삭제 되었을 때 모든 댓글을 삭제
    # 2. PROTECT : 댓글이 존재하면 글 삭제 안됨.
    # 3. SET_NULL : 글이 삭제되면 NULL로 치환.(NOT NULL일 경우 옵션 사용X)
    # 4. SET_DEFAULT : 디폴트 값으로 치환.