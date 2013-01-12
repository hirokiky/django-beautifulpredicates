from django.test import TestCase, RequestFactory

from beautifulpredicates.predicates import RequestParamPredicate

class RequestParamPredicateTest(TestCase):
    rf = RequestFactory()

    def test_with_key(self):
        predicate =  RequestParamPredicate('ritsu')

        self.assertEqual(predicate.k, 'ritsu')
        self.assertEqual(predicate.v, None)

        request = self.rf.get('/?ritsu', REQUEST_METHOD='GET')
        self.assertEqual(predicate(request),  True)
        request = self.rf.get('/?mio', REQUEST_METHOD='GET')
        self.assertEqual(predicate(request), False)

    def test_with_key_and_value(self):
        predicate =  RequestParamPredicate('ritsu=drum')

        self.assertEqual(predicate.k, 'ritsu')
        self.assertEqual(predicate.v, 'drum')

        request = self.rf.get('/?ritsu=drum', REQUEST_METHOD='GET')
        self.assertEqual(predicate(request), True)
        request = self.rf.get('/?ritsu=bass', REQUEST_METHOD='GET')
        self.assertEqual(predicate(request), False)
        request = self.rf.get('/?ritsu', REQUEST_METHOD='GET')
        self.assertEqual(predicate(request), False)
        request = self.rf.get('/?mio=drum', REQUEST_METHOD='GET')
        self.assertEqual(predicate(request), False)
