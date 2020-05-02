
from django.urls import path,re_path

from loans.views import  RegisterView, Lender_Details, Borrower_Details
from exam.views import login_page

urlpatterns = [
    path('register/',RegisterView.as_view()),
    re_path(r'^login/$', login_page),
    re_path(r'^lender/(?P<id>\d+)/$', Lender_Details),
    re_path(r'^borrower/(?P<id>\d+)/$', Borrower_Details),
]
