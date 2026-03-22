import pickle

# Save data to pickle file
data = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
with open('person.pkl', 'wb') as file:
    pickle.dump(data, file)
print("Data saved")

# Load data from pickle file
with open('person.pkl', 'rb') as file:
    data2 = pickle.load(file)
print("Data loaded:", data2)
print("Are they equal?", data == data2)