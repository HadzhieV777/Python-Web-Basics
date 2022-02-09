from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
import random

# A function is a Django view if:
# - accepts request as first param
# - returns HttpResponse

# def home(request):
#     html = f'<h1>{request.method}: This is the homepage</h1>'
#     # return HttpResponseNotFound() is the same as
#     # return HttpResponse(status=404)
#     # status code modifying is allowed
#     return HttpResponse(
#         html,
#         # status=201,
#         # context_type='text/plain',
#         # context_type='application/xml',
#         headers={
#             'x-somerandom-header': 'Django',
#         },
#     )
from django.urls import reverse_lazy

from employees_app.employees.models import Department, Employee


def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    print(reverse_lazy('department details', kwargs={
        'id': 1,
    }))

    context = {  # we can pass different values using dict
        'number': random.randint(0, 1024),
        'numbers': [random.randint(0, 1024) for _ in range(16)],
    }

    return render(request, 'index.html', context)


def go_to_home(request):
    return redirect('index')
    # return redirect('department details', id=random.randint(1, 1024))
    # return redirect(to='/')
    # return HttpResponseRedirect()


def not_found(request):
    raise Http404()
    # return HttpResponseNotFound()


def department_details(request, id):
    return HttpResponse(f'This is department {id}')


def list_departments(request):
    department = Department(  # declaring a object
        name=f'Department {random.randint(1, 1024)}'
    )
    department.save()  # we use save to send the object to the DB
    #  it's possible to use Department.objects.create to prevent using .save()

    context = {
        # we add prefetch_related to prevent n + 1 problem
        'departments': Department.objects.prefetch_related('employee_set').all(),
        # 'departments': Department.objects.filter(name__iendswith='app'),  # i means case-insensitive
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)


def create_department(request):
    return HttpResponse('Created')




'''
The N + 1 problem occurs when an application gets data from the database, 
and then loops through the result of that data. That means we call to the database again and again and again. 
In total, the application will call the database once 
for every row returned by the first query (N) plus the original query ( + 1)
'''
