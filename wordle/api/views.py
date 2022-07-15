from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import Length
from random import randrange
from .models import Word

@api_view(['GET'])
def get_word(request):
    words = Word.objects.annotate(text_len=Length('word')).filter(text_len=5)
    # return 204
    if (len(words) == 0):
        pass
    word = words[randrange(len(words))].word   
    return Response({"word": word.lower()})


