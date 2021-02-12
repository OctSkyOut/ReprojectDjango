from django.urls import path, re_path
from blog import views

app_name = "blog"
urlpatterns = [
    # /blog/
    path("", views.PostLV.as_view(), name="index"),
    # /blog/post
    path("post/", views.PostLV.as_view(), name="post_list"),
    # /blog/post/슬러그 이름
    re_path(r"^post/(?P<slug>[-\w]+)/$", views.PostDV.as_view(), name="post_detail"),
    # /blog/archive/
    path("archive/", views.PostAV.as_view(), name="post_archive"),
    # /blog/archive/2019
    path("archive/<int:year>/", views.PostYAV.as_view(), name="post_year_archive"),
    # /blog/archive/2019/Nov
    path(
        "archive/<int:year>/<str:month>/",
        views.PostMAV.as_view(),
        name="post_month_archive",
    ),
    path(
        "archive/<int:year>/<int:month>/<str:day>",
        views.PostDAV.as_view(),
        name="post_day_archive",
    ),
    # /blog/archive/today
    path("blog/archive/today/", views.PostTAV.as_view(), name="post_today_archive"),
    # -Tag-------------------------------------------------------------------------------------------
    path("tag/", views.TagCloudTV.as_view(), name="tag_cloud"),
    path("tag/<str:tag>/", views.TaggedObjectLV.as_view(), name="tagged_object_list"),
    # -Search-------------------------------------------------------------------------------------------
    path("search/", views.SearchFormView.as_view(), name="search"),
]
