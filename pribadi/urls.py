from django.urls import path
from . import views

urlpatterns = [
 path('', views.PAGE, name='index'),
 path('biodata-diri', views.ABOUT, name='about'),
 path('album-foto', views.ALBUM, name='album'),
 path('kumpulan-artikel', views.ARTIKEL, name='artikel'),
 path('detail-artikel/<str:id>', views.DETAIL_ARTIKEL, name='detail_artikel'),
 path('kumpulan-khutbah', views.KHUTBAH, name='khutbah'),
 path('detail-khutbah/<str:id>', views.DETAIL_KHUTBAH, name='detail_khutbah'),
]