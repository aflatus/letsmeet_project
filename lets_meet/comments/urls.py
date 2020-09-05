from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
    path('<event_id>/<comment_id>/detail/', views.CommentDetail.as_view(), name='comment_detail')
]