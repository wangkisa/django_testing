import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from catalog.models import Author


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

    def get(self, request):
        # 뷰 로직 작성
        author_list = list(Author.objects.filter().values())
        return JsonResponse(author_list, safe=False)
