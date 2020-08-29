from django.shortcuts import render
from .parsing import get_currencies, record_db
from django.views.decorators.cache import cache_page


@cache_page(60 * 60)
def currencies(request):
    record_db()
    content = get_currencies()
    last = len(content) - 26
    return render(request, 'parsing_currencies/currencies.html', {'content': content[last:]})



