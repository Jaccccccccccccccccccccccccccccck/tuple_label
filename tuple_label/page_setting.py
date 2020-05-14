"""api json format"""
from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    """overrides default pagination"""

    page_size = 10
    page_query_param = 'page'
    page_size_query_param = "page_size"
    max_page_size = 100
