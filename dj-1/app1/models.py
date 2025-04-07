from django.db import models

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title_des=models.CharField(max_length=255,verbose_name="Post Title")
    post_date=models.DateField(verbose_name="Post Date")
    post_text_1=models.CharField(max_length=255,verbose_name="Text Number 1")
    post_text_2 = models.CharField(
        max_length=255, verbose_name="Text Number 2")
    
    def __str__(self):
        return self.title_des