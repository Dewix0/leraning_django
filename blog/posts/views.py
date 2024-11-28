from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts=[
    {
        "id":1,
        "title": 'Let\'s explore python',
        "content":'Python Is Interpreted , High Level , general purose programming language. Widely used in the fields of web development ,data science and machine learning'
    },

    {
        "id":2,
        "title": 'Django  is the best framework',
        "content":'Django is almost used by every big tech companies like google , facebook, youtube , instagram , etc'
    },

    {
         "id":3,
        "title": 'Let\'s explore Javascript',
        "content":'Javascript is Interpreted high level programming lanuguage . Widely used in web-development'

    }
]




def home(reqest):
    html= ""
    for post in posts:
        html += f'''
            <div>
                    <h1>{post['id']} - {post['title']} </h1>
                    <p> {post['content']}</p>
            </div>
'''
    return HttpResponse(html)


def post(reqest,id):
    print(type(id))
    return HttpResponse(f"{id}")