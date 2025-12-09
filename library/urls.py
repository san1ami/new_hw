from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('about/', views.about, name='about'),
    path('time/', views.current_time),
    path('quote/', views.random_quote),

    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
