# wordle
Django REST API that responds requested amount of words with the requested word length within the preferred language(English or Turkish.

## How to use API
```
/api/word/<string:lang>/<int:length>/<int:amount>
```

To get 5 word with length 3 with curl
```
curl -k https://3.68.135.14/api/en/word/3/5
curl -k https://3.68.135.14/api/tr/word/3/5
```
