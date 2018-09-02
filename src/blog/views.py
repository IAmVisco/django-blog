from django.shortcuts import render, get_list_or_404
from django.views import View


class HomeBlogView(View):
    template_name = 'blog/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
