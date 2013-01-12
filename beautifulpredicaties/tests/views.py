from django.test import TestCase, RequestFactory
from django.http import HttpResponse

from beautifulpredicaties.views import PredicateProcessView

def simple_predicate(request, dispatch_flag):
    return dispatch_flag


class SimplePredicateProcessView(PredicateProcessView):
    dispatch_config = {'get_simple': simple_predicate}

    def get_simple(self, request, *args, **kwargs):
        return HttpResponse('This is a get simple')

    def get_default(self, request, *args, **kwargs):
        return HttpResponse('This is a get default')


class PredicateProcessViewTest(TestCase):
    rf = RequestFactory()

    def test_get(self):
        request = self.rf.get('/', REQUEST_METHOD='GET')

        response = SimplePredicateProcessView.as_view()(request, True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'This is a get simple')

        response = SimplePredicateProcessView.as_view()(request, False)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'This is a get default')
