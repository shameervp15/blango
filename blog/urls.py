from django.urls import path
from blog.views import index, post_detail, get_ip

urlpatterns = [
  path("", index),
  path("post/<slug>/", post_detail, name="blog-post-detail"),
  path("ip/", get_ip, name="get-ip"),
  
]