from django.urls import path
from .views import index, add_student, manage_users, view_data

urlpatterns = [
    path('', index, name='index'),
    path('add-student/', add_student, name='add_student'),
    path('manage-users/', manage_users, name='index'),
    path('view-data/', view_data, name='view_data'),
    # other URL patterns
]


