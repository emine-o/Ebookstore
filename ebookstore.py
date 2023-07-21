import sqlite3
import string

db = sqlite3.connect("ebookstore")
cursor = db.cursor()

#Create a table called "book".
cursor.execute("""CREATE TABLE book
               (id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)""")
db.commit

#Store the details of the books in variables.
id_1 = 3001
title_1 = "A Tale of Two Cities"
author_1 = "Charles Dickens"
qty_1 = 30

id_2 = 3002
title_2 = "Harry Potter and the Philosopher's Stone"
author_2 = "J.K. Rowling"
qty_2 = 40

id_3 = 3003
title_3 = "The Lion, the Witch and the Wardrobe"
author_3 = "C. S. Lewis"
qty_3 = 25

id_4 = 3004
title_4 = "The Lord of the Rings"
author_4 = "J.R.R Tolkien"
qty_4 = 37

id_5 = 3005
title_5 = "Alice in Wonderland"
author_5 = "Lewis Carroll"
qty_5 = 12

id_6 = 3006
title_6 = "Oliver Twist"
author_6 = "Charles Dickens"
qty_6 = 23

# Create a list consisting of book details.
# Capitalize each word of the titles and authors to get standart looking for each text.
books = [(id_1, string.capwords(title_1).strip(), string.capwords(author_1).strip(), qty_1),
         (id_2, string.capwords(title_2).strip(), string.capwords(author_2).strip(), qty_2),
         (id_3, string.capwords(title_3).strip(), string.capwords(author_3).strip(), qty_3),
         (id_4, string.capwords(title_4).strip(), string.capwords(author_4).strip(), qty_4),
         (id_5, string.capwords(title_5).strip(), string.capwords(author_5).strip(), qty_5),
         (id_6, string.capwords(title_6).strip(), string.capwords(author_6).strip(), qty_6)]

# Insert book details into table "book".
cursor.executemany("""INSERT INTO book VALUES(?, ?, ?, ?)""", books)
db.commit

while True:

    # Create a list of ID numbers of all the books registered.
    cursor.execute("""SELECT id FROM book""")
    all_book_id = cursor.fetchall()
    id_list = []
    for row in all_book_id:
        temp = "{0}".format(row[0])
        id_list.append(int(temp))
    
    # Create a list of titles of all the books registered.
    cursor.execute("""SELECT title FROM book""")
    all_book_title = cursor.fetchall()
    title_list = []
    for row in all_book_title:
        temp = "{0}".format(row[0])
        title_list.append(temp)

    # Create a list of authors of all the books registered.
    cursor.execute("""SELECT author FROM book""")
    all_book_author = cursor.fetchall()
    author_list = []
    for row in all_book_author:
        temp = "{0}".format(row[0])
        author_list.append(temp)

    menu = input('''
Select one of the following options:
1. Enter book
2. Update book
3. Delete book
4. Search book
5. List all books
0. Exit
''')
    
    # Execute if user choice is "Enter book".
    if menu == "1":

        valid_option = False
        while valid_option == False:

            try:
                # Store the ID user entered in variable.
                book_id = int(input("Enter the ID number of the book: "))

                # Check if the ID user entered exists in the table.
                if book_id not in id_list:
                    valid_option = True
                # Make user enter an ID that does not exist in the table.
                else:
                    print("\nThis ID number already exists. Try again.\n")

            # Make user enter an integer number.
            except ValueError:
                print("\nInvalid input! Please enter an integer number.\n")

        # Store the title user entered in variable.        
        book_title = input("Enter the title of the book: ")
        # Make sure the title look proper form of text.
        book_title = string.capwords(book_title).strip()

        # Store the author user entered in variable.        
        book_author = input("Enter the author of the book: ")
        # Make sure the author look proper form of text.
        book_author = string.capwords(book_author).strip()

        valid_option = False
        while valid_option == False:

            try:
                # Store the quantity user entered in variable.        
                book_qty = int(input("Enter the quantity of the book: "))
                # Go on if user enters an integer number.
                valid_option = True

            # Make user enter an integer number.
            except ValueError:
                print("\nInvalid input! Please enter an integer number.\n")
        
        # Store all book details in variable.
        book = [book_id, book_title, book_author, book_qty]

        # Insert book details into table.
        cursor.execute("""INSERT INTO book VALUES (?, ?, ?, ?)""", book)
        db.commit

        # Inform user what happened.
        print(f'''
The book has been added as below:
ID: {book_id}
Title: {book_title}
Author: {book_author}
Quantity: {book_qty}
''')

    # Execute if user choice is "Update book".
    elif menu == "2":        

        valid_option = False
        while valid_option == False:

            try:
                # Store the ID user entered in variable.
                book_id = int(input("Enter the ID number of the book you want to update: "))
                
                # Check if the ID user entered exists in the table.
                if book_id in id_list:
                    valid_option = True
                # Make user enter an ID that exists in the table.
                else:
                    print("\nThe ID number could not be found. Try again.\n")

            # Make user enter an integer number.
            except ValueError:
                print("\nInvalid input! Please enter an integer number.\n")
        
        # Select title corresponding the ID user entered.
        cursor.execute("""SELECT title FROM book WHERE id = ?""", (book_id,))
        for row in cursor.fetchone():
            book_title = "{0}".format(row)

        # Select author corresponding the ID user entered.
        cursor.execute("""SELECT author FROM book WHERE id = ?""", (book_id,))
        for row in cursor.fetchone():
            book_author = "{0}".format(row)

        # Select quantity corresponding the ID user entered.
        cursor.execute("""SELECT qty FROM book WHERE id = ?""", (book_id,))
        for row in cursor.fetchone():
            book_qty = "{0}".format(row)

        db.commit()

        updated_book_id = book_id
        updated_book_title = book_title
        updated_book_author = book_author
        updated_book_qty = book_qty

        menu_option = True
        while menu_option == True:
            
            # Present the current details of the book user would like to update.
            update_menu = input(f'''
    Select the index you would like to update:
    1. ID: {updated_book_id}
    2. Title: {updated_book_title}
    3. Author: {updated_book_author}
    4. Quantity: {updated_book_qty}  
    5. Back to main menu
    ''')

            # Execute if user wants to update ID number.
            if update_menu == "1":
                valid_option = False
                while valid_option == False:

                    try:
                        # Store the ID user entered in variable.
                        updated_book_id = int(input("Enter the new ID number: "))

                        # Check if the ID user entered exists in the table.
                        if updated_book_id not in id_list:
                            valid_option = True
                        # Make user enter an ID that does not exist in the table.
                        else:
                            print("\nThis ID number already exists. Try again.\n")

                    # Make user enter an integer number.
                    except ValueError:
                        print("\nInvalid input! Please enter an integer number.\n")

                    # Update ID in table.
                    cursor.execute("""UPDATE book SET id = ? WHERE id = ?""", (updated_book_id, book_id))
                    db.commit()

                    # Inform user what happened.
                    print("\nThe ID has been updated as '{0}'.\n".format(updated_book_id))

            # Execute if user wants to update title.
            elif update_menu == "2":
                # Store the title user entered in variable.
                updated_book_title = input("Enter the new title: ")
                # Update title in table.
                cursor.execute("""UPDATE book SET title = ? WHERE id = ?""", (updated_book_title, updated_book_id))
                db.commit()

                # Inform user what happened.
                print("\nThe title has been updated as '{0}'.\n".format(updated_book_title))

            # Execute if user would wants to update author.
            elif update_menu == "3":
                # Store the author user entered in variable.
                updated_book_author = input("Enter the new author: ")
                # Update author in table.
                cursor.execute("""UPDATE book SET author = ? WHERE id = ?""", (updated_book_author, updated_book_id))
                db.commit()

                # Inform user what happened.
                print("\nThe author has been updated as '{0}'.\n".format(updated_book_author))

            # Execute if user wants to update quantity.
            elif update_menu == "4":
                valid_option = False
                while valid_option == False:

                    try:
                        # Store the quantity user entered in variable.
                        updated_book_qty = int(input("Enter the quantity of the book: "))
                        valid_option = True

                    # Make user enter an integer number.
                    except ValueError:
                        print("\nInvalid input! Please enter an integer number.\n")

                # Update quantity in table.
                cursor.execute("""UPDATE book SET qty = ? WHERE id = ?""", (updated_book_qty, updated_book_id))
                db.commit()

                # Inform user what happened.
                print("\nThe quantity has been updated as '{0}'.\n".format(updated_book_qty))
            
            # Execute if user want to go back to main menu.
            elif update_menu == "5":
                menu_option = False

            # Make user enter a valid input.
            else:
                print("\nInvalid input! Please enter the index number of an option.\n")
            
            print()

    # Execute if user choice is "Delete book".
    elif menu == "3":
        valid_option = False
        while valid_option == False:

            try:
                # Store the ID user entered in variable.
                book_id = int(input("Enter the ID number of the book you want to delete: "))
                
                # Check if the ID user entered exists in the table.
                if book_id in id_list:
                    valid_option = True
                # Make user enter an ID that exists in the table.
                else:
                    print("\nThe ID number could not be found. Try again.\n")

            # Make user enter an integer number.
            except ValueError:
                print("\nInvalid input! Please try again.\n")

        # Delete book from table.
        cursor.execute("""DELETE FROM book WHERE id = ?""", (book_id,))
        db.commit

        # Inform user what happened.
        print(f"\nThe book with ID number '{book_id}' has been deleted.")

    # Execute if user choice is "Search book".
    elif menu == "4":
        menu_option = True
        while menu_option == True:

            search_menu = input('''
    Search a book using one of the options below:
    1. ID
    2. Title
    3. Author
    4. Back to main menu
    ''')

            # Execute if user wants to search with ID.
            if search_menu == "1":
                valid_option = False
                while valid_option == False:

                    try:
                        # Store the ID user entered in variable.
                        search_book_id = int(input("Enter the ID number: "))

                        # Check if the ID user entered exists in the table.
                        if search_book_id in id_list:
                            # Go on if the ID exists in table
                            valid_option = True
                        # Make user enter an ID that exists in the table.
                        else:
                            print("\nThe ID number could not be found. Try again.\n")

                    # Make user enter an integer number.
                    except ValueError:
                        print("\nInvalid input! Please enter an integer number.\n")

                # Create a list to store corresponding books with ID that user entered.
                search_book_list = []
                # Select corresponding books with ID that user entered, and add them into the list.
                cursor.execute("""SELECT * FROM book WHERE id = ?""", (search_book_id,))
                for row in cursor.fetchone():
                    search_book = "{0}".format(row)
                    search_book_list.append(search_book)
                db.commit
                
                # Print the result of search.
                print(f'''
ID: {search_book_list[0]}
Title: {search_book_list[1]}
Author: {search_book_list[2]}
Quantity: {search_book_list[3]}
''')

            # Execute if user wants to search with title.
            elif search_menu == "2":
                valid_option = False
                while valid_option == False:

                    # Store the title user entered in variable.
                    search_book_title = input("Enter the title: ")
                    # Make sure the format of the text that user entered matches the text in table.
                    search_book_title = string.capwords(search_book_title).strip()

                    # Check if the title user entered exists in the table.
                    if search_book_title in title_list:
                        # Go on if the title exists in table
                        valid_option = True
                    # Make user enter a title that exists in the table.
                    else:
                        print("\nThe title could not be found. Try again.\n")

                # Select corresponding books with title that user entered.
                cursor.execute("""SELECT * FROM book WHERE title = ?""", (search_book_title,))
                for row in cursor.fetchall():
                    # Print the result of search.
                    print('''
ID: {0}
Title: {1}
Author: {2}
Quantity: {3}'''.format(row[0], row[1], row[2], row[3]))
                    
                db.commit()

            elif search_menu == "3":
                valid_option = False
                while valid_option == False:

                    # Store the author user entered in variable.
                    search_book_author = input("Enter the author: ")
                    # Make sure the format of the text that user entered matches the text in table.
                    search_book_author = string.capwords(search_book_author).strip()

                    # Check if the author user entered exists in the table.
                    if search_book_author in author_list:
                        # Go on if the author exists in table
                        valid_option = True
                    # Make user enter a author that exists in the table.
                    else:
                        print("\nThe author could not be found. Try again.\n")

                # Select corresponding books with author that user entered.
                cursor.execute("""SELECT * FROM book WHERE author = ?""", (search_book_author,))
                for row in cursor.fetchall():
                    # Print the result of search.
                    print('''
ID: {0}
Title: {1}
Author: {2}
Quantity: {3}'''.format(row[0], row[1], row[2], row[3]))

                db.commit()
            
            # Execute if the user wants to go back to main menu.
            else:
                menu_option = False
    
    # Execute if user choice is "List all books".
    elif menu == "5":
        cursor.execute("""SELECT * FROM book""")
        for row in cursor.fetchall():
            print('''
ID: {0}
Title: {1}
Author: {2}
Quantity: {3}'''.format(row[0], row[1], row[2], row[3]))

        db.commit()

    # Execute if user choice is "Exit".
    elif menu == "0":
        print("Goodbye")
        exit()
    
    # Make user enter a valid input.
    else:
        print("\nInvalid input! Please enter the index number of an option.\n")
