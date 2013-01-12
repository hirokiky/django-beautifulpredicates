=======================
django-beautifulpredicates
=======================

Abstract
=========
Library to provide a predicate dispatch for Django's generic views.

It has PredicateProcessView.
PredicateProcessView which call method in considering of value returned by
`predicate`. The returned value is True, PredicateProcessView calles corresponding
method named `receiver`. You can set this `receiver` and `predicate` to
`dispatch_config`. Watch PonyView for usage.
