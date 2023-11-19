from .post import PostView
from .detail_post import PostDetailView
from .comment import CommentView
from .detail_comment import DetailCommentView
from .post_render import FormRender
from .post_patch_render import EditFormRender
from .edit_post import EditPostView
from .delete_post import DeletePost

all = (
    'PostView',
    'DetailPostView',
    'CommentView',
    'DetailCommentView',
    'FormRender',
    'EditFormRender',
    'EditPostView',
    'DeletePost',
    'PostDetailView'
)