import logging
import random
import requests

from const import (user_login, number_of_users, user_create_url, user_create_payload, max_posts_per_user, post_url, \
    post_create_payload, max_likes_per_user)


def user_login_with_basic_data(username, password, *args, **kwargs):
    user_login_payload = {
        "username": username,
        "password": password
    }
    user_token_request = requests.post(url=user_login, json=user_login_payload,
                                       headers={'Content-Type': 'application/json'})
    return user_token_request.json()


def generate_random_max(start_int, *args, **kwargs):
    random_integer = random.randrange(start_int)
    if random_integer == 0:
        random_integer = 1
    return random_integer


def feedback_post(post_id, access_token):
    feedback_post_url = f'http://localhost:8000/api/v1/posts/{post_id}/post_feedback/'
    feedback_post_request = requests.get(url=feedback_post_url, timeout=5,
                                         headers={'Content-Type': 'application/json',
                                                  'Authorization': f'Bearer {access_token}'})
    return feedback_post_request.json()


def create_user_and_post(*args, **kwargs):
    try:
        for number in range(number_of_users):
            user_sign_up_request = requests.post(url=user_create_url, json=user_create_payload,
                                                 headers={'Content-Type': 'application/json'})
            user_sign_up_data = user_sign_up_request.json()
            if user_sign_up_request.status_code == 201:
                user_token_data = user_login_with_basic_data(username=user_sign_up_data['username'],
                                                             password='notsafeforproduction')
                for k in range(generate_random_max(start_int=max_posts_per_user)):
                    post_detail_data = requests.post(url=post_url, json=post_create_payload,
                                                     headers={'Content-Type': 'application/json',
                                                              'Authorization': f'Bearer {user_token_data["access"]}'})
                    print({"user_sign_up_detail": user_sign_up_data, "user_token_data": user_token_data,
                           "post_detail_data": post_detail_data.json()})
                for like in range(generate_random_max(start_int=max_likes_per_user)):
                    post_get_request = requests.get(url=post_url, timeout=5,
                                                    headers={'Content-Type': 'application/json',
                                                             'Authorization': f'Bearer {user_token_data["access"]}'})
                    post_data = post_get_request.json()
                    for i in post_data:
                        feedback_post_data = feedback_post(post_id=i['id'], access_token=user_token_data["access"])
                        print({"liked_post": feedback_post_data})
        return True
    except Exception as e:
        logging.error(e, exc_info=True)


if __name__ == '__main__':
    create_user_and_post()
