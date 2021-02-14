"""newApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from newApp.views import HomeView, UserCreateView, UserCreateDoneTV

urlpatterns = [
    path("admin/", admin.site.urls),
    # 회원가입관련 url
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", UserCreateView.as_view(), name="resgister"),
    path("account/register/done", UserCreateDoneTV.as_view(), name="resgister_done"),
    # class기반 뷰
    path("", HomeView.as_view(), name="home"),
    path("bookmark/", include("bookmark.urls")),
    path("blog/", include("blog.urls")),
    path("photo/", include("photo.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(r"^__debug__/", include(debug_toolbar.urls)),
    ]