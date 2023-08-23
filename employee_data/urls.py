from django.urls import path
from employee_data import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path("<int:id>/", views.employee, name='employee'),
    path('add_data/',views.add_data, name='add_data'),
]   