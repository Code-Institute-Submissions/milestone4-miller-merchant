from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import BookReview, BookChoice, UserVote
from .forms import UserCommentForm
from django.db import IntegrityError

# Create your views here.

# renders landing page of the book fo the month section of the site
def review_landing(request):
    reviewlanding = BookReview.objects.all()
    return render(request, "landingbookreview.html", {"reviewlanding": reviewlanding})

# renders an individual book, this is the book of the month
def current_book_review(request):
    bookreview = BookReview.objects.all()
    return render(request, "bookreview.html", {"bookreview": bookreview})

# renders a list of the previous competition winner
def review_list(request):
    bookreview = BookReview.objects.all()
    return render(request, "reviewlist.html", {"bookreview": bookreview})

# renders an individual book review that previously won the book of the month competition
def prev_book_review(request, pk):
    bookreview = BookReview.objects.filter(pk=pk)
    return render(request, "previousreview.html", {"bookreview": bookreview})

# renders all books in bookreview and all comments in uservote votes and comments, voting allows comments made to uservote model to be counted 
# and diplayed within bookreview model
@login_required()
def view_votes(request):
    viewvote = UserVote.objects.all()
    bookchoice = BookChoice.objects.all()
    voting = BookChoice.objects.annotate(num_votes=Count('uservote'))
    return render(request, "viewvotes.html", {"voting": voting, "viewvote": viewvote, "bookchoice": bookchoice})

# renders vote page with comment form, pulls in user details and saves the form information to database
# renders all the books within bookreview for an improved UX experience
# messages confirm the whether user has voted has succesfully, error message will appear if they have
# already voted for said option
@login_required()
def book_vote(request):
    comment_form = UserCommentForm(request.POST or None)
    bookchoice = BookChoice.objects.all()
    if comment_form.is_valid():
        bookcomment = comment_form.save(commit=False)
        bookcomment.loggeduser = request.user
        try:
            bookcomment.save()
            messages.success(request, "You have voted")
        except IntegrityError:
            messages.error(request, "You have already voted this month")
    return render(request, "bookvote.html", {"comment_form": comment_form, "bookchoice": bookchoice})
