import requests
import pprint

# params = {
#     "q": "html",
# }
#
# response = requests.get("https://api.github.com/search/repositories", params=params)
# response_json = response.json()
# pprint.pprint(response_json)
# print(f"Количество репозиториев с использованием html: {response_json['total_count']}")

# img = "https://mp.lordfilm12.ru/uploads/posts/2019-11/1573455137-373190751.jpg"
# response = requests.get(img)
# with open("img.jpg", "wb") as f:
#     f.write(response.content)


# response =requests.get("https://google.com")
# print(response.status_code)
#
# print(response.headers)
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title" : "тестовый post запроос",
    "body" : "тестовый контент post запрооса",
    "userId" : 2
}
response = requests.post(url, data=data)
print(response.status_code)
print(f"ответ - {response.json()}")