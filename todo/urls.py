from django.urls import path
from todo import views


urlpatterns = [
    path('', views.TodoManage.as_view()),
    path('edit/<int:todo_id>/', views.TodoEdit.as_view()),
]
