from django import template
from django.conf import settings

register = template.Library()

@register.filter(name="get_lyrics")
def get_lyrics(files, index:int):
    """
    Get the lyrics of a file
    :file str:
    :return dict:
    """
    print("ICIIIIIIIIIIIIIIIIII")
    print(files)
    print(index)
    print("file", files[int(index)])
    static = settings.BASE_DIR / "nplp/static/nplp"
    file = static / files[int(index)]
    with open(file, 'r', encoding='utf-8') as file:
        content = file.read()

    lyrics = content.split('[Events]')[1]
    lyrics_lines = lyrics.split('Dialogue: ')

    lines = []
    starts = []
    end = []
    for line in lyrics_lines:
        lines.append(",".join(line.split(',')[9:]))
        starts.append(line.split(',')[1])
        end.append(line.split(',')[2])

    starts.pop(0)
    lines.pop(0)
    end.pop(0)

    answer = lines.pop()
    starts.pop()
    end.pop()

    return {
        'starts': starts,
        'end': end,
        'lines': lines,
        'answer': answer.strip().lower().split(' ')
    }