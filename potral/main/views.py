from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from main.models import News, Author, Category
from django.views import View

from django.urls import reverse_lazy

from main.forms import AuthorForm
from django.views.generic.edit import UpdateView



# Create your views here.

def news(request):
    return render(request, "main/news_list.html")



class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html') 


class NewsList(ListView):
    model = News
    template_name = 'news_list.html'

class AuthorsList(ListView):
    model = Author
    template_name = 'authors_list.html'
    #context_object_name = "portal"

class AuthorsUpdateView(UpdateView):
    model = Author
    from_class = AuthorForm
    template_name = 'update_author.html'
    success_url = reverse_lazy('portal:list')