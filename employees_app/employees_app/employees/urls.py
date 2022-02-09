# we make this file to avoid duplication in the main urls file
from django.urls import path

from employees_app.employees.views import department_details, list_departments, not_found,create_department

urlpatterns = (
    # we can add a required type of the ID
    # also can use urls with RegEx with re_path() instead of path()
    path('create/', create_department),
    path('<str:id>/', department_details, name='department details'),  # departments/ID =>

    path('', list_departments, name='list departments'),
    path('filter/by/order', list_departments, name='custom url'),
    path('not-found/', not_found),
)
