from celery import shared_task
from assignments.models import Assignment


# Create your tasks here. This will be executed by celery.
@shared_task
def task_execute(job_params):
    assignment = Assignment.objects.get(id=job_params["db_id"])
    assignment.sum = assignment.first_term + assignment.second_term
    assignment.save()
    