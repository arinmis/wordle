from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import Length
from rest_framework import status
from random import randrange
from .models import Word

@api_view(['GET'])
def get_word(request):
    words = Word.objects.annotate(text_len=Length('word')).filter(text_len=5)
    # no word found 
    if (len(words) == 0):
        return Response(status=status.HTTP_204_NO_CONTENT)
    word = words[randrange(len(words))].word   
    return Response({"word": word.lower()})


