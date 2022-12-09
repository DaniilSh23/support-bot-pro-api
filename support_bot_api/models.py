from django.db import models


class BotUser(models.Model):
    """Модель пользователя бота"""

    tlg_id = models.IntegerField(verbose_name='Телеграм ID', default=0)
    username = models.CharField(verbose_name='Телеграм username', max_length=100, blank=True, null=True)
    org_name = models.CharField(verbose_name='Название организации', max_length=100, blank=True, null=True)
    telephone = models.CharField(verbose_name='Телефон', max_length=12, blank=True, null=True)
    city = models.CharField(verbose_name='Город', max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(verbose_name='Персонал', default=False)
    is_active_staff = models.BooleanField(verbose_name='Активный персонал', default=False)

    class Meta:
        db_table = 'Таблица пользователей поддержки'
        ordering = ['-id']
        verbose_name = 'Пользователь поддержки'
        verbose_name_plural = 'Пользователи поддержки'

    def __str__(self):
        return f'Телеграм ID пользователя: {self.tlg_id}'


class Appeal(models.Model):
    """Модель обращений пользователей"""

    appeal_link = models.URLField(verbose_name='Ссылка на обращение', max_length=200)
    last_call = models.DateTimeField(verbose_name='Крайнее обращение', auto_now=True)
    last_operator = models.IntegerField(verbose_name='Крайний оператор(TLG ID)', default=0)
    author = models.IntegerField(verbose_name='Автор обращения(TLG ID)', default=0)

    class Meta:
        db_table = 'Таблица обращений поддержки'
        ordering = ['-id']
        verbose_name = 'Обращение поддержки'
        verbose_name_plural = 'Обращения поддержки'

    def __str__(self):
        return self.appeal_link


class KnowledgeBase(models.Model):
    """Модель для хранения данных о постах из базы знаний"""

    title = models.CharField(verbose_name='Название', max_length=100)
    category = models.CharField(verbose_name='Категория', max_length=200)
    tlg_msg_id = models.IntegerField(verbose_name='ID поста', default=0)
    link_to_post = models.URLField(verbose_name='Ссылка на пост', max_length=200)

    class Meta:
        db_table = 'Таблица базы знаний'
        ordering = ['id']
        verbose_name = 'База знаний'
        verbose_name_plural = 'База знаний'

    def __str__(self):
        return self.title
