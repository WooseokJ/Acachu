from __future__ import absolute_import, unicode_literals
from celery import shared_task
from app.components.celery_tasks import visitors

@shared_task
def add(x + y):
    return x + y


@shared_task
def ga_collect():
    visitors()