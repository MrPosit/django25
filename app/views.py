from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .models import Todo

@cache_page(60 * 15)
def test_cache(request):
    todos = cache.get('todos')
    if not todos:
        todos = Todo.objects.all()
        cache.set('todos', todos, 6000)
        print('Данные получены из базы данных')
    else:
        print('Данные получены из кеша')
    return render(request, 'test_cache.html', {'todos': todos})
