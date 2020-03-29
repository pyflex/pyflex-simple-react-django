from django.urls import path
from DjangoApi import views

urlpatterns = [
    path('api/v1/employeelist/', views.EmployeeView.as_view(), name='employeelist'),
    path('api/v1/employeelist/<int:pk>/',
         views.EmployeeSingleDetails.as_view(), name='employee_details'),
]
