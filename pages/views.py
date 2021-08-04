from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home_page_view(request):
#     return HttpResponse('Hello, World!')
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
