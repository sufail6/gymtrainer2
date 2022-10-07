from django.urls import path

from app2 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('trainer_register',views.trainer_register,name='trainer_register'),
    path('trainer_view',views.trainer_view,name='trainer_view'),
    path('trainer_update/<int:id>', views.trainer_update, name='trainer_update'),
    path('trainer_delete/<int:id>',views.trainer_delete,name='trainer_delete'),
    path('user_register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_view', views.user_view, name='user_view'),
    path('equipments_add', views.equipments_add, name='equipments_add'),
    path('equipments_view', views.equipments_view, name='equipments_view'),
    path('equipments_user_view', views.equipments_user_view, name='equipments_user_view'),
    path('equipments_update/<int:id>', views.equipments_update, name='equipments_update'),
    path('equipments_delete/<int:id>', views.equipments_delete, name='equipments_delete'),
    path('bill', views.bill, name='bill'),
    path('bill_view', views.bill_view, name='bill_view'),
]
