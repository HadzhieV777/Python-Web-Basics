from django.db import models
from django.urls import reverse


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True,


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )

    def get_absolute_url(self):
        return reverse('department details', kwargs={
            'id': self.id
        })

    def __str__(self):
        return self.name


class Employee(models.Model):
    # JOB TITLE
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    # COMPANY
    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    AUDI = 'AUDI'

    COMPANIES = (
        SOFT_UNI,
        GOOGLE,
        FACEBOOK,
        AUDI,
    )

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,  # null is None, not a ""
        blank=True,  # blank will handle the ""
        default='No name',
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
    )

    job_title = models.IntegerField(
        choices=(  # there is 2 values,1st is for the DB and 2nd is for django admin
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA_ENGINEER, 'QA Engineer'),
            (DEVOPS_SPECIALIST, 'DevOps Specialist'),
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )

    # one to many
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = (
            'company',
            'first_name',
        )


class User(models.Model):
    email = models.EmailField()

    # one to one
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    dead_line = models.DateField(
        null=True,
        blank=True,
    )
    employees = models.ManyToManyField(
        to=Employee
    )


# Django will handle the PascalCase and will convert it in the DB in snake_case
# and will create a table named employees_job_title

# class JobTitle(): => job_title


'''
Ints
1*2^0 + 0*2^1 + 1*2^2...
'''

'''
Floating-point
1*2^-1 + 0*2^-2 .... = 1/2 + 1/4 + 1/8 
'''
