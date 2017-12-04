# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Category, Entry
from .forms import CategoryForm, EntryForm

# Create your views here.


def index(request):
    return render(request, 'address_books/index.html')


def check_user(user, owner):
    if user != owner:
        raise Http404


#显示分组
#categorys_page:当前请求需要显示第几页
@login_required
def categorys(request, categorys_page):
    categorys = Category.objects.filter(owner=request.user).order_by('date_added')

    step = 4
    categorys_page = int(categorys_page)
    page_list = range(1, len(categorys) // step + 2)
    categorys = categorys[(categorys_page-1)*step:(categorys_page)*step]

    context = {'categorys':categorys, 'categorys_page':categorys_page, 'page_list':page_list}
    return render(request, 'address_books/categorys.html', context)


#显示分组中的联系人
#category_id:当前分组id
#category_page:当前对应的分组的需要显示第几页
@login_required
def category(request, category_id, category_page):
    category = Category.objects.get(id=category_id)
    if category.owner != request.user:
        raise Http404
    entries = category.entry_set.order_by('-date_added')
    count = entries.count()

    step = 4
    category_page = int(category_page)
    page_list = range(1, count//step + 2)
    entries = entries[(category_page-1)*step:(category_page)*step]

    context = {'entries':entries, 'category':category, 'category_id':category_id, 'count':count, 'category_page':category_page,'page_list':page_list}
    return render(request, 'address_books/category.html', context)


#添加新的分组
@login_required
def new_category(request):
    if request.method != 'POST':
        form = CategoryForm
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return HttpResponseRedirect(reverse('address_books:categorys', args=[1]))
    context = {'form':form}
    return render(request, 'address_books/new_category.html', context)

#编辑分组
@login_required
def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    check_user(request.user, category.owner)
    if request.method != 'POST':
        form = CategoryForm(instance=category)
    else:
        form = CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('address_books:categorys', args=[1,]))
    context = {'category':category, 'form':form, 'category_id':category_id}
    return render(request, 'address_books/edit_category.html', context)


#编辑联系人条目
@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    category = entry.category
    #获取用户对应的所有分组
    owner_categorys = Category.objects.filter(owner=request.user).order_by('date_added')
    if category.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            edit_entry = form.save(commit=False)
            edit_entry.category = owner_categorys.get(id=request.POST['new_category_id'])
            edit_entry.save()
            Entry.objects.filter(id=entry_id).delete()
            return HttpResponseRedirect(reverse('address_books:category', args=[category.id, 1]))
    context = {'category': category, 'form': form, 'entry': entry, 'owner_categorys': owner_categorys}
    return render(request, 'address_books/edit_entry.html', context)


#删除条目
@login_required
def delete_entry(request, category_id, category_page, entry_id):
    try:
        entries = Entry.objects.filter(id=str(entry_id))
        entries.delete()
    except Exception as e:
        context = {'e': e, 'entry_id': entry_id, 'category_id': category_id, 'category_page': category_page}
        return render(request, 'address_books/test.html', context)
    context = {'category_id': category_id, 'category_page': category_page}
    return HttpResponseRedirect(reverse('address_books:category', args=[category_id, category_page]))

#删除分组
@login_required
def delete_category(request, categorys_page, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('address_books:categorys', args=[categorys_page,]))


#添加新的联系人条目
@login_required
def new_entry(request, category_id):
    category = Category.objects.get(id=category_id)
    if category.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.category = category
            new_entry.save()
            return HttpResponseRedirect(reverse('address_books:category', args=[category_id, 1]))
    context = {'category':category, 'form':form}
    return render(request, 'address_books/new_entry.html', context)


#搜索联系人条目
@login_required
def search(request):
    if request.POST:
        search_name = request.POST['search_name']
        entries = Entry.objects.filter(name=search_name)

    context = {'entries': entries, 'search_name': search_name}
    return render(request, 'address_books/search.html', context)


def test(request):
    list = [1, 2, 3, 4, 5]
    context = {'a': 1, 'b': 2, 'list': list}
    return render(request, 'address_books/test.html', context)
    
    
    
    
    
    
    
    
    
    
    
