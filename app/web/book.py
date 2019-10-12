from flask import jsonify

from helper import is_isbn_or_key
from fisher_book import FisherBook

@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
    q: 表示搜索关键字或isbn编号
    page: 表示分页信息
    '''

    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == "isbn":
        result = FisherBook.search_by_isbn(q)
    else:
        result = FisherBook.search_by_keyword(q)

    return jsonify(result)