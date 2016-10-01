from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="projects_owner")

    description = models.TextField(null=True, blank=True)

    PRIVATE = 0
    MEMBER = 1

    PRIVACY_TYPES = (
        (PRIVATE, "Private"),
        (MEMBER, "Project Member")
    )

    privacy_type = models.PositiveIntegerField(
        default=0, choices=PRIVACY_TYPES)

    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class Member(models.Model):
    user = models.ForeignKey(User, related_name="member")

    OWNER = 0
    MEMBER = 1

    ROLE_TYPES = (
        (OWNER, "Owner"),
        (MEMBER, "Member")
    )

    role = models.PositiveIntegerField(default=1, choices=ROLE_TYPES)


class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks')
    assignee = models.ForeignKey(Member, related_name='member_tasks')
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
