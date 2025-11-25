from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3