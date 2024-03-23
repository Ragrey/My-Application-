import streamlit as st
import pandas as pd

class LibraryManagementSystem:
    def __init__(self):
        self.books_df = pd.DataFrame(columns=['Title', 'Author', 'Genre', 'Available'])

    def add_book(self, title, author, genre):
        new_book_df = pd.DataFrame({'Title': [title], 'Author': [author], 'Genre': [genre], 'Available': [True]})
        self.books_df = pd.concat([self.books_df, new_book_df], ignore_index=True)
        st.write(f"Book '{title}' by {author} added to the library.")

    
    def remove_book(self, title):
        if title in self.books_df['Title'].values:
            self.books_df = self.books_df[self.books_df['Title'] != title]
            st.write(f"Book '{title}' removed from the library.")
        else:
            st.write(f"Book '{title}' not found in the library.")

    def borrow_book(self, title):
        if title in self.books_df['Title'].values:
            index = self.books_df[self.books_df['Title'] == title].index[0]
            if self.books_df.loc[index, 'Available']:
                self.books_df.loc[index, 'Available'] = False
                st.write(f"You have borrowed the book '{title}'.")
            else:
                st.write(f"The book '{title}' is currently not available.")
        else:
            st.write(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        if title in self.books_df['Title'].values:
            index = self.books_df[self.books_df['Title'] == title].index[0]
            if not self.books_df.loc[index, 'Available']:
                self.books_df.loc[index, 'Available'] = True
                st.write(f"You have returned the book '{title}'.")
            else:
                st.write(f"The book '{title}' is already in the library.")
        else:
            st.write(f"Book '{title}' not found in the library.")

    def display_books(self):
        st.write("Books currently available in the library:")
        st.write(self.books_df)


# Streamlit App
def main():
    st.title("Library Management System")

    library = LibraryManagementSystem()

    menu = ["Add Book", "Remove Book", "Borrow Book", "Return Book", "Display Books"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        st.subheader("Add Book")
        title = st.text_input("Title")
        author = st.text_input("Author")
        genre = st.text_input("Genre")
        if st.button("Add"):
            library.add_book(title, author, genre)

    elif choice == "Remove Book":
        st.subheader("Remove Book")
        title = st.text_input("Title")
        if st.button("Remove"):
            library.remove_book(title)

    elif choice == "Borrow Book":
        st.subheader("Borrow Book")
        title = st.text_input("Title")
        if st.button("Borrow"):
            library.borrow_book(title)

    elif choice == "Return Book":
        st.subheader("Return Book")
        title = st.text_input("Title")
        if st.button("Return"):
            library.return_book(title)

    elif choice == "Display Books":
        st.subheader("Display Books")
        library.display_books()


if __name__ == "__main__":
    main()
