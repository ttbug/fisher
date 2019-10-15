import json
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.fisher_book import FisherBook
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookViewCollection

@web.route('/book/search/')
def search():
    '''
    q: 表示搜索关键字或isbn编号
    page: 表示分页信息
    '''

    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    books = BookViewCollection()

    if not form.validate():
        return jsonify(form.errors)

    q = form.q.data.strip()
    page = form.page.data

    isbn_or_key = is_isbn_or_key(q)

    fisher_book = FisherBook()
    if isbn_or_key == "isbn":
        fisher_book.search_by_isbn(q)
    else:
        fisher_book.search_by_keyword(q, page)
    
    books.fill(fisher_book, q)

    # lambda表达式把不能序列化的内容转换成字典
    return json.dumps(books, default=lambda o: o.__dict__)