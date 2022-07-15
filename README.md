# wordle
Django REST API that responds requested amount of words with the requested amount.

## How to use API
```
/api/word/<int:length>/<int:amount>
```

To get 5 word with length 3 with curl
```
curl -k https://3.68.135.14/api/word/3/5
```
