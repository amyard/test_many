from django.contrib import admin
from .models import Publication, Article


admin.site.register(Publication)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'pk','headline']