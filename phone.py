import requests
from bs4 import BeautifulSoup
import re

# Regex pattern to match phone numbers that are not formatted as ###-###-####
phone_pattern = re.compile(r'\b(?!(\d{3}-\d{3}-\d{4})\b)(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})\b')

# Function to find phone numbers in the text
def find_phone_numbers(text):
    return phone_pattern.findall(text)

# Function to grab the visible text content from the URLs
def scrape_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        # Get only the visible text
        visible_text = soup.get_text(separator=' ')
        return visible_text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ''

# Read URLs from a file
def read_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
        # Remove any extra whitespace characters, such as newlines
        urls = [url.strip() for url in urls]
        return urls
    except Exception as e:
        print(f"Error reading URL file: {e}")
        return []

# Main function to process URLs
def main():
    # Path to the file containing URLs
    url_file_path = 'urls.txt'
    urls = read_urls_from_file(url_file_path)
    
    # Loop through the urls in the urls.txt file
    for url in urls:
        text_content = scrape_url(url)
        if text_content:
            phone_numbers = find_phone_numbers(text_content)
            for number_tuple in phone_numbers:
                number = number_tuple[1]  # Extract the actual phone number part from the match
                print(f"Found incorrect formated phone number on {url}: {number}")

if __name__ == "__main__":
    main()
