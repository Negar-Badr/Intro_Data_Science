import requests
import argparse
import os
import json
from datetime import datetime
from bs4 import BeautifulSoup


def get_page_with_cache(url, cache_loc, cache_time=1800):
    if os.path.isfile(cache_loc):
        print(f"Cache found for {url}.")
        with open(cache_loc, 'r') as f:
            cached_data = json.load(f)
        
        last_cached = datetime.strptime(cached_data['last_cached'], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_cached).total_seconds() <= cache_time:
            return cached_data['html']

    print(f"Cache not found for {url}, fetching...")
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    response = requests.get(url, headers={'User-Agent': user_agent})
    
    html_content = response.text
    cached_data = {
        'last_cached': datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
        'html': html_content
    }
    
    # Save to cache
    with open(cache_loc, 'w') as f:
        json.dump(cached_data, f)
    
    return html_content


def get_cache_index(title, hashfile):
    if os.path.isfile(hashfile):
        with open(hashfile, 'r') as f:
            hashlist = json.load(f)
    else:
        hashlist = {}

    if title in hashlist:
        return hashlist[title]
    
    new_index = max(hashlist.values(), default=-1) + 1
    hashlist[title] = new_index

    # Update hash list file
    with open(hashfile, 'w') as f:
        json.dump(hashlist, f)
    
    return new_index


def scrape_article(story_url, cache_file, base_url):
    story_html = get_page_with_cache(base_url + story_url, cache_file)
    soup = BeautifulSoup(story_html, 'html.parser')

    title = soup.find("h1", class_="article-title").text.strip()
    publication_date = soup.find("span", class_="published-date__since").text.strip()
    
    author_tag = soup.find("span", class_="published-by__author")
    author = author_tag.find("a").text.strip() if author_tag else "Montreal Gazette"
    
    blurb = soup.find("p", class_="article-subtitle").text.strip()

    return {
        'title': title,
        'publication_date': publication_date,
        'author': author,
        'blurb': blurb
    }


def collect_trending_stories(output_file):
    BASE_URL = 'https://montrealgazette.com'
    homepage_html = get_page_with_cache(f"{BASE_URL}/category/news/", 'cache_files/homepage.json')
    
    soup = BeautifulSoup(homepage_html, 'html.parser')
    trending_section = soup.find('div', class_='col-xs-12 top-trending')
    
    trending_stories = trending_section.find_all('a', class_='article-card__link')
    trending_links = [story['href'] for story in trending_stories]

    articles_data = []
    for story in trending_stories:
        story_title = story['aria-label']
        cache_index = get_cache_index(story_title, 'cache_files/hash_list.json')
        
        article_info = scrape_article(story['href'], f'cache_files/{cache_index}.json', BASE_URL)
        articles_data.append(article_info)

    # Save to output JSON file
    with open(output_file, 'w') as f:
        json.dump(articles_data, f, indent=4)




def main():
    parser = argparse.ArgumentParser(description="Scrape trending stories from the Montreal Gazette.")
    parser.add_argument("-o", "--outputfile", required=True, help="Output file to save trending stories.")
    
    args = parser.parse_args()
    collect_trending_stories(args.outputfile)

if __name__ == "__main__":
    main()


