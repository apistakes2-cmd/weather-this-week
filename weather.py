predictions = {'monday': 'sunny','tuesday': 'rainy',
               'wednesday': 'cloudy','thursday': 'sunny',
               'friday': 'sunny','saturday': 'thunderstorms',
               'sunday': 'snowy'
}

day= input('enter day :')
if day in predictions:
    print(predictions[day])
else:
    print("Day not found.")
