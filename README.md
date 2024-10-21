# Dietary-Analysis-Tool
A dietary analysis tool that allows users to input their daily food intake and gets a breakdown of the nutrients they consume, including, calories, protein, carbohydrates and fat.  This tool could be useful for someone trying to track their diet and understand their nutrient intake.
The Python concepts used in the program are:

# Data Types: 
The program uses several data types, including strings, integers, and dictionaries. Strings are used to represent the food names and nutritional information, while integers are used to represent the amounts of each food. Dictionaries are used to store the nutritional information for each food.

# Functions:
The program defines several functions to help with the analysis. For example, there is a function to calculate the total calories, protein, carbohydrates, and fat in a user's diet, and a function to format the output as a table.
	
# Input and Output: 
The program uses Python's built-in input and print functions to get the user's input and display the results.

# Control Structures:
The program uses several control structures, including if/else statements and loops, to perform the analysis.

# Now, let's talk about the features and functions of the program. Here are some of the key features:

# Food Data Dictionary:
The food_dict dictionary serves as a simple database of foods and their nutritional information per 100 grams. Each food item is a key in the dictionary, and the value is another dictionary containing the nutritional information (calories, protein, carbs, and fat).

# User Input / Calculations: 
The get_food_data function asks the user to input the foods they ate and their weights in grams. It then calculates the total intake of calories, protein, carbs, and fat based on the nutritional information in the food_dict and the weight of the food consumed. The program prompts the user to enter the names and quantities of the foods they have eaten, and it uses this information to calculate the total nutritional intake.

# User Interaction:
The main_menu function provides a simple text-based user interface. The user can choose to enter their food intake or exit the program. If they choose to enter their food intake, the get_food_data function is called.

# Nutrient Display / Output:
The print_nutrient_info function is used to display the total nutrient information to the user in a readable format. The program displays the results in a table, with columns for the food name, amount, and nutritional information.

# Error Handling: 
If the user enters a food that is not in the food_dict, the program informs the user that the food is not in the database.

