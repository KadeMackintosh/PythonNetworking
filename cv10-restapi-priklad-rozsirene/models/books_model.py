books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


def get_books_all():
    return books

def get_book_by_id(id):
    result = []
    for book in books:
        if book['id'] == id:
            result.append(book)
    print(result)
    return result

def add_book(title,author,first_sentence,year_published):
    new_book = { "id": len(books), "title": title, "author": author, "first_sentence": first_sentence, "year_published": year_published}
    books.append(new_book)
    return new_book

def delete_book_by_id(id):
    result = {}
    for i in range(len(books)):
        if books[i]['id'] == id:
            result = books[i]
            del books[i]
            break
    return result