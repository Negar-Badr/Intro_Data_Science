import json
import random
import argparse

def extract_to_tsv(input_file, output_file, num_posts):
    with open(input_file, 'r') as in_file:
        data = json.load(in_file)
        posts = data['data']['children']

        num_posts = min(num_posts, len(posts))

        selected_posts = random.sample(posts, num_posts)


        with open(output_file, 'w') as out_file:
            out_file.write('Name\ttitle\tcoding\n')
            for post in selected_posts:
                name = post['data'].get('name', '')  
                title = post['data'].get('title', '').replace('\t', ' ')
                out_file.write(f'{name}\t{title}\t\n')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", required=True, help="Output TSV file")
    parser.add_argument("input", help="Input JSON file")
    parser.add_argument("num_posts", type=int, help="Number of posts to extract")
    args = parser.parse_args()
    extract_to_tsv(args.input, args.output, args.num_posts)


