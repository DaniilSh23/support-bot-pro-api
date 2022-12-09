from django.contrib import admin
from support_bot_api.models import BotUser, Appeal, KnowledgeBase


class BotUserAdmin(admin.ModelAdmin):
    """Регистрация модели BotUser в админке"""

    list_display = ('tlg_id', 'org_name', 'city', 'telephone', 'is_staff', 'is_active_staff')
    list_display_links = ('tlg_id', 'org_name', 'city', 'telephone', 'is_staff', 'is_active_staff')
    search_fields = ('org_name', 'tlg_id', 'city',  'telephone')
    list_filter = ('is_staff', 'is_active_staff', 'city')


class AppealAdmin(admin.ModelAdmin):
    """Регистрация модели Appeal в админке"""

    list_display = ('last_operator', 'last_call', 'appeal_link')
    list_display_links = ('last_operator', 'last_call', 'appeal_link')
    search_fields = ('last_operator', 'last_call', 'author')
    list_filter = ('last_operator', 'last_call')


class KnowledgeBaseAdmin(admin.ModelAdmin):
    """Регистрация модели KnowledgeBase в админке"""

    list_display = ('id', 'title', 'tlg_msg_id')
    list_display_links = ('id', 'title', 'tlg_msg_id')
    search_fields = ('title', 'category', 'tlg_msg_id', 'link_to_post')
    list_filter = ('category',)


admin.site.register(BotUser, BotUserAdmin)
admin.site.register(Appeal, AppealAdmin)
admin.site.register(KnowledgeBase, KnowledgeBaseAdmin)
