from django.contrib import admin
from .models import ClubHead, Authority, Proposal, ProposalApproval

admin.site.register(ClubHead)
admin.site.register(Authority)
admin.site.register(Proposal)
admin.site.register(ProposalApproval)