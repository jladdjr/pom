from django.db import models

class Day(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Project(models.Model):
    project_name = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name

class Progress(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    poms = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)

    def __str__(self):
        return "{0.poms} / {0.goal}".format(self)

    @property
    def is_complete(self):
        return poms >= goal
