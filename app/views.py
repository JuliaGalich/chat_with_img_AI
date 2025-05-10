from django.shortcuts import render
from .forms import PromptForm
from project.settings import API_KEY

import openai
#openai.api_key = ''
client = openai.OpenAI(api_key=API_KEY)

def home(request):
    response_text = None
    response_image = None

    if request.method == 'POST':
        form = PromptForm(request.POST)

        want_text = 'text_response' in request.POST
        want_image = 'image_response' in request.POST

        # is_valid
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            want_text = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = want_image.choices[0].message.content

            if want_image:
                image_result = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="512x512",
                    response_format="url"
                )
            response_image = image_result.data[0].url

            #model "gpt-image-1"
            # image_result = client.images.generate(
            #     model="gpt-image-1",
            #     prompt=prompt
            # )
            #
            # image_base64 = image_result.data[0].b64_json
            # response_image = image_base64.b64decode(image_base64)

            # Save the image to a file
            with open("otter.png", "wb") as f:
                f.write(response_image)

    else:
        form = PromptForm()

    return render(request, 'home.html', {
        'form': form,
        'response_text':response_text,
        'response_image': response_image
    })