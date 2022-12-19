from jinja2 import Template
from jinja2.filters import escape


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


data = """{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответсвующее значение{% endraw %}"""

link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

cities = [
    {"id": 1, "city": "Москва"},
    {"id": 5, "city": "Тверь"},
    {"id": 7, "city": "Минск"},
    {"id": 8, "city": "Смоленск"},
    {"id": 11, "city": "Калуга"},
]

link2 = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{ c['id'] }}">{{ c['city'] }}</option>
{% endif -%}    
{% endfor -%}   
</select>'''


name = "Vadim"
age = 28
person = Person("Vadim", 33)
tm = Template(link2)
msg = tm.render(cities=cities)

msg2 = escape(link)
print(msg)
#print(msg2)
