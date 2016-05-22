
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('post.urls')),
    url(r'^$', 'post.views.index',name='view_posts'),
    url(r'^blog/view/(?P<slug>[^\.]+)', 'post.views.view_post', name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+)', 'post.views.view_category', name='view_blog_category'),
]
