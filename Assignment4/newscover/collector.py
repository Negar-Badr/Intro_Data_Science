import argparse
import json
from newscover.newsapi import fetch_latest_news

def collect_news(api_key, input_file, output_dir, lookback_days=10):
    # Read the input file containing keywords
    with open(input_file, 'r') as f:
        keyword_sets = json.load(f)
    
    for name, keywords in keyword_sets.items():
        articles = fetch_latest_news(api_key, keywords, lookback_days)
        # Save the articles to the output directory
        with open(f"{output_dir}/{name}.json", 'w') as out_file:
            json.dump(articles, out_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='News Collection Tool')
    parser.add_argument('-k', '--api_key', required=True, help='News API key')
    parser.add_argument('-i', '--input_file', required=True, help='Input JSON file with keywords')
    parser.add_argument('-o', '--output_dir', required=True, help='Output directory to save news results')
    parser.add_argument('-b', '--lookback_days', type=int, default=10, help='Number of days to look back')
    
    args = parser.parse_args()
    collect_news(args.api_key, args.input_file, args.output_dir, args.lookback_days)
