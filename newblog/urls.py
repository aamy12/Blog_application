from django.conf.urls import url
from newblog import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'Home', views.HomePageView.as_view()),

    url(r'^index/$', views.indexPageView.as_view()),
    url(r'index', views.indexPageView.as_view()),

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
    url(r'^passwordreset', views.resetPassword),

    url(r'^viewallblogs', views.viewallblogs),

    url(r'^blogid=(?P<pk>[0-9]+)$', views.editBlog, name='editblog'),
    url(r'^editblog', views.updateBlog),

    url(r'^postcomment', views.Comments),
    url(r'^viewid=(?P<pk>[0-9]+)$', views.vieweachBlog, name='vieweachblog'),


 ]

