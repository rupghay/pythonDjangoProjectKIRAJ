import csv
import json
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import UploadForm
from .models import Candle
import asyncio

class UploadCSVView(View):
    def get(self, request):
        form = UploadForm()
        return render(request, 'upload_csv.html', {'form': form})

    async def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['csv_file']
            timeframe = form.cleaned_data['timeframe']

            # Define the path to save the uploaded file in the media directory
            uploaded_file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)

            # Save the uploaded file to the media directory
            with open(uploaded_file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Check if the uploaded file has a .txt extension
            if uploaded_file.name.endswith('.txt'):
                # Rename the file with a .csv extension
                new_file_path = uploaded_file_path[:-4] + '.csv'
                os.rename(uploaded_file_path, new_file_path)
                uploaded_file_path = new_file_path

            # Now, you can read and process the uploaded CSV file from 'uploaded_file_path'
            # Convert to candles, store in JSON, and so on.

            # Example: Group data into 5-minute candles (assuming 'timeframe' is in minutes)
            grouped_candles = group_candles_by_timeframe(uploaded_file_path, timeframe)

            await asyncio.sleep(1)
            # Store the converted data in JSON or perform other processing as needed
            response_data = {'message': 'Data processed and saved as JSON file.'}
            return JsonResponse(response_data)

        return JsonResponse({'error': 'Invalid form data'})


   #asyncio.run(post())

def group_candles_by_timeframe(csv_file_path, timeframe):
    # Implement the logic to read the CSV file and group candles by the specified timeframe.
    # This will depend on the structure of your CSV data and how you want to group it.
    # You can use libraries like Pandas for efficient data manipulation.


    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        candles = [row for row in reader]
    #return candles
    # Implement the grouping logic here based on the 'timeframe' variable
    # For example, you can iterate through 'candles' and create new candles with the desired timeframe

    grouped_candles = []  # Store the grouped candles here

    return grouped_candles

def download_json(request):
    # Generate the JSON file and provide it for download
    # Set appropriate response headers
    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="candles.json"'

    # Write JSON data to the response
    # Replace this with your actual JSON generation code
    json_data = json.dumps({'example': 'data'})
    response.write(json_data)
    return response

# import csv
# import json
# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
# from django.views import View
# from .forms import UploadForm
# from .models import Candle
#
# class UploadCSVView(View):
#     def get(self, request):
#         form = UploadForm()
#         return render(request, 'upload_csv.html', {'form': form})
#
#     async def post(self, request):
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             csvfile = form.cleaned_data['csv_file']
#             timeframe = form.cleaned_data['timeframe']
#             candles = []
#
#             # Read and process the CSV file, convert to candles
#
#             # Store the converted data in JSON
#             # Create a JSON file and store it in the file system
#
#             response_data = {'message': 'Data processed and saved as JSON file.'}
#             return JsonResponse(response_data)
#
#         return JsonResponse({'error': 'Invalid form data'})
#
# def download_json(request):
#     # Generate the JSON file and provide it for download
#     # Set appropriate response headers
#     response = HttpResponse(content_type='application/json')
#     response['Content-Disposition'] = 'attachment; filename="candles.json"'
#
#     # Write JSON data to the response
#     # Replace this with your actual JSON generation code
#     json_data = json.dumps({'example': 'data'})
#     response.write(json_data)
#     return response
