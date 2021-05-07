from django.db import models

class PizzaType(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Size(models.Model):
  title = models.CharField(max_length=100)

  def __str__(self):
    return self.title


class Pizza(models.Model):
  name = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
  size = models.ForeignKey(Size, on_delete=models.CASCADE)
  extra = models.CharField(max_length=100, blank=True)
