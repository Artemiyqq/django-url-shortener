from django.contrib import admin
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name=''),
    path('<str:shortened_url>', main_views.redirect_to_original)
]

handler404 = 'main.views.error_404_view'
