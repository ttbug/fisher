
class BookView:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = ','.join(book['author'])
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.pages = book['pages'] or ''
        self.isbn = book['isbn']
        self.pages = book['pages']
        self.binding = book['binding']

    @property
    def intro(self):
        datas = filter(lambda x: True if x else False, [self.author,self.publisher,self.price])
        return '/'.join(datas)


class BookViewCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, fisher, keyword):
        self.total = fisher.total
        self.keyword = keyword
        self.books = [BookView(book) for book in fisher.books]

class _BookView:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword,
        }

        if data:
            returned["total"] = 1
            returned["books"] = [cls._cut_book_data(data)]
        
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword,
        }

        if data:
            returned["total"] = data["total"]
            returned["books"] = [cls._cut_book_data(book) for book in data["books"]]
        
        return returned

    @classmethod
    def _cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'author': ','.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image'],
            'pages': data['pages'] or '',
        }

        return book