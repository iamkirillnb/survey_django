from django.contrib import admin
from .models import Quest, MySurvey, Users

class QuestAdmin(admin.ModelAdmin):
    list_display = ('text', 'survey', )

class MySurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'end',)
    list_display_links = ('id', 'title', )

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'qwes', 'sur',)
    list_display_links = ('answer',)

admin.site.register(Quest, QuestAdmin)
admin.site.register(MySurvey, MySurveyAdmin)

admin.site.register(Users, UserAdmin)

