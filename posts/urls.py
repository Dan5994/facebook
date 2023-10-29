from django.urls import path
from .views import PostView, DetailPostView, CommentView, DetailCommentView, FormRender, EditFormRender, EditPostView, DeletePost
from . import view


urlpatterns = [
    path('get', PostView.as_view(), name = 'get'),
    path('create', PostView.as_view(), name = 'create'),
    path('get/<int:_id>', DetailPostView.as_view(), name='get_one_post'),
    path('delete/<int:_id>', DetailPostView.as_view(), name='delete'),
    path('update/<int:_id>', DetailPostView.as_view(), name='patch'),
    path('upgrade/<int:_id>', DetailPostView.as_view(), name='put'),
    path('comment/get', CommentView.as_view(), name = 'com_get'),
    path('comment/create', CommentView.as_view(), name = 'com_create'),
    path('comment/<int:_id>', DetailCommentView.as_view(), name='get_one_com'),
    path('comment/<int:_id>/delete', DetailCommentView.as_view(), name='delete'),
    path('comment/<int:_id>/update', DetailCommentView.as_view(), name='update'),
    path('comment/upgrade/<int:_id>', DetailCommentView.as_view(), name='upgrade'),
    path('post_com/<int:_id>', view.posts_comment),
    path('stat/<int:_id>/<status>', view.update_statu),
    path('transact/', view.update_counter),
    path('new_post', FormRender.as_view(), name='post_form'),
    path('get/edit/<int:_id>', EditPostView.as_view(), name='post_edit'),
    path('get/update/<int:_id>', EditFormRender.as_view(), name='edit_form'),
   path('get/delete/<int:_id>', DeletePost.as_view(), name='post_delete'),
] 