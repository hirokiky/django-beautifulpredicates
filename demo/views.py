from django.http.response import HttpResponse

from beautifulpredicates.predicates import RequestParamPredicate
from beautifulpredicates.views import PredicateProcessView


class PonyView(PredicateProcessView):
    dispatch_config = (
                          ('get_corn', (RequestParamPredicate('corn'),)),
                          ('get_corn_1', (RequestParamPredicate('corn=1'),)),
                      )
    def get_corn(self, request, *args, **kwargs):
        return HttpResponse('pony with some corn')

    def get_corn_1(self, request, *args, **kwargs):
        return HttpResponse('pony with unicorn')

    def get_default(self, request, *args, **kwargs):
        return HttpResponse('pony')
