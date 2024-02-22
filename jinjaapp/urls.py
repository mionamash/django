from djangonao.urls import path
from jinjaapp import views

urlpatterns =[
  path('',views.home,name='my_home'),
    path('about/', views.about, name='my_about'),
    path('contact/', views.contacts, name='my_contacts'),
  path('gallery/', views.gallery, name='my_gallery'),

]