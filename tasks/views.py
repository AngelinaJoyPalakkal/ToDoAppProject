from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import Task, Habit, Mood


def task_list(request):

    if request.method == "POST":

        title = request.POST.get("title")

        if title:
            Task.objects.create(title=title)

        return redirect("/")

    tasks = Task.objects.all()

    completed_tasks = Task.objects.filter(
        completed=True
    ).count()

    total_tasks = Task.objects.count()

    habits = Habit.objects.all()

    moods = Mood.objects.all().order_by(
        "-created_at"
    )

    context = {
        "tasks": tasks,
        "completed_tasks": completed_tasks,
        "total_tasks": total_tasks,
        "habits": habits,
        "moods": moods,
    }

    return render(
        request,
        "tasks/task_list.html",
        context
    )


# ---------------- TASKS ---------------- #

def delete_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    task.delete()

    return redirect("/")


def toggle_complete(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    task.completed = not task.completed
    task.save()

    return JsonResponse({
        "success": True,
        "completed": task.completed
    })


def toggle_favorite(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    task.favorite = not task.favorite
    task.save()

    return redirect("/")


# ---------------- HABITS ---------------- #

# ---------------- HABITS ---------------- #

def toggle_habit(request, habit_id):

    habit = get_object_or_404(
        Habit,
        id=habit_id
    )

    habit.completed = not habit.completed
    habit.save()

    return JsonResponse({
        "success": True,
        "completed": habit.completed
    })


def add_habit(request):

    if request.method == "POST":

        name = request.POST.get("name")

        if name:
            Habit.objects.create(name=name)

    return redirect("/")


def delete_habit(request, pk):

    habit = get_object_or_404(
        Habit,
        pk=pk
    )

    habit.delete()

    return redirect("/")
# ---------------- MOODS ---------------- #

def add_mood(request):

    if request.method == "POST":

        mood = request.POST.get("mood")

        if mood:

            new_mood = Mood.objects.create(
                mood=mood
            )

            return JsonResponse({
                "success": True,
                "mood": new_mood.mood,
                "id": new_mood.id,
                "created_at": new_mood.created_at.strftime(
                    "%d %b %Y %H:%M"
                )
            })

    return JsonResponse({
        "success": False
    })


def delete_mood(request, pk):

    mood = get_object_or_404(
        Mood,
        pk=pk
    )

    mood.delete()

    return redirect("/")