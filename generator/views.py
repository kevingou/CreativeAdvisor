from django.shortcuts import render
from django.http import HttpResponse
import requests # add this line

def index(request):
    if request.method == 'POST': # if the user submits some text
        text = request.POST.get('text') # get the text from the form
        chatgpt_url = 'https://api.openai.com/v1/engines/davinci/completions' # the url of chatgpt api
        chatgpt_headers = {'Authorization': 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'} # the headers of chatgpt api, you need to replace the xxx with your own key
        chatgpt_data = {'prompt': text, 'max_tokens': 50, 'temperature': 0.9} # the data of chatgpt api, you can adjust the parameters according to your needs
        chatgpt_response = requests.post(chatgpt_url, headers=chatgpt_headers, json=chatgpt_data) # send a post request to chatgpt api and get the response
        chatgpt_result = chatgpt_response.json() # parse the response as a json object
        reply = chatgpt_result['choices'][0]['text'] # get the reply text from the json object

        midjourney_url = 'https://api.midjourney.com/v1/generate' # the url of midjourney api
        midjourney_headers = {'Authorization': 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'} # the headers of midjourney api, you need to replace the xxx with your own key
        midjourney_data = {'prompt': reply, 'size': '512x512', 'quality': 'high'} # the data of midjourney api, you can adjust the parameters according to your needs
        midjourney_response = requests.post(midjourney_url, headers=midjourney_headers, json=midjourney_data) # send a post request to midjourney api and get the response
        midjourney_result = midjourney_response.json() # parse the response as a json object
        image_url = midjourney_result['image_url'] # get the image url from the json object

        context = {'text': text, 'reply': reply, 'image_url': image_url} # create a context dictionary to pass the variables to the template
        return render(request, 'generator/index.html', context) # render the index.html template with the context

    else: # if the user visits the website for the first time
        return render(request, 'generator/index.html') # render the index.html template without any context
