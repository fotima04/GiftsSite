from django.contrib import admin
from django.urls import path,include
from .views import HomePageView,AboutView,GiftsView,ContactView,Giftsdetail
urlpatterns = [
path('',HomePageView.as_view(),name='home'),
path('about/',AboutView.as_view(),name='about'),
path('gifts/',GiftsView.as_view(),name='gifts'),
path('contact/',ContactView.as_view(),name='contact'),
path('detailgifts/<id>/',Giftsdetail.as_view(),name='detail')
]
