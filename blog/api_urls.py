from django.urls import path, include

from blog.api_views import PostList, PostDetail

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)