from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
SUBJECT_CHOICES = [
    ('BCT001', 'Software Engineering'),
    ('BCT002', 'System Analysis and Design'),
    ('BCT003', 'Operating System'),
    ('BCT004', 'Object Oriented Programming'),
    ('BCT005', 'Electornics & Instrumentation')
]

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
    join_date = models.DateField(default=date.today, verbose_name="Join Date")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        ordering = ['-full_name']
    
    def __str__(self):
        return self.full_name
    
class Assignment(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Assignment Title')
    start_date = models.DateField(null=False, blank=False, verbose_name='Start Date')
    end_date = models.DateField(blank=False, null=False, verbose_name='End Date')
    question_file = models.FileField(upload_to='assignments/questions/', null=True, blank=True, verbose_name='Select Assignment File')
    question = models.TextField(null=True, blank=True, verbose_name='Assignment Question')
    remark = models.CharField(max_length=100, null=False, blank=False, verbose_name='Assignment Details')
    full_mark = models.FloatField(blank=False, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Uploaded By')
    assignment_subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='N/A', verbose_name='Assignment Subject')
    
    class Meta:
        verbose_name = 'assignment'
        verbose_name_plural = 'assignments'
        ordering = ['-title']
    
    def __str__(self):
        return self.title

class Material(models.Model):
    MATERIAL_CATEGORY = [
        ('SLIDE', 'Chapter Slide'),
        ('TEXT_BOOK', 'A text book'),
        ('REFERENCE_BOOK', 'A reference book'),
        ('OLD_QUESTION', 'Previous board exam question'),
        ('AUDIO_BOOK', 'An audio book')
    ]
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Material Title')
    category = models.CharField(max_length=30, choices=MATERIAL_CATEGORY, null=False, blank=False, verbose_name='Category')
    description = models.CharField(max_length=255, default='', null=False, blank=False, verbose_name='Material Description')
    material_subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='N/A', verbose_name='Material Subject')
    material_file = models.FileField(upload_to='material/', null=False, blank=False, verbose_name='Select file')
    upload_date = models.DateTimeField(default=datetime.now, verbose_name='Upload Date')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=0)

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materials'
        ordering = ['-title']
    
    def __str__(self):
        return self.title