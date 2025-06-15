from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    SEMESTER = [
        ('SEM_ONE', 'Semester One'),
        ('SEM_TWO', 'Semester Two'),
        ('SEM_THREE', 'Semester Three'),
        ('SEM_FOUR', 'Semester Four'),
        ('SEM_FIVE', 'Semester Five'),
        ('SEM_SIX', 'Semester Six'),
        ('SEM_SEVEN', 'Semester Seven'),
        ('SEM_EIGHT', 'Semester Eight')
    ]
    full_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Student Full Name")
    email = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name="Student Email")
    semester = models.CharField(max_length=20, choices=SEMESTER, default='N/A', null=True, blank=True)
    phone_no = models.IntegerField(null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        ordering = ['-full_name']
    
    def __str__(self):
        return self.full_name

class Teacher(models.Model):
    DEPARTMENT = [
        ('BCA', 'Bachelor of Computer Application'),
        ('BCT', 'Bachelor of Computer Engineering'),
        ('BEI', 'Bachelor of Electronics and Information'),
        ('BCE', 'Bachelor of Civil Engineering')
    ]
    full_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Teacher Full Name")
    email = models.CharField(max_length=100, unique=True, blank=False, null=True, verbose_name="Teacher Email")
    department = models.CharField(max_length=5, choices=DEPARTMENT, default='N/A', null=True, blank=True)
    phone_no = models.IntegerField(null=False, blank=False)
    join_date = models.DateField(default='Join Date')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        ordering = ['-full_name']
    
    def __str__(self):
        return self.full_name
    
class Assignment(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Assignment Title')
    start_date = models.DateField(default='Start Date', null=False, blank=False, verbose_name='Start Date')
    end_date = models.DateField(default='End Date', blank=False, null=False, verbose_name='End Date')
    question_file = models.FileField(upload_to='assignments/questions/', null=True, blank=True, verbose_name='Select Assignment File')
    question = models.TextField(null=True, blank=True, verbose_name='Assignment Question')
    remark = models.CharField(max_length=100, null=False, blank=False, verbose_name='Assignment Details')
    full_mark = models.FloatField(blank=False, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Uploaded By')

    class Meta:
        verbose_name = 'assignment'
        verbose_name_plural = 'assignments'
        ordering = ['-title']
    
    def __str__(self):
        return self.title