import streamlit as st
from pages.page1 import page1_content
from pages.page2 import page2_content
from st_pages import Page, show_pages, add_page_title

add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        # Page("./pages/page1.py", "Home", "🏠"),
        Page("./pages/page2.py", "Traffic", "🚦"),
    ]
)

def main():
    # st.sidebar.title("Navigation")
    return

if __name__ == "__main__":
    main()
