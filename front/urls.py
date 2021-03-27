from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('view/<str:slug>', views.category_list, name='category'),
    path('show/<int:pk>', views.category_list, name='category_id'),
    path('text_id/<int:pk>', views.text, name='post_detail_id'),
    path('tegs/<str:slug>', views.tegs, name='teg')
]