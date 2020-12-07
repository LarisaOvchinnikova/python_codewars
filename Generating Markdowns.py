https://www.codewars.com/kata/5f656199132bf60027275739
def generate_markdowns(markdown, text, url_or_language):
    if markdown == 'link':
        return f"[{text}]({url_or_language})"
    if markdown == 'img':
        return f"![{text}]({url_or_language})"
    if markdown == 'code':
        return f"```{url_or_language}\n{text}\n```"