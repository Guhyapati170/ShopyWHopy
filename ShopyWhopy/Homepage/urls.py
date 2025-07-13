from django.urls import path
from . import views

app_name='Homepage'

urlpatterns = [
    path("", views.index , name="index"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]