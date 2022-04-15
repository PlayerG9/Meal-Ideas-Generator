# Meal-Ideas-Generator
 website to find ideas for meals


# NOTES
file can be uploaded with json together???


# Usefull Links
https://developer.mozilla.org/de/docs/Web/HTTP/Methods

# Usefull docs
https://developer.mozilla.org/de/docs/Web/API/FormData

# Project related Q&A
https://stackoverflow.com/questions/23945494/use-html5-to-resize-an-image-before-upload
https://codeat21.com/uploading-and-resizing-images-with-react-js/

# Project related code
`headers.set('Authorization', 'Basic ' + base64.encode(username + ":" + password));`



# StackOverflow-Question


## send files and body with fetch()
how can I send files and a json body with fetch.
I know from python requests that I can make
```python
file = "a.txt"
body = json.dump(json_data)
requests.post(
    '/endpoint',
    files=[file],
    body=body
)
```
how can I archive this with javascript `fetch()`?

I searched the [Dokumentation](https://developer.mozilla.org/en-US/docs/Web/API/fetch) but I found only how to add a body
```javascript
var body = JSON.stringify(json_data)
fetch(
    '/endpoint',
    body=body
)
```
or a file
```javascript
fetch(
    '/endpoint,
    body=input.files[0]
)
```
but how can I archive both?  
or would it be better to convert the image with base64 (or so) and save it as a value in the json?
