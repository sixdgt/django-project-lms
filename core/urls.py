from django.urls import path
from core.views import (
   HomePageView, 
   TeacherCreateView, 
   TeacherListView,
   TeacherDetailView, 
   TeacherDeleteView,
   TeacherUpdateView)

urlpatterns = [
   # path('', views.home, name='home') - function base views loading
   path('', HomePageView.as_view(), name='home'),
   path('teacher/list/', TeacherListView.as_view(), name='teacher.index'),
   path('teacher/create/', TeacherCreateView.as_view(), name='teacher.create'),
   path('teacher/<int:pk>/detail/', TeacherDetailView.as_view(), name='teacher.detail'),
   path('teacher/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher.edit'),
   path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher.delete')
]