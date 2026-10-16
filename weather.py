predictions = {'monday': 'sunny','tuesday': 'rainy',
               'wednesday': 'cloudy','thursday': 'sunny',
               'friday': 'sunny','saturday': 'thunderstorms',
               'sunday': 'snowy'
}

day= input('enter day :')
if day in predictions:
    print(predictions[day])
    print("Thank you for using the weather prediction program.")
else:
    print("Day not found.")
