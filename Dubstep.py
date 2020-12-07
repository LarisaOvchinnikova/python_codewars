https://www.codewars.com/kata/551dc350bf4e526099000ae5
def song_decoder(song):
    song = song.split("WUB")
    lst = [el for el in song if el !=""]
    return " ".join(lst).strip()


def song_decoder(song):
    return " ".join(song.replace("WUB", " ").split())