from django.http.response import HttpResponse
from django.core.urlresolvers import reverse

from beautifulpredicaties.predicaties import RequestParamPredicate
from beautifulpredicaties.views import PredicateProcessView


class PonyView(PredicateProcessView):
    dispatch_config = {'get_corn': (RequestParamPredicate('corn'),),
                       'get_corn_1': (RequestParamPredicate('corn=1'),),
                      }
    def get_corn(self, request, *args, **kwargs):
        return HttpResponse('pony with some corn' + reverse('pony'))

    def get_corn_1(self, request, *args, **kwargs):
        return HttpResponse('pony with unicorn')

    def get_default(self, request, *args, **kwargs):
        return HttpResponse('pony')
