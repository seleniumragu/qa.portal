from django.db import models
from django.urls import reverse

# Create your models here.


class Automation(models.Model):
    gitrepo = models.CharField(max_length=100)
    gitbranch = models.CharField(max_length=100)
    env = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    processes = models.CharField(max_length=100)
    googlechaturl = models.CharField(max_length=100)
    reportpath = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Automation")
        verbose_name_plural = ("Automations")
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    # This method name: 'get_absolute_url()' is reserved in django
    # def get_absolute_url(self):
    #     return reverse("automation_app:edit", kwargs={"automation_id": self.pk})

    def get_absolute_url_edit(self):
        return reverse("automation_app:edit", kwargs={"automation_id": self.pk})

    def get_absolute_url_delete(self):
        return reverse("automation_app:delete", kwargs={"automation_id": self.pk})
