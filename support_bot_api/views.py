from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from support_bot_api.models import BotUser, Appeal, KnowledgeBase
from support_bot_api.serializers import BotUsersSerializer, AppealSerializer, KnowledgeBaseSerializer


class BotUserView(APIView):
    """
    Представление для получения данных модели BotUser
    """

    def get(self, request, format=None):
        """
        Ответ на GET запрос. Отдаём информацию из таблицы пользователей бота.
            ?tlg_id=... - Получение инфо по телеграм id пользователя.
        """

        tlg_id = request.query_params.get('tlg_id')
        if tlg_id:
            try:
                # Если не возьмём, то создадим
                bot_user, is_created = BotUser.objects.get_or_create(
                    tlg_id=tlg_id,
                    defaults={'tlg_id': tlg_id}
                )
            except Exception:
                return Response(f'Пользователь с id телеграм:{tlg_id} не существует.', status.HTTP_400_BAD_REQUEST)
            bot_users_serializer_data = BotUsersSerializer(bot_user, many=False).data
            return Response({'object': bot_users_serializer_data, 'is_created': is_created}, status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """
        POST запрос для обновления (по tlg_id) или создания новой записи о пользователе.
        """

        serializer = BotUsersSerializer(data=request.data)
        if serializer.is_valid():
            bot_user_object = BotUser.objects.update_or_create(
                tlg_id=serializer.data.get("tlg_id"),
                defaults=serializer.data
            )
            result_object = BotUsersSerializer(bot_user_object[0]).data
            return Response(result_object, status.HTTP_200_OK)
        else:
            return Response('Переданные данные не прошли валидацию', status.HTTP_400_BAD_REQUEST)


class AppealView(APIView):
    """Представление для работы с инфо из таблицы обращений пользователей."""

    def get(self, request, format=None):
        """GET запрос для получение инфо из таблицы обращений."""

        tlg_id = request.query_params.get('tlg_id')
        if tlg_id:
            try:
                appeal_obj = Appeal.objects.get(author=tlg_id)
            except Exception:
                return Response(f'Обращения польз. с id телеграм:{tlg_id} не существует.', status.HTTP_400_BAD_REQUEST)
            appeal_serializer_data = AppealSerializer(appeal_obj, many=False).data
            return Response(appeal_serializer_data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """POST запрос для записи или обновления данных в таблице обращений"""

        serializer = AppealSerializer(data=request.data)
        if serializer.is_valid():
            appeal_obj = Appeal.objects.update_or_create(
                author=serializer.data.get('author'),
                defaults=serializer.data
            )
            result_object = AppealSerializer(appeal_obj[0]).data
            return Response(result_object, status.HTTP_200_OK)
        else:
            return Response('Переданные данные не прошли валидацию', status.HTTP_400_BAD_REQUEST)


class KnowledgeBaseView(APIView):
    """Представление для работы с моделью базы знаний"""

    def get(self, request, format=None):
        """
        Обработка GET запроса.
            без параметров - получение всех записей
        """

        knowledge_base_objects = KnowledgeBase.objects.all()
        knowledge_base_serializer = KnowledgeBaseSerializer(knowledge_base_objects, many=True).data
        return Response(knowledge_base_serializer, status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Обработка POST запроса для модели базы знаний.
        """

        serializer = KnowledgeBaseSerializer(data=request.data)
        if serializer.is_valid():
            knowledge_base_obj = Appeal.objects.update_or_create(
                title=serializer.data.get('title'),
                defaults=serializer.data
            )
            result_object = AppealSerializer(knowledge_base_obj[0]).data
            return Response(result_object, status.HTTP_200_OK)
        else:
            return Response('Переданные данные не прошли валидацию', status.HTTP_400_BAD_REQUEST)
