import requests

class PostApi:
    URL_BASE = "https://jsonplaceholder.typicode.com/"

    def get_post(self, post_id):
       return requests.get(
           f"{self.URL_BASE}/posts/{post_id}")
    