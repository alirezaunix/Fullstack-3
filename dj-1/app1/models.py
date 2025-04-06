from django.db import models

# Create your models here.
#Django ORM
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title_des=models.CharField(max_length=255)
    post_date=models.DateField()
    post_text_1=models.CharField(max_length=255)
    post_text_2=models.CharField(max_length=255)
    
    