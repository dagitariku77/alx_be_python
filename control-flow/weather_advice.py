
def get_weather():
    return input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

def provide_recommendation(weather):
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

def main():
    weather = get_weather()
    provide_recommendation(weather)

if __name__ == "__main__":
    main()