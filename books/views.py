from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Book, Review
from .forms import ReviewForm
import random


def about(request):
    return HttpResponse("<h1>О себе</h1><p>Изучаем Django и книги!</p>")


def current_time(request):
    time_str = "12:00"
    hour = int(time_str.split(":")[0])
    if hour < 12:
        message = "Сейчас утро"
    elif 12 <= hour <= 14:
        message = "Сейчас обед"
    elif 15 <= hour <= 20:
        message = "Сейчас вечер"
    else:
        message = "Сейчас ночь"
    return HttpResponse(f"<h2>{message}</h2>")


def random_quote(request):
    quotes = [
        "Образование есть то, что остается после того, как забыто все выученное в школе",
        "Альберт Эйнштейн"
        "Книга — великая вещь, пока человек умеет ею пользоваться",
        "Александр Блок"
        "Самая трудная вещь на свете — это думать своей собственной головой",
        "Бертольт Брехт"
        "Жить — значит меняться, меняться — значит взрослеть, а взрослеть — значит непрерывно творить самого себя",
        "Анри Бергсон"
        "Любовь — это единственное, что может поспорить с человеческим одиночеством",
        "Гарриет Бичер-Стоу"
        "Время ничего не меняет. Меняемся мы",
        "Генри Дэвид Торо"
        "Чтобы написать хорошую книгу, нужно только три вещи: знать предмет, владеть языком и обладать способностью выражать свои мысли",
        "Уильям Сомерсет Моэм"
        "Умный человек не делает сам всех ошибок — он предоставляет шанс другим",
        "Уинстон Черчилль"
        "Есть преступления хуже, чем сжигать книги. Например — не читать их",
        "Рэй Брэдбери"
        "Человек — единственное животное, которое краснеет (или должно краснеть)",
        "Марк Твен"
    ]
    quote = random.choice(quotes)
    return HttpResponse(f"<h2>{quote}</h2>")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()

    return render(request, 'books/book_detail.html', {'book': book, 'form': form})
