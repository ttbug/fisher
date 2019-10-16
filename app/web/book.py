import json
from flask import jsonify, request, render_template, flash

from app.libs.helper import is_isbn_or_key
from app.spider.fisher_book import FisherBook
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookViewCollection, BookView

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

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)

        fisher_book = FisherBook()
        if isbn_or_key == "isbn":
            fisher_book.search_by_isbn(q)
        else:
            fisher_book.search_by_keyword(q, page)
        
        books.fill(fisher_book, q)
    else:
        flash("搜索的关键字不符合要求，请重新输入")

    # lambda表达式把不能序列化的内容转换成字典
    return render_template("search_result.html", books=books)


@web.route('/test')
def test():
    data = {
        'name': '',
        'age': 30,
    }

    flash("hello, adam")

    return render_template('test.html', data=data)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    fisher = FisherBook()
    fisher.search_by_isbn(isbn)
    book = BookView(fisher.first)

    return render_template('book_detail.html', book=book)