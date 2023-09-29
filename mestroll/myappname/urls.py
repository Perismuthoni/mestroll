from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.test_view, name="test_view"),
    path("hello/", views.hello, name="hello"),
    path("fetch-users/", views.fetch_users, name="fetch_users"),
    path("post_signin/", views.call_insert_class, name="call_insert_class"),
    path("post_apology/", views.call_insert_apology, name="call_insert_apology"),
    path("fetch_user_by_email/", views.fetch_user_by_email, name="fetch_user_by_email"),  
    path("testd/", views.testd, name="testd"),
]
