from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
# Create your views here.

# request - обязат. аргумент; это модуль Python, который вы можете использовать для отправки всех видов HTTP-запросов.


# получение всех новостей
def index(request):
    news = News.objects.order_by('-creation_date')
    # первая переменная request (всегда), вторая переменная - название шаблона
    # третья переменная - передача контекста, если его много, то создаётся переменная context
    # context в данном случае должен быть словарём
    return render(request, 'news/index.html', {'news': news, 'title': 'Новости', 'list_name': 'Список всех новостей'})


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


# получение последних пяти новостей
def last_news(request):
    latest_news = News.objects.exclude(is_published=False).order_by('-creation_date')[:5]
    return render(request, 'news/index.html', {'news': latest_news,
                                               'title': 'Новости',
                                               'list_name': 'Список последних новостей'})


def view_news(request, new_id):
    # new_item = News.objects.get(pk=new_id)
    new_item = get_object_or_404(News, pk=new_id)
    return render(request, 'news/view_news.html', {'new_item': new_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы зарегистрированы!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации.')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы были успешно авторизованы! Сейчас вы находитесь на главной странице.')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации.')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
