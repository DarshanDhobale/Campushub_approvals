from django.urls import path
from . import views

urlpatterns = [
    path('create-proposal/', views.create_proposal, name='create_proposal'),
    path('club-head-login/', views.club_head_login, name='club_head_login'),
    path('authority-login/', views.authority_login, name='authority_login'),
    path('authority-approvals/', views.authority_approvals, name='authority_approvals'),
    path('approval-detail/<int:approval_id>/', views.approval_detail, name='approval_detail'),
]
