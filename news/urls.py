from operator import index
from django.urls import URLPattern, path
from .views import get_category, index
urlpatterns = [
    path('', index),
    path('category/<int:category_id>/', get_category)
]