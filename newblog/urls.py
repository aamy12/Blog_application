from django.conf.urls import url
from newblog import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^index/$', views.HomePageView.as_view()),
    url(r'index', views.HomePageView.as_view()),

    url(r'^register/$', views.RegisterPageView.as_view()),
    url(r'^register/', views.register),

    url(r'^logincheck', views.validate),
    url(r'^gologin', views.LoginPageView.as_view()),

    url(r'^dashboard', views.DashboardPageView.as_view()),

    url(r'^createblog', views.CreateBlogPageView.as_view()),
    url(r'^newblog', views.createBlog),

    url(r'^viewblog', views.viewBlog),
    url(r'^viewblog', views.ViewBlogPageView.as_view()),

    url(r'^reset', views.ResetPassPageView.as_view()),
    url(r'^resetpass', views.resetPassword)
 ]

