from django.contrib import admin
from django.urls import path
from posts.views import test_view, main_page_view, post_list_view, post_detail_view, post_create_view
from user.views import register_view, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('test/', test_view, name='test'),
    path('', main_page_view, name='main_page'),
    path('posts/', post_list_view, name='post_list'),
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),
    path('posts/create/', post_create_view, name='post_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
