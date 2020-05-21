from django.shortcuts import render
from django.urls import reverse_lazy
from CB_app import models
from CB_app.models import customer_profile,Bookmark,customer_bookmark
from django.views.generic.edit import (CreateView,DeleteView,UpdateView)
from django.views.generic import View,TemplateView,ListView,DetailView

from django.db.models import Q

import pymysql.cursors
import sqlite3
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class customerListView(ListView):
    model = customer_profile

class customerDetailView(DetailView):
    context_object_name = 'cust_dv'
    model = customer_profile
    template_name = 'CB_app/customer_detailview.html'

class customercreateview(CreateView):

    fields = ('customer_fname','customer_lname','lat','lon')
    model = customer_profile


class customerupdateview(UpdateView):
    fields = ('customer_fname','customer_lname')
    model = customer_profile

class customerdeleteview(DeleteView):
    model = customer_profile
    success_url = reverse_lazy("CB_app:customer")


class bookmarkListView(ListView):
    model = Bookmark

class bookmarkDetailView(DetailView):
    context_object_name = 'bdv'
    model = Bookmark
    template_name = 'CB_app/bookmark_detailview.html'

class bookmarkcreateview(CreateView):
    fields = ('title','url','source_name','pub_date','customer')
    model = Bookmark

class bookmarkupdateview(UpdateView):
    fields = ('title','url')
    model = Bookmark

class bookmarkdeleteview(DeleteView):
    model = Bookmark
    success_url = reverse_lazy("CB_app:bookmark")


class Query(TemplateView):
    template_name = 'CB_app/query.html'
    def get(self,request):
        query = models.customer_bookmark.objects.all().select_related('cb_customer_id').select_related('cb_bookmark_id')
        q = request.GET.get('q')
        if q != '' and q is not None:
            query = query.filter(cb_customer_id__customer_fname__icontains=q) \
                 | query.filter(cb_customer_id__customer_lname__icontains=q)  \
                 | query.filter(cb_bookmark_id__source_name__icontains=q) \
                 | query.filter(cb_customer_id__id__icontains=q) \
                 | query.filter(cb_bookmark_id__id__icontains=q)

        return render(request, self.template_name, {'query':query})
