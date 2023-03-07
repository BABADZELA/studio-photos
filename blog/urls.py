from django.urls import path
from .views import home, photo_upload, photo_and_blog_upload, view_blog, edit_blog, create_multiple_photos, follow_users
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('blog/', home, name='home'),
    path('photo/telecharger/', photo_upload, name='photo_upload'),
    path('photo/upload-multiple/', create_multiple_photos, name='create_upload_multiple'),
    path('blog/create/', photo_and_blog_upload, name='blog_post'),
    path('blog/<int:blog_id>/', view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit/', edit_blog, name='edit_blog'),
    path('follow-users/', follow_users, name='follow_users'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)