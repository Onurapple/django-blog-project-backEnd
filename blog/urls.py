from django.urls import path
#from .views import post_list, post_create, post_detail, post_update, post_delete, like
from .views import BlogList, BlogRUD, BlogComment, BlogLike, BlogPostView
#app_name = 'blog'
urlpatterns = [
    path('bloglist/', BlogList.as_view()),
    path('bloglist/<int:pk>/', BlogRUD.as_view()),
    path('bloglist/<int:pk>/comment/', BlogComment.as_view()),
    path('bloglist/<int:pk>/like/', BlogLike.as_view()),
    path('bloglist/<int:pk>/blogpostview/', BlogPostView.as_view()),

    # path('', post_list, name='list'),
    # path('create/', post_create, name='create'),
    # path('<str:slug>/', post_detail, name='detail'),
    # path('<str:slug>/update/', post_update, name='update'),
    # path('<str:slug>/delete/', post_delete, name='delete'),
    # path('<str:slug>/like/', like, name='like')
]