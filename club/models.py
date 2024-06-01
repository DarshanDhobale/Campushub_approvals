from django.db import models
from django.contrib.auth.models import User

class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add common fields for all users here, if any

    class Meta:
        abstract = True

class ClubHead(BaseUser):
    club_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

class Authority(BaseUser):
    id_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

class Proposal(models.Model):
    organizing_club = models.ForeignKey(ClubHead, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue_requirements = models.CharField(max_length=100)
    budget_requirements = models.DecimalField(max_digits=10, decimal_places=2)
    required_resources = models.TextField()
    attachments = models.FileField(upload_to='attachments/')

class ProposalApproval(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    authority = models.ForeignKey(Authority, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
