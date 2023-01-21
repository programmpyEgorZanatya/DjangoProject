from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('items_list/',views.items_list, name="items-list"),
    path('item/<int:id>',views.item_page, name="item_page"),

]