from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.index, name='index'),
    path('coins/', views.home, name='home'),
    path('coins/<int:coin_id>/', views.coin_detail, name='detail'),
    path('coins/<int:coin_id>/add_bid/', views.add_bid, name='add_bid'),
    path('coins/<int:coin_id>/add_certification/', views.add_certification, name='add_certification'),
    path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
    path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coin_update'),
    path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coin_delete'),
    path('about/', views.about, name='about'),
    path('certifications/', views.certifications, name='certifications'),
    path('certification/create/', views.CertificationCreate.as_view(), name='certifications_create'),
    path('certification/<int:pk>/update/', views.CertificationUpdate.as_view(), name='certification_update'),
    path('certification/<int:pk>/delete/', views.CertificationDelete.as_view(), name='certification_delete'),
] 