from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    email = models.EmailField(max_length=30, verbose_name='Почта')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        def __str__(self):
            return self.username