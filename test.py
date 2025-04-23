import streamlit as st  # type: ignore
import json
import os


st.title("📚 Personal Library Manager")

# Load data with error handling
books = []
data_file = "data.json"

if os.path.exists(data_file):
    try:
        with open(data_file, "r") as f:
            books = json.load(f)
    except json.JSONDecodeError:
        st.error("⚠️ The data file is corrupted or not in JSON format.")
    except Exception as e:
        st.error("⚠️ An error occurred while loading the data: " + str(e))
else:
    st.info("No data file found. A new one will be created when you add a book.")

# Display books
st.subheader("Library Books:")
if books:
    for book in books:
        st.markdown(f"**📖 {book['title']}** by {book['author']} ({book['year']})")
else:
    st.write("No books in your library yet.")

# Add a new book
st.subheader("➕ Add a New Book")

title = st.text_input("Title")
author = st.text_input("Author")
year = st.number_input("Year", min_value=1000, max_value=2100, step=1)

if st.button("Add Book"):
    if title and author and year:
        new_book = {"title": title, "author": author, "year": int(year)}
        books.append(new_book)
        try:
            with open(data_file, "w") as f:
                json.dump(books, f, indent=4)
            st.success("✅ Book added successfully!")
            st.experimental_rerun()
        except Exception as e:
            st.error("❌ Failed to save the book: " + str(e))
    else:
        st.warning("⚠️ Please fill in all fields.")
