from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import Length
from rest_framework import status
from random import randrange, sample
from .models import Word

@api_view(['GET'])
def get_word(request, lang, length, amount) :
    # check language
    supported_langs = [lang[0] for lang in Word.Language.choices]
    if (not (lang in supported_langs)):
        return Response("Supported languages: {}" .format(",".join(supported_langs)), status=status.HTTP_400_BAD_REQUEST)

    words = Word.objects.annotate(text_len=Length('word')).filter(text_len=length, lang=lang)
    # no word found 
    if (len(words) == 0 or amount > len(words) ):
        return Response(status=status.HTTP_204_NO_CONTENT)
    # remove words that has space
    selected_words = map(lambda item : item.word.lower(), sample(list(words), amount))
    return Response({"words": selected_words})

