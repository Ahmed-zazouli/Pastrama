import bs4
import sys

def verify_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = bs4.BeautifulSoup(html_content, 'html.parser')

    # Check title
    title = soup.find('title')
    assert title and "Pastrama" in title.text, "Title does not contain Pastrama"

    # Check Header
    header = soup.find('header')
    assert header is not None, "Missing <header> tag"
    h1 = header.find('h1')
    assert h1 and h1.text == "Pastrama", "Missing or incorrect <h1>"

    # Check Overview Section
    overview = soup.find(id="overview")
    assert overview is not None, "Missing section with id='overview'"
    assert "Rue Oumayma Essayeh" in overview.text, "Address not found in overview"
    assert "06 78 84 81 81" in overview.text, "Phone number not found in overview"

    # Check Menu Section
    menu = soup.find(id="menu")
    assert menu is not None, "Missing section with id='menu'"
    menu_items = ["BBQ Chicken Wings", "Virgin Mojito", "Pastrami"]
    for item in menu_items:
        assert item in menu.text, f"Menu item '{item}' not found"

    # Check Reviews Section
    reviews = soup.find(id="reviews")
    assert reviews is not None, "Missing section with id='reviews'"
    reviewers = ["H.IBTIHAL", "Nihal El", "Muhammad Abbas Khan"]
    for r in reviewers:
        assert r in reviews.text, f"Reviewer '{r}' not found"

    print("All checks passed successfully!")

if __name__ == '__main__':
    verify_html('index.html')
