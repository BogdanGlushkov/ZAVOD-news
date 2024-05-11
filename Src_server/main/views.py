from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializers import NewsSerializer

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import News, Tags



def index(request, tag_slug=None):
    tags = Tags.objects.all()
    tag_selected = None

    if tag_slug:
        tag_selected = tag_slug

    return render(request, 'main/index.html', {'tags': tags, 'tag_selected': tag_selected})


def show_theme(request, theme_slug):
    theme = get_object_or_404(News, slug=theme_slug)
    theme.views += 1
    theme.save()
    tags = theme.tags.all
    print(tags)

    return render(request, 'main/theme.html', {'theme': theme, 'tags': tags})


def show_statistics(request, tag_slug=None):
    news = News.objects.all().order_by('-views')
    tags = Tags.objects.all()
    tag_selected = None

    if tag_slug:
        tag_id = tags.filter(slug=tag_slug)[0].id
        news = news.filter(tags=tag_id)
        tag_selected = tag_slug

    return render(request, 'main/statistics.html', {'news': news, 'tags': tags, 'tag_selected': tag_selected})


@api_view(['GET'])
def news_list(request, page=None, tag_slug=None):
    news = News.objects.all()
    if not page and not tag_slug:
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
    else:
        if tag_slug:
            tag_id = get_object_or_404(Tags, slug=tag_slug)
            news = news.filter(tags=tag_id)
        if page and len(news) + 1 > page:
            news = news.order_by('-id')[(page - 1) * 3:page * 3]
            serializer = NewsSerializer(news, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No more news available'}, status=status.HTTP_204_NO_CONTENT)


class news_create(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@api_view(['DELETE'])
def news_delete(request, theme_slug):
    theme = get_object_or_404(News, slug=theme_slug)
    theme.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1> Page Not Found 404 </h1>')
