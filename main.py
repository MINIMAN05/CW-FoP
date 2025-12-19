import os
import json

books = []

def load_base():
    if not os.path.exists('library.json'):
        with open('library.json', 'w') as file:
            json.dump([], file)
    with open('library.json', 'r') as file:
        data = json.load(file)
    return data




def add_book():
    while True:
        try:
            id = int(input("Enter ID of the book: "))
        except Exception as e:
            print(e)
            return 

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
            'is_available': 'Yes'
            }
        
        data = load_base()
        
        data.append(book)
        
        with open('library.json', 'w') as file:
            json.dump(data, file, indent=4)
            
        
 
        choose_to_stop = input("Print exit, if you finished adding books. Just press Enter if you want to keep adding: ")

        if choose_to_stop == 'exit':
            break

def delete_book():
    data = display_books()
    new_data = []
    if data == []:
        print("There is no books to delete")
        return
    try:
        delete_id = int(input("Print ID of book that you want to delete: "))
    except Exception as e:
        print(e)
        
    for i in data:
        if i['id'] != delete_id:
            new_data.append(i)
    with open('library.json', 'w') as file:
        json.dump(new_data, file, indent=4)
        
            
    

def display_books():
    data = load_base()
    total = 0
    if data == []:
        print("There is no books to display")
        return
        
    print("Id", 3*' ',"Title", 3*' ',"Author", 3*' ',"Genre", 3*' ',"Year", 3*' ',"Price", 3*' ',"is_available", 3*' ')
    for i in data:
        print(i['id'], ' ',i['title'], ' ',i['author'], ' ',i['genre'],  ' ',i['year'],  ' ',i['price'], ' ',i['is_available'])
        total += i['price']
    print(f'\nTotal price of all books: ${total}')
    return data
    

    
def borrow():
    data = display_books()
    
    try:
        borrow_id = int(input("Print ID of book that you want to borrow: "))
    except Exception as e:
        print(e)
    for i in data:
        if i['id'] == borrow_id:
            if i['is_available'] == 'Yes':
                i['is_available'] = 'No'
                print("Book has been borrowed")
                
                with open('library.json', 'w') as file:
                    json.dump(data, file, indent=4)
                    
            else:
                print("Book has already been borrowed")
            break
    else:
        print("Book with this ID has not been found")
        
def return_book():
    data = display_books()
        
    try:
        return_id = int(input("Print ID of book that you want to return: "))
    except Exception as e:
        print(e)
    for i in data:
        if i['id'] == return_id:
            if i['is_available'] == 'No':
                i['is_available'] = 'Yes'
                print("Book has been returned")
                
                with open('library.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                print("Book has already been returned")
            break
    else:
        print("Book with this ID has not been found")
            

def filter():
    data = load_base()
    found = False
    genre_filter = input("Enter a category that you want filter by: ").capitalize()
    for i in data:
        if i['genre'] == genre_filter:
            print("Id", 3*' ',"Title", 3*' ',"Author", 3*' ',"Genre", 3*' ',"Year", 3*' ',"Price", 3*' ',"is_available", 3*' ')
            
            print(i['id'], ' ',i['title'], ' ',i['author'], ' ',i['genre'],  ' ',i['year'], ' ',i['is_available'])
            found = True
    if not found:
        print(f"Books that are in {genre_filter} genre were not found")
            


def main_menu():
    while True:
        print(30*'-', "MAIN MENU", 30*'-')
        print('1. Add books')
        print('2. Display books')
        print('3. Borrow a book')
        print('4. Return a book')
        print('5. Filter by genre')
        print('6. Delete a book')
        print('7. Exit')
        try:
            option = int(input("Enter a option (1-7) "))
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
            return_book()
        elif option == 5:
            filter()
        elif option == 6:
            delete_book()
        elif option == 7:
            break
            
            
            
            
            
main_menu()





# list = [{'a':1, 'c':3}, {'b':2}]
# for i in list:
#     for key,val in i.items():
#         print(key, val)