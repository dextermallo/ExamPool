"""ExamPool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import catalog.views
import users.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('index/',catalog.views.index),
    path('accounts/login/',users.views.login),
    path('accounts/register/',users.views.register),
    path('accounts/logout/', users.views.logout),
    path('admin/', admin.site.urls),
    path('accounts/info/<str:username>/', users.views.user_profile),
    path('department/', catalog.views.allDepartment),
    path('department/<str:dpName>/', catalog.views.allSubject),
    path('department/<str:dpName>/<str:sbIndex>/', catalog.views.board),
    path('department/<str:dpName>/<str:sbIndex>/<str:articleId>', catalog.views.article),
    path('department/<str:dpName>/<str:sbIndex>/edit/post', catalog.views.postArticle),
    path('department/<str:dpName>/<str:sbIndex>/<str:articleId>/deleteArticle', catalog.views.deleteArticle),
    path('department/<str:dpName>/<str:sbIndex>/<str:articleId>/<str:commentId>/deleteComment', catalog.views.deleteComment),
    path('department/<str:dpName>/<str:sbIndex>/<str:articleId>/reviseArticle', catalog.views.reviseArticle),
    path('department/<str:dpName>/<str:sbIndex>/<str:articleId>/reply', catalog.views.replyArticle),
    path('department/<str:dpName>/<str:sbIndex>/<str:articleId>/reply/<str:commentId>', catalog.views.replyComment),
    path('accounts/update_user_profile/', users.views.update_user_profile),
    path('accounts/update_user_icon/', users.views.update_user_icon),
    path('accounts/', include('django.contrib.auth.urls')),
    
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
