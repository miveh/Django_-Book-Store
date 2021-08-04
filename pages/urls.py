# pages/urls.py
from django.urls import path
# from .views import home_page_view
from .views import HomePageView, AboutPageView

urlpatterns = [
    # path('', home_page_view, name='home')
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),  # new
]
