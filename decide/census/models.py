from django.db import models


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()
    register_status = models.PositiveIntegerField()

    class Meta:
        unique_together = (('voting_id', 'voter_id'),)
