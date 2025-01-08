from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm

# Псевдо-список существующих пользователей
users = ('Takehiko', 'TrueUser', 'Max')


def sign_up_by_html(request):
    info = {}  # Создаём словарь для передачи данных в шаблон

    if request.method == 'POST':
        # Извлекаем данные из формы
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:
            age = int(age)
        except ValueError:
            info['error'] = "Возраст должен быть числом."
            return render(request, 'registration_page.html', info)
        if username in users:
            info['error'] = "Пользователь с таким логином уже существует."
        elif password != repeat_password:
            info['error'] = "Пароли не совпадают."
        elif age < 18:
            info['error'] = "Регистрация доступна только для пользователей старше 18 лет."
        else:
            info['message'] = f"Приветствуем, {username}!"
            info['success'] = True  # Флаг для успешной регистрации

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Извлекаем данные из формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in users:
                info['error'] = "Пользователь с таким логином уже существует."
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают."
            elif age < 18:
                info['error'] = "Регистрация доступна только для пользователей старше 18 лет."
            else:
                info['message'] = f"Приветствуем, {username}!"
                form = RegistrationForm()
    else:
        info['form'] = RegistrationForm()
        return render(request, 'registration_page.html', info)

    info['form'] = form
    return render(request, 'registration_page.html', info)

