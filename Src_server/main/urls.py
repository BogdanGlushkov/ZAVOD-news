from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000/
    path('tags/<slug:tag_slug>', views.index, name='tags'),  # http://127.0.0.1:8000/tags/slug
    path('theme/<slug:theme_slug>', views.show_theme, name='theme'),  # http://127.0.0.1:8000/theme/slug
    path('statistics/', views.show_statistics, name='theme_statistics'),  # http://127.0.0.1:8000/statistics/
    path('statistics/tags/<slug:tag_slug>', views.show_statistics, name='theme_statistics_by_tags'), # http://127.0.0.1:8000/statistics/tags/slug
    path('api/news/<int:page>', views.news_list, name='news_list'),  # all - http://127.0.0.1:8000/api/news/0
    path('api/news/tags/<slug:tag_slug>/<int:page>', views.news_list, name='news_list'),  # http://127.0.0.1:8000/api/news/tags/slug/id
    path('api/show/', views.news_list, name='news_list'),  # http://127.0.0.1:8000/api/show/
    path('api/create/', views.news_create.as_view({'post': 'create'}), name='news_create'),  # http://127.0.0.1:8000/
    path('api/delete/<slug:theme_slug>/', views.news_delete, name='news_delete'),  # http://127.0.0.1:8000/
]

handler404 = views.pageNotFound
