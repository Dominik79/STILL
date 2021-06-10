from django.urls import path

from . import views
from .views import HomePageView, KlienciPageView, MapaPageView, KontaktPageView, TelefonyPageView, load_infowindow

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('klienci/', KlienciPageView.as_view(), name='klienci'),
    path('mapa/', MapaPageView.as_view(), name='mapa'),
    path('kontakt/', KontaktPageView.as_view(), name='kontakt'),
    path('telefony/', TelefonyPageView.as_view(), name='telefony'),
    path('load_infowindow/', load_infowindow, name='load_infowindow'),
]