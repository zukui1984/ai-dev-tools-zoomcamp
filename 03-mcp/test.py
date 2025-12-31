import requests

def get_web_content(url):
    jina_url = f"https://r.jina.ai/{url}"
    response = requests.get(jina_url)
    return response.text

if __name__ == "__main__":
    url = "https://github.com/alexeygrigorev/minsearch"
    content = get_web_content(url)
    print(f"Content length: {len(content)}")
