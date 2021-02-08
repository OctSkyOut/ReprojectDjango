from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="TITLE")
    slug = models.SlugField(
        "SLUG",
        unique=True,
        max_length=100,
        allow_unicode=True,
        help_text="타이틀의 내용을 간략화 시켜줍니다.",
    )
    description = models.CharField(
        "DESCRIPTION", max_length=100, blank=True, help_text="간략한 설명"
    )
    content = models.TextField(
        "CONTENT",
    )
    create_dt = models.DateTimeField("CREATE_DT", auto_now_add=True)
    modify_dt = models.DateTimeField("MODIFY_DT", auto_now_add=True)

    # tag Table
    tags = TaggableManager("TAG", blank=True)

    class Meta:
        verbose_name = "post"  # 테이블 단수별칭
        verbose_name_plural = "posts"  # 테이블 복수 별칭
        db_table = "blog_posts"  # 테이블 이름
        ordering = ("-modify_dt",)  # 정렬순서 = 수정날짜 순서

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
