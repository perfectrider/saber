from django.urls import path
from .views import BuildView

urlpatterns = [
    path('builds/', BuildView.as_view(), name='builds'),
]
