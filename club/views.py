from django.shortcuts import render, redirect
from .forms import ProposalForm,ClubHeadLoginForm,AuthorityLoginForm

from .models import ClubHead, Authority, Proposal, ProposalApproval
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import ProposalApproval





def club_head_login(request):
    if request.method == 'POST':
        form = ClubHeadLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('create_proposal')  # Redirect to create proposal page on successful login
            else:
                # Handle invalid login credentials
                return render(request, 'club_head_login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = ClubHeadLoginForm()
    return render(request, 'club_head_login.html', {'form': form})

def authority_login(request):
    if request.method == 'POST':
        form = AuthorityLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to authority dashboard or any other page
                return redirect('authority_approvals')
            else:
                # Handle invalid login credentials
                return render(request, 'authority_login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = AuthorityLoginForm()
    return render(request, 'authority_login.html', {'form': form})

# views.py
from django.utils import timezone

def create_proposal(request):
    club_head = ClubHead.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProposalForm(request.POST, request.FILES)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.organizing_club = club_head
            proposal.date = timezone.now().date()  # Auto-capture the current date
            proposal.time = timezone.now().time()  # Auto-capture the current time
            proposal.save()
            authorities = request.POST.getlist('authorities')
            for authority_id in authorities:
                authority = Authority.objects.get(pk=authority_id)
                ProposalApproval.objects.create(proposal=proposal, authority=authority)
            return redirect('authority_approvals')
    else:
        form = ProposalForm()
    return render(request, 'create_proposal.html', {'form': form, 'club_head': club_head})


@login_required
def authority_approvals(request):
    # Get the logged-in authority
    authority = request.user.authority  # Assuming the authority is linked to the User model
    
    # Get all approvals corresponding to the authority
    approvals = ProposalApproval.objects.filter(authority=authority)
    
    return render(request, 'authority_approvals.html', {'approvals': approvals})

@login_required
def approval_detail(request, approval_id):
    # Get the approval object based on its ID
    proposal = get_object_or_404(Proposal, pk=approval_id)
    
    return render(request, 'approval_detail.html', {'proposal': proposal})