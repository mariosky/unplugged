"""unplugged URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from xyz import views
urlpatterns = [
    url(r'^admin/' , admin.site.urls),
    url(r'^$', views.gallery, name='gallery'),
    url(r'^gallery_paint/(\d*)/$', views.gallery_paint, name='gallery_paint'),
    url(r'^artist/(\d*)/$', views.artist, name='artist'),
    url(r'^masonry$', views.gallery_masonry, name='gallery_masonry'),
    url(r'^about$', views.about, name='about'),
    url(r'^kenburns', views.gallery_kenburns, name='gallery_kenburns'),
    url(r'^grid', views.gallery_grid, name='gallery_grid'),
    url(r'^index.html$', views.gallery, name='gallery'),
    url(r'^last_generation$', views.generation, name='generation'),
    url(r'^generation/(\d*)/$', views.generation, name='generation'),
    url(r'^upload.html$', views.upload, name='upload'),
    url(r'^upload_minimal', views.upload_minimal, name='upload_minimal'),
    url(r'^evoart', views.evoart, name='evoart'),
    url(r'^logout', views.logout_view, name='logout_view'),
    url(r'^update_paint', views.update_paint, name='update_paint'),
]


