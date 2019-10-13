
def is_isbn_or_key(word):
    '''
    isbn13 由13位0-9数字组成， isbn10  由10位0-9数字组成，包括'-'
    '''
    isbn_or_key = "key"
    word_tmp = word.replace('-','')
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    elif len(word_tmp) == 10 and word_tmp.isdigit():
        isbn_or_key = "isbn"

    return isbn_or_key