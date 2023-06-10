from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.coins_index, name='home'),
    path('coins/<int:coin_id>/', views.coin_detail, name='detail'),
    path('about', views.about, name='about'),
] 