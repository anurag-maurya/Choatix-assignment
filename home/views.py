from django.shortcuts import render
import environ
from django.http import JsonResponse
from .tasks import generate_image
from celery.result import AsyncResult
import json
from django.http import JsonResponse
from celery.result import AsyncResult


# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Reading .env file


def index(request):
    return render(request, 'index.html')


def generate_images(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        prompts = data.get('prompts', [])
        
        # Trigger Celery tasks
        task_ids = {}
        for i, prompt in enumerate(prompts):
            result = generate_image.delay(prompt)
            task_ids[f'task{i+1}'] = result.id
        
        return JsonResponse(task_ids)

    return JsonResponse({'error': 'Invalid request'}, status=400)



# function to get task status from Celery
def get_task_status(request):
    task_id = request.GET.get('task_id')
    result = AsyncResult(task_id)
    
    if result.state == 'PENDING':
        response = {
            'state': result.state,
            'status': 'Processing'
        }
    elif result.state == 'SUCCESS':
        response = {
            'state': result.state,
            'status': 'Done',
            'result': result.result
        }
    else:
        response = {
            'state': result.state,
            'status': result.info  
        }
    
    return JsonResponse(response)

def image_count(request):
    count = env.int('IMAGES_COUNT', default=1)
    return JsonResponse({'count': count})
