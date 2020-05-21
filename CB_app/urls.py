from django.conf.urls import url
from django.urls import path
from CB_app import views

app_name = 'CB_app'

urlpatterns = [
    path('',views.customerListView.as_view(),name='customer'),
    path('<int:pk>/',views.customerDetailView.as_view(),name='detail'),
    path('create/',views.customercreateview.as_view(),name='create'),
    path('update/<int:pk>/',views.customerupdateview.as_view(),name='update'),
    path('delete/<int:pk>/',views.customerdeleteview.as_view(),name='delete'),

    path('bookmark/',views.bookmarkListView.as_view(),name='bookmark'),
    path('bookmark/<int:pk>/',views.bookmarkDetailView.as_view(),name='b_detail'),
    path('bookmark/b_create/',views.bookmarkcreateview.as_view(),name='b_create'),
    path('bookmark/b_update/<int:pk>/',views.bookmarkupdateview.as_view(),name='b_update'),
    path('bookmark/b_delete/<int:pk>/',views.bookmarkdeleteview.as_view(),name='b_delete'),

    path('query/',views.Query.as_view(),name = 'query'),


]
