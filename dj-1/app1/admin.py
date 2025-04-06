from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #list_display=['id','title_des','post_date','post_text_1','post_text_2']
    pass