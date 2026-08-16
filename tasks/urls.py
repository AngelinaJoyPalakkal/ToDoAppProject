from django.urls import path
from . import views

urlpatterns = [

    path("", views.task_list, name="task_list"),

    path(
        "delete/<int:task_id>/",
        views.delete_task,
        name="delete_task"
    ),

    path(
        "complete/<int:task_id>/",
        views.toggle_complete,
        name="toggle_complete"
    ),

    path(
        "favorite/<int:task_id>/",
        views.toggle_favorite,
        name="toggle_favorite"
    ),

   path("add_habit/", views.add_habit, name="add_habit"),

path(
    "habit/<int:habit_id>/",
    views.toggle_habit,
    name="toggle_habit"
),

path(
    "add_mood/",
    views.add_mood,
    name="add_mood"
),
    path('delete_mood/<int:pk>/', views.delete_mood, name='delete_mood'),
    path('delete_habit/<int:pk>/', views.delete_habit, name='delete_habit'),
]