import json
import os

import requests


def read_data_from_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def send_post_requests(data_list, url):
    for data in data_list:
        template_name = data.pop("name", None)
        response = requests.post(url, data=data)
        print(f"response {response.text}  | Response for {data}")
        if template_name:
            print(f"original name: {template_name}")
        print("\n")


if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "tests", "test_templates.json")
    url = "http://localhost:8000/get_form"
    data_list = read_data_from_file(file_path)
    send_post_requests(data_list, url)
