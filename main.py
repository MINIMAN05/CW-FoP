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
            
                
        # try:
        #     price = float(input("Enter price of the book: "))
            
        except Exception as e:
            print(e)
            return
        book = {
            'id':id,
            'title':title,
            'author':author,
            'genre':genre,
            'year':year,
            'is_available': 'Yes'
            }
        books.append(book)
            
        
 
        choose_to_stop = input("Print exit, if you finished adding books. Just press Enter if you want to keep adding: ")

        if choose_to_stop == 'exit':
            break



    main_menu()

def display_books():
    print("Id", 3*' ',"Title", 3*' ',"Author", 3*' ',"Genre", 3*' ',"Year", 3*' ',"Price", 3*' ',"is_available", 3*' ')
    for i in books:
        print(i['id'], ' ',i['title'], ' ',i['author'], ' ',i['genre'],  ' ',i['year'], ' ',i['is_available'])

    # main_menu()
    
def borrow():
    display_books()
        
    try:
        borrow_id = int(input("Print ID of book that you want to borrow: "))
    except Exception as e:
        print(e)
    for i in books:
        if i['id'] == borrow_id:
            if i['is_available'] == 'Yes':
                i['is_available'] = 'No'
                print("Book has been borrowed")
            else:
                print("Book has already been borrowed")
            break
    else:
        print("Book with this ID has not been found")
            
        


def main_menu():
    while True:    
        print(30*'-', "MAIN MENU", 30*'-')
        print('1. Add books')
        print('2. Show books')
        print('3. Borrow a book')
        print('4. Exit')
        try:
            option = int(input("Enter a option (1-5) "))
        except:
            print("Invalid input")
            continue
        if option == 1:
            add_book()
        elif option == 2:
            display_books()
        elif option == 3:
            borrow()
        elif option == 4:
            break
            
            
            
            
            
main_menu()

