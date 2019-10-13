from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.fisher_book import FisherBook
from . import web
from app.forms.book import SearchForm

@web.route('/book/search/')
def search():
    '''
    q: 表示搜索关键字或isbn编号
    page: 表示分页信息
    '''

    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)

    if not form.validate():
        return jsonify(form.errors)

    q = form.q.data.strip()
    page = form.page.data

    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == "isbn":
        result = FisherBook.search_by_isbn(q)
    else:
        result = FisherBook.search_by_keyword(q, page)

    return jsonify(result)