from django.shortcuts import render

from employees_app.employees.models import Employee, Department


def index(request):
    employees = [e for e in Employee.objects.order_by('department__name', 'last_name', '-first_name')]
    context = {
        'number_1': 123,
        'number_2': 321,
        'number_3': 200,
        'numbers': [123, 321, 200],
        'title': 'EmPlOyEeS LiSt',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deleniti excepturi id ipsum natus quo ut voluptate. Accusantium ad aperiam iste temporibus? Consectetur cupiditate iure molestias nisi numquam obcaecati, perferendis velit.',
        'employees': employees,
        # it's better to sort the obj params here not in the view
        'department_names': [d.name for d in Department.objects.all()],
    }
    return render(request, 'templates_examples/index.html', context)
