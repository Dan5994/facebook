from rest_framework import filters
from ..models import Post


class PostFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queruset, view):
        counter = request.query_params.get('counter')
        if counter:
            return queruset.filter(counter__gte=counter)
        return queruset 
