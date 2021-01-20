from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField("TITLE", max_length=100, blank=True)
    url = models.URLField("URL", unique=True)

    # 레코드(셀값 표햔)
    def __str__(self):
        return self.title
