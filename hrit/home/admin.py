from django.contrib import admin
from .models import Content
from .models import Member
from .models import Service
from .models import Work
from django_markdown.models import MarkdownField
from django_markdown.widgets import AdminMarkdownWidget

class CustomModelAdmin(admin.ModelAdmin):
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

admin.site.register(Content, CustomModelAdmin)
admin.site.register(Member, CustomModelAdmin)
admin.site.register(Service, CustomModelAdmin)
admin.site.register(Work, CustomModelAdmin)
