

from celery import shared_task
import requests
from datetime import datetime
from .models import GeneratedImage
import environ
env = environ.Env()
environ.Env.read_env()  # Reading .env file

@shared_task
def generate_image(prompt):
    # Generate unique file name based on timestamp
    print("generating image for prompt", prompt)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    file_name = f"{timestamp}.webp"
    token=env.str("STABILITY_TOKEN") # token to authenticate Stability API
    
    # Make API request to generate image
    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/ultra",
        headers={
            "authorization": token,
            "accept": "image/*"
        },
        files={"none": ''},
        data={
        "prompt": prompt,
        "output_format": "webp",
    },
    )
    print("rimage generated for prompt: ", prompt)
    
    # Check response status and save image
    if response.status_code == 200:
        image_path=f'static/generated_images/{file_name}'

        with open(f'./{image_path}', 'wb') as file:
            file.write(response.content)
        generated_image = GeneratedImage(prompt=prompt, image_url=env.str("BASE_URL")+image_path)
        generated_image.save()
        
        return file_name
    else:
        raise Exception(f"Error {response.status_code}: {response.json()}")
