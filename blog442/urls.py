from django.contrib import admin
from django.urls import path, include
from posts.views import main_page_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view, name='main_page'),
    path('api/vi1/posts/', include('posts.urls')),
    path('api/vi1/posts/posts2/', include('posts.urls')),
    path('api/vi1/user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

