# https://www.codewars.com/kata/5ebd53ea50d0680031190b96/train/python
def get_turkish_number(num):
    units = {
        '0': 'sıfır', '1': 'bir', '2': 'iki', '3': 'üç', '4': 'dört', '5': 'beş', '6': 'altı', '7': 'yedi', '8': 'sekiz', '9': 'dokuz' }
    tens = {
        '1': 'on', '2': 'yirmi', '3': 'otuz', '4': 'kırk', '5': 'elli', '6': 'altmış', '7': 'yetmiş', '8': 'seksen', '9': 'doksan'}
    second = num % 10
    first = num // 10
    if num < 10:
        return units[str(second)]
    elif second == 0:
        return tens[str(first)]