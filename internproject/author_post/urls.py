from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path
from author_post.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url



urlpatterns = [
	 url(r'^details/author/(?P<id>\w+)/$', author_details),	 url(r'^details/post/(?P<id>\w+)/$', post_details),url(r'^posts/$', view_posts)

	
	


]
