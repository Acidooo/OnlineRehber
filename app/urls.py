from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name="search"),
    path('', views.HomePageView.as_view(), name="home"),
    path('contacts/create', views.ContactCreateView.as_view(), name="create"),
    path('detail/<int:pk>/', views.ContactDetailView.as_view(), name="detail"),
    path('contacts/update/<int:pk>', views.ContactUpdateView.as_view(), name="update"),
    path('contacts/delete/<int:pk>', views.ContactDeleteView.as_view(), name="delete"),
    path('signup/', views.SignUpView.as_view(), name="signup"),

]
