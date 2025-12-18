books = []

def add_book():
    try:
        id = int(input("Enter ID of the book: "))
    except Exception as e:
        print(e)
        return # return 
            
    try:
        title = input("Enter title of the book: ")
    except Exception as e:
        print(e)
        return
        
        
    try:
        author = input("Enter author of the book: ")
    except Exception as e:
        print(e)
        return
        
        
    try:
        genre = input("Enter genre of the book: ")
    except Exception as e:
        print(e)
        return
        
        
    try:
        year = int(input("Enter published year of the book: "))
    except Exception as e:
        print(e)
        return
        
            
    try:
        price = float(input("Enter published price of the book: "))
    except Exception as e:
        print(e)
        return
    
    try:
        choose_to_stop = input("Print exit, if you finished adding books. Just press Enter if you want to keep adding")
    except Exception as e:
        print(e)
    if choose_to_stop == 'exit':
                
    book = {
        'id':id,
        'title':title,
        'author':author,
        'genre':genre,
        'year':year,
        'price':price,
        }
    books.append(book)
    print(books)

def main_menu():
    print(30*'-', "MAIN MENU", 30*'-')
    print('1. Add a book')
    option = int(input("Enter a option that you want to "))
    while True:
        if option == 1:
            add_book()
            

main_menu()