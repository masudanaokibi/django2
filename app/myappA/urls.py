from django.urls import path
from . import views

app_name = 'myappA'
urlpatterns = [
    # path('', views.PersonListView.as_view())
    path('', views.index, name='index'),
]
