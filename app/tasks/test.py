"""
Test Tasks
"""

from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def hello(text):
    return {"status": "passed", "result": text}