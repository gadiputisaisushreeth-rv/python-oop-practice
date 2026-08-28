class Library:
    def __init__(self,book_list):
        self.book_list = list(book_list)

    def __str__(self):
        return f"Books Available{self.book_list}"
    
    def add_book(self,book_name): 
        self.book_list.append(book_name)
        return self.book_list

    def borrow_book(self,borrowed):
        if borrowed in self.book_list:
            self.book_list.remove(borrowed)
        else:
            print("Book not There")
        return self.book_list

    def return_book(self,returning):
        if returning not in self.book_list:
            self.book_list.append(returning)
            print("Thank You for returning")
        else:
            print("Book not Borrowed")
        return self.book_list

if __name__ == "__main__":
    user1 = Library([])
    print(user1)

    choice = input("Enter operation (add/borrow/return/list): ")

    if choice == "add":
        book_name = input("Enter Book Name: ")
        user1.add_book(book_name)
    elif choice == "borrow":
        borrowed = input("Enter Book Name: ")
        user1.borrow_book(borrowed)
    elif choice == "return":
        returning = input("Enter Book Name: ")
        user1.return_book(returning)

    print(f"The Book are : {user1.book_list}")