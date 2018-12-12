from django.urls import path, reverse_lazy
from orders import views as my_order
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', my_order.index, name='home'),
    path('orders', my_order.index, name='home'),
    path('order/<int:order_id>/', my_order.show, name='show'),
    path('order/new/', my_order.new, name='new'),
    path('order/edit/<int:order_id>/', my_order.edit, name='edit'),
    path('order/delete/<int:order_id>/', my_order.destroy, name='delete'),
    path('users/login/', auth.LoginView.as_view(template_name='login.html'), name='login'),
    path('users/logout/', auth.LogoutView.as_view(next_page='/'),  name='logout'),
    path('users/change_password/', login_required(auth.PasswordChangeView.as_view(success_url=reverse_lazy('home'),template_name='change_password.html')), name='change_password'),
]
