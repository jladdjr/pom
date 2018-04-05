from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    registered = models.DateTimeField()

class WorkDay(models.Model):
    date = models.DateField()
    started = models.BooleanField()
    stopped = models.BooleanField()
    start_time = models.TimeField()
    stop_time = models.TimeField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "Date: " + start_time.strftime("%Y-%m-%d")

class Priority(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return str(rank) + " - " + name

class Task(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField(default=0)
    original_pomodoro_goal = models.IntegerField(default=0)
    current_pomodoro_goal = models.IntegerField(default=0)
    pomodoros_completed = models.IntegerField(default=0)
    priority = models.ForeignKey(Priority)
    day = models.ForeignKey(WorkDay)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return str(current) + " slots (Goal: " + str(goal) + ")"

class Pomodoro(models.Model):
    completed = models.BooleanField
    date = models.DateTimeField()
    pomodoro_set = models.ForeignKey(PomodoroSet)

    def __unicode__(str):
        if completed:
            return "Completed (" + date.strftime("%Y-%m-%d %H:%M:%S") + ")"
        return "Not completed"

