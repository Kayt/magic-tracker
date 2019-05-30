from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from django_extensions.db.models import TimeStampedModel
from werkzeug import urls


class Project(TimeStampedModel):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Ticket(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(
        Project,
        related_name="tickets",
        on_delete=models.CASCADE,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="created_tickets",
        on_delete=models.CASCADE,
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tickets",
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    ticket = models.ForeignKey(
        Ticket,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="created_comments",
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse("post_list")


    def __str__(self):
        return self.content
