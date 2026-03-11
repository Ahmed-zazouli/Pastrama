import bs4
import sys
import os

def verify_html(filepath):
    print(f"Checking {filepath}...")
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        sys.exit(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = bs4.BeautifulSoup(html_content, 'html.parser')

    # Check Title
    title = soup.find('title')
    assert title and "Dar El Kaid" in title.text, "Title does not contain 'Dar El Kaid'"

    # Check Header
    header = soup.find('header')
    assert header is not None, "Missing <header> tag"
    h1 = header.find('h1')
    assert h1 and h1.text == "Restaurant Dar El Kaid", "Missing or incorrect <h1>"

    score = header.find(class_='score')
    assert score and score.text == "4.3", "Header score should be 4.3"

    # Check Overview Section
    overview = soup.find(id="overview")
    assert overview is not None, "Missing section with id='overview'"
    overview_text = overview.text
    assert "Rue Mohamed El Alaoui" in overview_text, "Address not found"
    assert "06 62 86 19 99" in overview_text, "Phone number not found"
    assert "eat-now.io" in overview_text, "eat-now.io link text not found"
    assert "darelkaid.ma" in overview_text, "darelkaid.ma link text not found"

    # Check Menu Section
    menu = soup.find(id="menu")
    assert menu is not None, "Missing section with id='menu'"
    menu_text = menu.text
    assert "Cuscús de pollo" in menu_text, "Menu highlight 'Cuscús de pollo' not found"
    assert "Tajine de cordero" in menu_text, "Menu highlight 'Tajine de cordero' not found"

    # Check Reviews Section
    reviews = soup.find(id="reviews")
    assert reviews is not None, "Missing section with id='reviews'"
    reviews_text = reviews.text
    assert "986 reviews" in reviews_text, "Review count '986' not found"
    assert "Cuscús de pollo y tajine de cordero" in reviews_text, "Recent customer update not found in reviews"

    print("All checks passed successfully for Dar El Kaid!")

if __name__ == '__main__':
    verify_html('dar-el-kaid/index.html')