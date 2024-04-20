# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
import logging


# Получаем экземпляр логгера для этого модуля
logger = logging.getLogger(__name__)


def home(request):
    # HTML-вёрстка и данные о главной странице
    html = """
       <html>
       <head><title>Главная</title></head>
       <body>
           <h1>Добро пожаловать на мой первый Django-сайт!</h1>
           <p>Это главная страница.</p>
       </body>
       </html>
       """
    # Сохраняем информацию о посещении страницы в лог
    logger.info('Посещена главная страница')
    return HttpResponse(html)
#код с ошибкой
"""
    # HTML-вёрстка и данные о главной странице
    html = "<h1>Добро пожаловать на главную страницу!</h1>"

    # Логируем информацию о посещении страницы
    logger.info("Посещена главная страница")

    return render(request, 'myapp/home.html', {'html': html})
"""

def about(request):
    # HTML-вёрстка и данные о странице "О себе"
    html = """
        <html>
        <head><title>О себе</title></head>
        <body>
            <h1>Обо мне</h1>
            <p>Привет! Меня зовут Андрей и я начинающий Django-разработчик.</p>
            <p>На этой странице вы можете узнать немного больше обо мне и моем проекте. 
            либо одежды либо доставки</p>
        </body>
        </html>
        """
    # Сохраняем информацию о посещении страницы в лог
    logger.info('Посещена страница "О себе"')
    return HttpResponse(html)
