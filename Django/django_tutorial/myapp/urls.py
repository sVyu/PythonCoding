from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    # path('read/1/', views.read)
    path('read/<id>/', views.read),
    path('update/<id>/', views.update),
    path('delete/', views.delete)
]
