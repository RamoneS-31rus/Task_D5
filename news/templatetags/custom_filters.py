from django import template

register = template.Library()


@register.filter(name="censor")
def censor(value):
    with open("news/templatetags/bad_words.txt", "r", encoding="UTF8") as file:
        file = file.readlines()[0].split()
    if isinstance(value, str):
        for word in file:
            value = value.replace(word, "*****")
        return str(value)
    else:
        raise ValueError(f"Нельзя применять метод censor не к строке")
