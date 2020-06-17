import json
import urllib.request

from collections import Counter
from pprint import pprint

comments_url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/comments')
posts_url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts')

comments = json.loads(comments_url.read())
posts = json.loads(posts_url.read())

counter_comments = Counter(comment['postId'] for comment in comments)

with_comments = [{'id': post['id'], 'title': post['title'], 'body': post['body'], 'total_comments': counter_comments[post['id']]} for post in posts]

print(with_comments)

