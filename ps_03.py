from bs4 import BeautifulSoup
import requests
from googletrans import Translator

# url = 'http://quotes.toscrape.com/'
# response = requests.get(url)
#
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
#
# text = soup.find_all('span', class_='text')
# author = soup.find_all('small', class_='author')
#
# for i in range(len(text)):
#     print(f"Цитата номер- {i+1}")
#     print(text[i].text)
#     print(f"Автор: {author[i].text}\n")

translator = Translator()

def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        english_words = soup.find('div', id='random_word').text.strip()
        russian_words = translator.translate(english_words, dest='ru').text

        word_definition = soup.find('div', id='random_word_definition').text.strip()
        russian_definition = translator.translate(word_definition, dest='ru').text
        return {
            "english_words": russian_words,
            "word_definition": russian_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру \"Угадай слово\"")
    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        print(f"Значение слова - {word_definition}")
        user = input("что это за слово? ")
        if user == word:
            print("Правильно")
        else:
            print(f"Неправильно, правильное слово - {word}")

        play_again = input("Хотите сыграть еще? (y/n) ")
        if play_again.lower() != "y":
            print("Спасибо за игру")
            break

word_game()