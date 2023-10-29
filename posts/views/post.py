from django.views import View
from posts.models import Post
from django.http import HttpResponse, JsonResponse
from django.template import loader


class PostView(View):
    @staticmethod
    def parsing_data(post:Post):
        return{'id':post.id, 'title':post.title, 'text':post.text, 'counter':post.counter}
    
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        template = loader.get_template('post/posts_list.html')
        context = {
            'posts':posts
        }
        return HttpResponse(template.render(context, request))
    
    
    def post(self, request):
        title = request.POST.get('title')
        text = request.POST.get('text')
        new_post = Post(title=title, text=text)
        new_post.save()
        return HttpResponse('Post created')
    