from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.fisher_book import FisherBook
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookView

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
        result = BookView.package_single(result, q)
    else:
        result = FisherBook.search_by_keyword(q, page)
        result = BookView.package_collection(result, q)

    return jsonify(result)