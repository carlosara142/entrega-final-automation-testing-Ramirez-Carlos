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
#crear un post
    def create_post(self, user_id, title, body):
        post_data = {
            "userId": user_id,
            "title": title,
            "body": body
        }
        return requests.post(
            f"{self.URL_BASE}/posts",
            json=post_data
        )