from difflib import SequenceMatcher
from datetime import datetime
from typing import Any
import requests

class ChatBot: 
    def __init__(self, name: str, responses: dict[str,str]) -> None: 
        self.name = name
        self.responses = responses

    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence: SequenceMatcher = SequenceMatcher(a = input_sentence, b = response_sentence)
        return sequence.ratio()
    
    @staticmethod
    def get_coordinates_by_ip() -> tuple[float, float]:
        response = requests.get('http://ip-api.com/json/')
        if response.status_code == 200:
            data = response.json()
            return data['lat'], data['lon']
        else:
            raise Exception("Unable to fetch location")

    @staticmethod
    def describe_weather_code(code: int) -> str:
        descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            80: "Rain showers",
            81: "Heavy rain showers",
            82: "Violent rain showers",
            95: "Thunderstorm",
            96: "Thunderstorm with hail",
            99: "Severe thunderstorm with hail"
        }
        return descriptions.get(code, "Unknown weather")
    
    def get_weather(self, coordinates: tuple[float, float]) -> str:
        url = 'https://api.open-meteo.com/v1/forecast'
        params = {
            'latitude': coordinates[0],
            'longitude': coordinates[1],
            'current_weather': True
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather = data.get("current_weather", {})
            return f'Current weather: {self.describe_weather_code(weather['weathercode'])}, temperature {weather['temperature']}'
        else:
            raise Exception(f"Failed to fetch weather. Status code: {response.status_code}")
    
    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity : float = 0.0
        best_match: str = 'Sorry, I didn\'t understand that'

        for response in self.responses:
            similarity: float = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity and similarity > 0.5:
                highest_similarity  = similarity
                best_match = self.responses[response]

        return best_match, highest_similarity
    
    def run(self) -> None:
        print(f'Hello! My name is {self.name}, how can I help you?')

        while True:
            user_input: str = input('You: ')
            response, similarity = self.get_best_response(user_input)

            if response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H:%M}'

            if response == 'GET_WEATHER':
                response = self.get_weather(self.get_coordinates_by_ip())

            print(f'{self.name}: {response} (Similarity: {similarity:.2%})')

            if response == 'Goodbye! Have a great day!':
                break

def main() -> None:
    responses: dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'what are your business hours?': 'We\'re open Monday to Friday, 9 AM to 5 PM.',
        'i am looking for a gift for my friend': 'Great, get him/her a nice shirt!',
        'i want to reset my password': 'That\'s very important, but I can\'t help you with that.',
        'i am not sure how to proceed': 'No problem, please go on.',
        'my birthday is today': 'Congratulations, happy birthday!',
        'what is the weather like today': 'GET_WEATHER',
        'bye': 'Goodbye! Have a great day!'
    }

    chatbot: ChatBot = ChatBot(name= 'Pedro', responses= responses)
    chatbot.run()

if __name__ == '__main__':
    main()