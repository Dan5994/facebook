from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class FormRender(View):
    def get(self, request):
        form_created = render(request, 'post/create_post.html')
        return HttpResponse(form_created)