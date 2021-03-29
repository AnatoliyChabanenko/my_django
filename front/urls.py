from django.urls import path
from . import views
from .views import HomeView, News_list, Text, Tegs

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('view/<str:slug>', News_list.as_view(), name='category'),
    path('show/<int:pk>', News_list.as_view(), name='category_id'),
    path('text_id/<int:pk>', Text.as_view(), name='post_detail_id'),
    path('tegs/<int:pk>', Tegs.as_view(), name='teg')
]