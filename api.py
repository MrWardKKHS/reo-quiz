from bs4 import BeautifulSoup
from pydantic.main import BaseModel
import requests
from random import choice, shuffle
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from random import choice, shuffle
from functools import cache
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "file:///C:/Users/award/dev/reo-quiz/public/index.html",
    'null', 
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Word(BaseModel):
    maori: str
    english: str
    breakdown: str

class Question(BaseModel):
    correct: Word
    all_questions: list[Word]

@cache
def load_questions():
    url = "https://nzhistory.govt.nz/culture/maori-language-week/1000-maori-place-names"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    word_dict = {}
    rows = soup.find_all('tr')
    for i, row in enumerate(rows):
        maori, breakdown, english = row.contents
        word_dict[i] = Word(
            maori=maori.text, 
            english=english.text, 
            breakdown=breakdown.text.replace('; ', "\n")
        )
    return word_dict

def make_question():
    words = load_questions()
    ans = choice(words)
    all_questions = []
    while len(all_questions) < 3:
        random_word = choice(words)
        if random_word != ans:
            all_questions.append(random_word)
    all_questions.append(ans)
    shuffle(all_questions)
    question = Question(correct=ans, all_questions=all_questions)
    return question

def make_round(num:int = 10):
    round = []
    for i in range(num):
        round.append(make_question())
    return round


@app.get("/")
def get_item():
    return make_round()
