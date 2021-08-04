from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func): # 게시글에 소유권이 필요하다.
    def decorated(request, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return  HttpResponseForbidden()
    return decorated
