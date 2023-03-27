from django.shortcuts import render
from transformers import pipeline

def generate_text(request):
    if request.method == 'POST':
        prompt = request.POST['prompt']
        model_name = 'gpt2'  # Replace with the name of your pre-trained model
        generator = pipeline('text-generation', model=model_name)
        generated_text = generator(prompt, max_length=50, do_sample=True)[0]['generated_text']
        return render(request, 'result.html', {'generated_text': generated_text})
    else:
        return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

def index(request):
    return render(request, 'index.html')
