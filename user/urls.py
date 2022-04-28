from django.urls import path, include

from user import views

urlpatterns = [
    path('create', views.create_user, name='create'),
    path('get/<int:user_id>', views.get, name='get'),
    path('getAll', views.get_all, name='get_all'),
    path('update/<int:user_id>', views.update, name='update'),
    path('delete/<int:user_id>', views.delete_user, name='detail'),
    path('<int:user_id>/ledger/', include('ledger.urls')),
    #path('<int:user_id>/splitExpense/', include('shared_expense.urls'))
]
