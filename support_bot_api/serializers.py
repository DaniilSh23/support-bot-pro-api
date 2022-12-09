from rest_framework import serializers
from support_bot_api.models import BotUser, Appeal, KnowledgeBase


class BotUsersSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели пользователей бота"""

    class Meta:
        model = BotUser
        fields = '__all__'


class AppealSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Appeal"""

    class Meta:
        model = Appeal
        fields = '__all__'


class KnowledgeBaseSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели KnowledgeBase"""

    class Meta:
        model = KnowledgeBase
        fields = '__all__'

