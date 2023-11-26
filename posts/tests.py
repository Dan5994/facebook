from django import views
from django.test import RequestFactory, TestCase
from posts import models
from posts import views
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from .models import Post

class CreatePostTests(APITestCase):
    def test_create_post(self):
        url = reverse('get')
        data = {"title":"title1","text":"text1",
                "counter": 4, "cotegoru": "новости"}
        
        response = self.client.post(url, data, format='json')
        self.assertEqual (response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title,"title1")
        self.assertEqual(Post.objects.get().text,"text1")
        self.assertEqual(Post.objects.get().counter, 4)
        self.assertEqual(Post.objects.get().cotegoru, "новости")
        # import pdb; pdb.set_trace()
class ListPostTests(APITestCase):
    def setUp(self):
        self.posts = []
        post = models.Post(
            title = 'Первый пост',
            text = 'Первый текст',
            counter = 3,
            cotegoru = 'Новости'
        )
        post.save()
        self.posts.append(post)
        post = models.Post(
            title = 'Второй пост',
            text = 'Второй текст',
            counter = 2,
            cotegoru = 'Игры'
        )
        post.save()
        self.posts.append(post)
        self.id_2_post_map = {post.id: post for post in self.posts}

    def test_list_post(self):
        url = reverse('get') 
        response = self.client.get(url)
        self.assertEqual (response.status_code, status.HTTP_200_OK)
        for item in response.data:
            post = self.id_2_post_map[item['id']]
            self.assertEqual(item['title'], post.title)
        self.assertEqual(len(response.data), len(self.posts))
        # import pdb; pdb.set_trace() 
              