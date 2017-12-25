# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Category, Entry
from .forms import CategoryForm, EntryForm


import django_filters
from rest_framework import viewsets, filters
from .serializer import CategorySerializer, EntrySerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from permissions import permissions

from permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView


# Create your views here.

# #--------------------------------------------------------------------
# class CategoryList(generics.ListCreateAPIView):
#     #创建前先设置owner
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
# #--------------------------------------------------------------------
#
# #------------------------------------------------------------
# class EntryList(generics.ListCreateAPIView):
#     # authentication_classes = (BasicAuthentication,)
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     def perform_create(self, serializer):
#         category_text = self.request.data['category.text']
#         category_objs = Category.objects.filter(text=category_text)
#         #有对应的category
#         if category_objs.count() != 0:
#             serializer.save(category=category_objs[0])
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     queryset = Entry.objects.all()
#     serializer_class = EntrySerializer
# class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Entry.objects.all()
#     serializer_class = EntrySerializer
# #----------------------------------------------------------------------
#



# ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ViewSet
class EntryViewSet(viewsets.ModelViewSet):
    # 找出category对应的entry
    def perform_create(self, serializer):
        category_text = self.request.data['category.text']
        category_objs = Category.objects.filter(text=category_text)
        # 有对应的category
        if category_objs.count() != 0:
            serializer.save(category=category_objs[0])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



# ViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





from rest_framework import generics
from rest_framework import mixins
# -------------------------------------------------
class CategoryList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Category.objects.all();
    serializer_class = CategorySerializer
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = CategorySerializer(queryset, many=True)
    #     return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})

    def get(self, request, *args, **kwargs):
        # categorys = Category.objects.all()
        # serializer = CategorySerializer(categorys, many=True)
        # return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
        response = self.list(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    # def post(self, request, format=None):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        response = self.update(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    # def get_object(self, pk):
    #     try:
    #         return Category.objects.get(pk=pk)
    #     except Category.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     category = self.get_object(pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data, headers={''})
    #
    # def put(self, request, pk, format=None):
    #     category = self.get_object(pk)
    #     serializer = CategorySerializer(category, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     category = self.get_object(pk)
    #     category.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------
class EntryList(APIView):
    def get(self, request, fromat=None):
        entrys = Entry.objects.all()
        serializer = EntrySerializer(entrys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntryDetail(APIView):
    def get_object(self, pk):
        try:
            return Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        entry = self.get_object(pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#------------------------------------------------
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





#----------------------最初------------------------------------------
def check_user(user, owner):
    if user != owner:
        raise Http404

def index(request):
    return render(request, 'address_books/index.html')


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
#category_id:分组id
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
#entry_id:条目id
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
#categroy_id:要删除的条目的分组id
#category_page:当前条目所在的页数
#entry_id:条目id
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
#category_page:当前分组所在的页数
#category_id:当前分组的id
@login_required
def delete_category(request, categorys_page, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('address_books:categorys', args=[categorys_page,]))


#添加新的联系人条目
#category_id:当前分组id
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
    
    
    
    
    
    
    
    
    
    
    
