from django.urls import path
from core.views import HomePageView, TeacherCreateView, TeacherListView

urlpatterns = [
   # path('', views.home, name='home') - function base views loading
   path('', HomePageView.as_view(), name='home'),
   path('teacher/list/', TeacherListView.as_view(), name='teacher.index'),
   path('teacher/create/', TeacherCreateView.as_view(), name='teacher.create')
]