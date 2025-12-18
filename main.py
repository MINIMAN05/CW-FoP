books = []

def add_book():
    while True:
        try:
            id = int(input("Enter ID of the book: "))
        except Exception as e:
            print(e)
            return # return 

        title = input("Enter title of the book: ")

        author = input("Enter author of the book: ").title()

        genre = input("Enter genre of the book: ").capitalize()
            
        try:
            year = int(input("Enter published year of the book: "))
            
        except Exception as e:
            print(e)
            return
            
                
        try:
            price = float(input("Enter price of the book: "))
            
        except Exception as e:
            print(e)
            return
        book = {
            'id':id,
            'title':title,
            'author':author,
            'genre':genre,
            'year':year,
            'price':price,
            }
        books.append(book)
            
        
 
        choose_to_stop = input("Print exit, if you finished adding books. Just press Enter if you want to keep adding: ")

        if choose_to_stop == 'exit':
            break



    main_menu()

def display_books():
    print("Id", 3*' ',"Title", 3*' ',"Author", 3*' ',"Genre", 3*' ',"Year", 3*' ',"Price", 3*' ')
    for i in books:
        print(i['id'], i['title'], i['author'], i['genre'], i['year'], i['price'])
        
    # print(books)
    main_menu()
    

def main_menu():
    while True:    
        print(30*'-', "MAIN MENU", 30*'-')
        print('1. Add a book')
        print('2. Show a book')
        option = int(input("Enter a option that you want to "))
        if option == 1:
            add_book()
        elif option == 2:
            display_books()
            
main_menu()

