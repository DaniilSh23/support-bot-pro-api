from django.urls import path

from support_bot_api.views import BotUserView, AppealView, KnowledgeBaseView

urlpatterns = [
    path('bot_user/', BotUserView.as_view(), name='bot_user'),
    path('appeal/', AppealView.as_view(), name='appeal'),
    path('knowledge_base/', KnowledgeBaseView.as_view(), name='knowledge_base')
]