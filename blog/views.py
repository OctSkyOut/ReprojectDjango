from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
    DayArchiveView,
    TodayArchiveView,
    FormView,
)
from blog.forms import PostSearchForm
from blog.models import Post
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

# listView
class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts"
    paginate_by = 2


# DetailView
class PostDV(DetailView):
    model = Post


# ArchiveViews
class PostAV(ArchiveIndexView):
    model = Post
    date_field = "modify_dt"


class PostYAV(YearArchiveView):
    model = Post
    date_field = "modify_dt"
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_dt"
    month_format = "%m"


class PostDAV(DayArchiveView):
    model = Post
    date_field = "modify_dt"
    month_format = "%m"


class PostTAV(TodayArchiveView):
    model = Post
    date_field = "modify_dt"


class TagCloudTV(TemplateView):
    template_name = "taggit/taggit_cloud.html"


class TaggedObjectLV(ListView):
    model = Post
    template_name = "taggit/taggit_post_list.html"

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get("tag"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tagname"] = self.kwargs["tag"]
        return context


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = "blog/post_search.html"

    def form_valid(self, form):
        searchWord = form.cleaned_data["search_word"]
        post_list = Post.objects.filter(
            Q(title__icontains=searchWord)
            | Q(description__icontains=searchWord)
            | Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context["form"] = form
        context["search_term"] = searchWord
        context["object_list"] = post_list

        return render(self.request, self.template_name, context)
