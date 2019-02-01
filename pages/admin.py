from django.contrib import admin

# Register your models here.

from .models import Page 

class PageAdmin(admin.ModelAdmin):
	list_display = ['email', 'timestamp', 'updated']
	class Meta:
		model = Page


admin.site.register(Page, PageAdmin) 