def calculate_bmi(weight, height):
    """Calculate the user's BMI"""
    bmi = weight / (height ** 2)
    return bmi

def print_recommendations(bmi):
    """Print dietary recommendations based on the user's BMI"""
    if bmi < 18.5:
        print("Your BMI is below normal. Consider increasing your caloric intake and eating more protein-rich foods.")
    elif bmi >= 18.5 and bmi < 24.9:
        print("Your BMI is normal. Keep up the good work!")
    elif bmi >= 25 and bmi < 29.9:
        print("Your BMI is above normal. Consider reducing your caloric intake and eating more fruits, vegetables, and whole grains.")
    else:
        print("Your BMI is in the obese range. Consider consulting a dietitian or healthcare professional for personalized advice.")

def print_nutrient_info(calories, protein, carbs, fat):
    """Print the nutrient information for the user"""
    print(f"Calories: {calories:.2f}")
    print(f"Protein: {protein:.2f}g")
    print(f"Carbohydrates: {carbs:.2f}g")
    print(f"Fat: {fat:.2f}g")

def get_food_data(food_dict):
    """Get the nutrient information for the user's daily food intake"""
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    while True:
        food = input("Enter a food you ate today (or 'done' to finish): ").lower()
        if food == "done":
            break
        if food in food_dict:
            weight = float(input(f"How much {food} did you eat (in grams): "))
            # Calculate the nutrient information based on the weight
            food_info = food_dict[food]
            ratio = weight / 100  # Assuming the food_dict values are per 100 grams
            total_calories += food_info["calories"] * ratio
            total_protein += food_info["protein"] * ratio
            total_carbs += food_info["carbs"] * ratio
            total_fat += food_info["fat"] * ratio
        else:
            print(f"Sorry, {food} is not in our database.")

    # Print the total nutrient information
    print_nutrient_info(total_calories, total_protein, total_carbs, total_fat)

def main_menu():
    food_dict = {
        "apple": {"calories": 95, "protein": 0.5, "carbs": 25, "fat": 0.3},
        "granola bar": {"calories": 190, "protein": 3, "carbs": 33, "fat": 6},
        "chicken breast": {"calories": 284, "protein": 54, "carbs": 0, "fat": 4},
        "black beans": {"calories": 227, "protein": 15, "carbs": 41, "fat": 0.5},
        "quinoa": {"calories": 222, "protein": 8, "carbs": 40, "fat": 3.6},
        "avocado": {"calories": 234, "protein": 2.9, "carbs": 12, "fat": 21},
        "banana": {"calories": 105, "protein": 1.3, "carbs": 27, "fat": 0.4},
        "broccoli": {"calories": 55, "protein": 3.7, "carbs": 11, "fat": 0.4},
        "egg": {"calories": 72, "protein": 6, "carbs": 0.6, "fat": 5},
        "milk": {"calories": 146, "protein": 8, "carbs": 12, "fat": 8},
        "orange": {"calories": 43, "protein": 1, "carbs": 11, "fat": 0.3},
        "potato": {"calories": 163, "protein": 4, "carbs": 37, "fat": 0.2},
        "salmon": {"calories": 281, "protein": 39, "carbs": 0, "fat": 19},
        "steak": {"calories": 335, "protein": 54, "carbs": 0, "fat": 25},
        "tuna": {"calories": 179, "protein": 39, "carbs": 0, "fat": 1.3}
    }

    while True:
        print("\nDietary Analysis Tool")
        print("1. Enter food intake")
        print("2. Calculate BMI")
        print("3. Exit.")
        choice = input("Enter your choice: ")

        if choice == "1":
            get_food_data(food_dict)
        elif choice == "2":
            height = float(input("Enter your height in meters: "))
            weight = float(input("Enter your weight in kilograms: "))
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is {bmi:.2f}")
            print_recommendations(bmi)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main_menu()
