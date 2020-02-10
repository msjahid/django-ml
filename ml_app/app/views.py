from django.shortcuts import render
import pickle
import os
import numpy as np
li = ['dak_dagorik_type', 'from_office_id','from_office_unit_id','from_officer_id',
'from_officer_designation_id','to_office_id','to_office_unit_id','to_officer_id','to_officer_designation_id',
'attention_type','operation_type', 'dak_priority']

modulePath = os.path.dirname(__file__)
path = os.path.join(modulePath,'model.pkl')
with open(path, 'rb') as file:
    model = pickle.load(file)

def home_view(request):
    print(request.GET)
    return render(request, "index.html")

def predict(request):
    data = request.POST
    int_features = [int(data.get(x)) for x in li]
    # int_features = [int(data.get(x)) for x in data.get('TB_sample')]
    # int_features = [int(data.get(x)) for x in data.values()]
    # int_features = [for key, value in request.POST.items()]
    # int_features = [int(data.get(x)) for x in data.items()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction

    return render(request, 'index.html', {'prediction_text':output})

if __name__ == "__main__":
    app.run(debug=True)
