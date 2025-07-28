from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
# The `urlpatterns` list routes URLs to views.
# For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# This code defines URL patterns for the snippets app in a Django project.
# It maps the URLs to the corresponding views for listing, creating, retrieving, updating, and deleting code snippets.
# The `format_suffix_patterns` function allows the URLs to accept format suffixes like `.json` or `.api`.
# The `snippet_list` view handles requests to `/snippets/`, while the `snippet_detail` view handles requests to `/snippets/<int:pk>/`.
# This allows for a RESTful API structure where snippets can be managed through HTTP methods.
# The `urlpatterns` list routes URLs to views.
# For more information on URL routing in Django, see the Django documentation.
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/#including-other-urlconfs
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/#including-other-urlconfs
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/#including-other-urlconfs
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/#including-other-urlconfs
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/#including-other-urlconfs
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/#including-other-urlconfs
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/#including-other-urlconfs
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/#including-other-urlconfs      