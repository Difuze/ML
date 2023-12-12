# recommendation/views.py

from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd

def predict(request):
    if request.method == 'POST':
        online_order = request.POST['online_order']
        book_table = request.POST['book_table']
        location = request.POST['location']
        city = request.POST['city']
        type1 = request.POST['type']
        votes = int(request.POST['votes'])
        cost = int(request.POST['cost'])
        rest_type_count = int(request.POST['rest_type_count'])

        # Create a DataFrame with user input
        user_input = pd.DataFrame({
            "online_order": [online_order],
            "book_table": [book_table],
            "location": [location],
            "votes": [votes],
            "cost": [cost],
            "type": [type1],
            "city": [city],
            "rest_type_count": [rest_type_count]
        })

        # Load the saved model
        with open('model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        # Make predictions using the loaded model
        prediction = model.predict(user_input)

        return render(request, 'result.html', {'prediction': prediction[0]})

    return render(request, 'input_form.html')
