from django.urls import path, re_path
from blog import views

app_name = "blog"
urlpatterns = [
    # /blog/
    path("", views.PostLV.as_view(), name="index"),
    # /blog/post
    path("post/", views.PostLV.as_view(), name="post_list"),
    # /blog/post/슬러그 이름
    re_path(r"^(?P<slug>[-\w]+)/$", views.PostDv.as_view(), name="post_detail"),
    # /blog/archaive/
    path("archaive/", views.PostAV.as_view(), name="post_archaive"),
    # /blog/archaive/2019
    path("archaive/<int:year>/", views.PostYAV.as_view(), name="post_year_archaive"),
    # /blog/archaive/2019/Nov
    path(
        "archaive/<int:year>/<str:month>/",
        views.PostMAV.as_view(),
        name="post_month_archaive",
    ),
    # /blog/archaive/today
    path("blog/archaive/today/", views.PostTAV.as_view(), name="post_today_archaive"),
]
