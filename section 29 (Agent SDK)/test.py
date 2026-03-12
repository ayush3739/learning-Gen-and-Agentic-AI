from bs4 import BeautifulSoup
import requests,re

website="https://blogpy.vercel.app/"

response = requests.get(website)
print(response.text)

soup= BeautifulSoup(response.text, 'html.parser')
# Remove noise tags
for tag in soup(['script', 'style', 'nav', 'footer', 'head']):
    tag.decompose()

text = soup.get_text(separator=' ', strip=True)
text = re.sub(r'\s+', ' ', text).strip() # remove extra whitespace and newlines

print(f"\n--- Total chars: {len(text)} ---")