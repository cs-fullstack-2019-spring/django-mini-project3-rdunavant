from django.urls import path
from App.App import views
urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/name/<int:id>', views.teacher, name='name'),
    path('teachers/school/<int:id>', views.school, name='school'),
    path('teachers/subject/<int:id>', views.subject, name='subject'),
    path('teachers/hours/<int:id>', views.hours, name='hours'),
    path('teachers/dateOfWork/<int:id>', views.dateOfWork, name='dateOfWork'),
    path('teachers/dateOfEntry/<int:id>', views.dateOfEntry, name='dateOfEntry'),
]