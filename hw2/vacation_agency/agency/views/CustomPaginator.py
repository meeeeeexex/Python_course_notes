from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import roman


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'results': data,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
        })

    page_query_param = 'stranitsa'
    page_size = 10
    page_size_query_param = 'page_size'

    def get_page_number(self, request, paginator):
        page_number = request.query_params.get(self.page_query_param, 1)
        if isinstance(page_number, str) and \
                any(roman_symbol in page_number for roman_symbol in 'XMLVICD'):
            page_number = roman.fromRoman(page_number)

        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number
