import uuid

number_of_users = 1
max_posts_per_user = 2
max_likes_per_user = 4

user_create_payload = {
    'password': 'notsafeforproduction',
    'is_active': 'true',
    'username': str(uuid.uuid4())
}
post_create_payload = {
    'title': 'Bot Created Title'
}
user_create_url = 'http://localhost:8000/api/v1/sign_up/'
user_login = 'http://localhost:8000/api/v1/token/'
post_url = 'http://localhost:8000/api/v1/posts/'
