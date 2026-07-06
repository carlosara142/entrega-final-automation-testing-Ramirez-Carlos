import requests

class PostApi:
    URL_BASE = "https://jsonplaceholder.typicode.com/"

#llama a todos los posts
    def get_all_posts(self):
       return requests.get(
           f"{self.URL_BASE}/posts"
        )
#llama a un post en especifico por id
    def get_one_post(self, post_id):
       return requests.get(
           f"{self.URL_BASE}/posts/{post_id}"
        )
    