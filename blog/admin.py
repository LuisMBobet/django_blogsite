from django.contrib import admin
from .models import Post,Image,Project,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title','post_date')
    list_filter = ['post_date']
    search_fields = ['post_title','post_content']
    readonly_fields=('post_date','post_slug')

class ImageUpload(admin.ModelAdmin):
    list_display = ('image_id','image_name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name',)
    readonly_fields = ('project_slug','project_status_colour',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    readonly_fields = ('tag_colour',)

admin.site.register(Post,PostAdmin)
admin.site.register(Image,ImageUpload)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Tag,TagAdmin)
# Register your models here.
