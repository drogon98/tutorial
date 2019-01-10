from django.urls import path

from . import views
app_name="posts"

urlpatterns=[
  path('home/',views.HomeView.as_view(),name="home"),
  path('connect/<operation>/<int:pk>/',views.change_friend,name="change_friend"),

]
