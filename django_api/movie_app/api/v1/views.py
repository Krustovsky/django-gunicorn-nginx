from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView


from movies.models import Filmwork, PersonFilmwork

RoleType = PersonFilmwork.RoleType


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ["get"]  # Список методов, которые реализует обработчик
    paginate_by = 50

    def get_person_aggragation(self, RoleType: str):
        return ArrayAgg(
            "persons__full_name",
            filter=Q(personfilmwork__role=RoleType),
            distinct=True,
        )

    def get_queryset(self):
        # return Genre.objects.all().values().annotate(table = Person.objects.all().count())

        return (
            Filmwork.objects.values("id", "id", "title", "description", "creation_date", "rating", "type").annotate(
                actors=self.get_person_aggragation(RoleType.ACTOR)
            )
                .annotate(
                directors=self.get_person_aggragation(RoleType.DIRECTOR)
            ).annotate(
                writers=self.get_person_aggragation(RoleType.WRITER)
            )
                .annotate(genres=ArrayAgg("genres__name", distinct=True))
        ).order_by("id")

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)

class MoviesListApi(MoviesApiMixin, BaseListView):

    def get_context_data(self, *, object_list=None, **kwargs):

        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        context = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": page.previous_page_number() if page.has_previous() else None,
            "next": page.next_page_number() if page.has_next() else None,
            "results": list(queryset)
        }

        return context

class MoviesDetailApi(MoviesApiMixin, BaseDetailView):

    def get_context_data(self, **kwargs):
        context = list(self.get_queryset().filter(id=self.kwargs['pk']))[0]

        return context