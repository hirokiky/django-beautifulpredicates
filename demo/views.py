from django.http.response import HttpResponse

from beautifulpredicates.predicates import RequestParamPredicate
from beautifulpredicates.views import PredicateProcessView


class PonyView(PredicateProcessView):
    dispatch_config = (
                          ('get_corn_1', (RequestParamPredicate('corn=1'),)),
                          ('get_corn', (RequestParamPredicate('corn'),)),
                      )
    def get_corn(self, request, *args, **kwargs):
        return HttpResponse('pony with some corn')

    def get_corn_1(self, request, *args, **kwargs):
        return HttpResponse('pony with unicorn')

    def get_default(self, request, *args, **kwargs):
        return HttpResponse('pony')
