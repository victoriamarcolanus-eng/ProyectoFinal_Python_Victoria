from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('about/', views.about, name="about"),
    # ESTA ES LA QUE FALTA:
    path('pages/', views.listar_posts, name="pages"), 
    
    path('pages/<int:pk>/', views.detalle_post, name="post_detail"),
    path('pages/create/', views.PostCreateView.as_view(), name="post_create"),
    path('pages/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post_delete"),
]