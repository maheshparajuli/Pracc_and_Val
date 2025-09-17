import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
url = "https://www.example.com"  # Replace with your target URL

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Example 1: Extract the title of the page
    title = soup.title.string
    print(f"Page Title: {title}")

    # Example 2: Find all paragraph elements
    paragraphs = soup.find_all("p")
    print("\nParagraphs:")
    for p in paragraphs:
        print(p.get_text())

    # Example 3: Find an element by its ID
    # Assuming there's an element with id="my_element"
    my_element = soup.find(id="my_element")
    if my_element:
        print(f"\nContent of 'my_element': {my_element.get_text()}")
    else:
        print("\nElement with id 'my_element' not found.")

    # Example 4: Find elements by class name
    # Assuming there are elements with class="my_class"
    my_class_elements = soup.find_all(class_="my_class")
    if my_class_elements:
        print("\nElements with class 'my_class':")
        for element in my_class_elements:
            print(element.get_text())
    else:
        print("\nNo elements found with class 'my_class'.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")