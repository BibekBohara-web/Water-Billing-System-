from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('signup', views.signup, name="signup"),

    path('indexD', views.indexD, name="indexD"),

    # profile

    path('profile', views.profile, name="profile"),

    # home button

    path('home', views.home, name="home"),

    # view client, supplier

    # path('view_client', views.view_client, name="view_client"),

    # path('view_supplier', views.view_supplier, name="view_supplier"),    

    # dashboard company and client

    path('companyD', views.companyD, name="companyD"),

    # clients

    path('client', views.client, name='client'),

    path('addClient', views.addClient, name='addClient'),

    # path('details', views.details, name='details'),

    path('add', views.add, name="add"),

    path('edit_item/<int:id>', views.edit_item, name="edit_item"),

    path('delete_item/<int:id>', views.delete_item, name="delete_item"),

    path('update_item/<int:id>', views.update_item, name="update_item"),

    # Suppliers

    path('suppliers', views.suppliers, name="suppliers"),

    path('addSuppliers', views.addSuppliers, name="addSuppliers"),

    path('cadd', views.cadd, name="cadd"),

     path('cedit_item/<int:cid>', views.cedit_item, name="cedit_item"),

    path('cdelete_item/<int:cid>', views.cdelete_item, name="cdelete_item"),

    path('cupdate_item/<int:cid>', views.cupdate_item, name="cupdate_item"),

    # Billing and History

    path('bh',views.bh, name="bh" ),

  # Log Out
  path('logout', views.logout, name="logout"),

    # path('signin', views.signin, name="signin"),
    # path('signout', views.signout, name="signout"),
]
