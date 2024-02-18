from django.urls import path

from . import views
from pages.views import HomePageView, KlienciPageView, MapaPageView, KontaktPageView, BSHPageView, load_infowindow, \
    apiexternaltasktrigger, apiexternaliotdevice, apiexternaltaskactivejobs

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home/', HomePageView.as_view(), name='home'),
    path('klienci/', KlienciPageView.as_view(), name='klienci'),
    path('mapa/', MapaPageView.as_view(), name='mapa'),
    path('kontakt/', KontaktPageView.as_view(), name='kontakt'),
    path('bsh/', BSHPageView.as_view(), name='bsh'),
    path('load_infowindow/', load_infowindow, name='load_infowindow'),
    path('api/externaltask/trigger', apiexternaltasktrigger, name='apiexternaltasktrigger'),
    path('api/externaliotdevice', apiexternaliotdevice, name='apiexternaliotdevice'),
    path('api/externaltask/active/jobs', apiexternaltaskactivejobs, name='apiexternaltaskactivejobs'),
]