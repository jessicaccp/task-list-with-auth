from django.contrib.auth.models import User
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    TextField,
)

from .enums import TaskPriority, TaskStatus


class Task(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name="tasks")

    title = CharField(max_length=100)
    description = TextField(blank=True)
    status = CharField(
        choices=TaskStatus.choices, max_length=20, default=TaskStatus.PENDING
    )
    priority = CharField(
        choices=TaskPriority.choices, max_length=20, default=TaskPriority.LOW
    )
    due_date = DateTimeField(null=True, blank=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
