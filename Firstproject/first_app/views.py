from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models.functions import Lower
from .models import *
from django.utils import timezone

def hello(request):
    current_stream = Streams.get_current_stream()
    # Добавляем историю поиска для главной страницы
    search_history = request.session.get('search_history', [])
    return render(request, 'base.html', {
        'current_stream': current_stream,
        'search_history': search_history
    })

def page2(request):
    streams = Streams.objects.all()
    search_history = request.session.get('search_history', [])
    return render(request, 'two.html', {
        'streams': streams,
        'search_history': search_history
    })

def page3(request):
    donations = Donations.objects.all()
    search_history = request.session.get('search_history', [])
    return render(request, 'three.html', {
        'donations': donations,
        'search_history': search_history
    })

def page4(request):
    sort_by = request.GET.get('sort', '')
    
    if sort_by == 'nickname':
        users = Users.objects.all().order_by(Lower('nickname'))
    elif sort_by == 'date':
        users = Users.objects.all().order_by('-registration_date')
    else:
        users = Users.objects.all() 
    
    # Получаем историю поиска из сессии
    search_history = request.session.get('search_history', [])
    
    return render(request, 'four.html', {
        'users': users,
        'current_sort': sort_by,
        'search_history': search_history
    })

def page5(request, user_id):
    user = get_object_or_404(Users, id=user_id)
    search_history = request.session.get('search_history', [])
    return render(request, 'five.html', {
        'user': user,
        'search_history': search_history
    })

def search_users(request):
    search_query = request.GET.get('search', '').strip()
    
    if search_query:
        search_history = request.session.get('search_history', [])
        
        if search_query in search_history:
            search_history.remove(search_query)
        
        search_history.insert(0, search_query)
        
        search_history = search_history[:10]
        
        request.session['search_history'] = search_history
    
    if not search_query:
        return redirect('page4')
    
    users = Users.objects.filter(nickname__icontains=search_query)
    
    if users.count() == 1:
        return redirect('page5', user_id=users.first().id)
    elif users.count() > 1:
        return render(request, 'four.html', {
            'users': users,
            'current_sort': '',
            'search_query': search_query,
            'search_history': request.session.get('search_history', [])
        })
    else:
        return render(request, 'four.html', {
            'users': Users.objects.none(),
            'current_sort': '',
            'search_query': search_query,
            'no_results': True,
            'search_history': request.session.get('search_history', [])
        })