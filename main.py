import tkinter as tk
import random
from PIL import Image, ImageTk

foods = [
    {
        "name": "Pizza",
        "img": "./images/img.jpg",
        "ingredients": ["Dough", "Tomato Sauce", "Cheese", "Pepperoni", "Bell Peppers"],
        "recipe": "1. Preheat the oven to 450°F (230°C).\n2. Roll out the pizza dough on a floured surface.\n3. Spread tomato sauce evenly on the dough.\n4. Sprinkle cheese over the sauce.\n5. Add pepperoni and bell peppers.\n6. Bake in the preheated oven for 10-15 minutes, or until crust is golden and cheese is melted."
    },
    {
        "name": "Pasta",
        "img": "./images/img_2.jpg",
        "ingredients": ["Pasta", "Tomato Sauce", "Garlic", "Basil", "Parmesan Cheese"],
        "recipe": "1. Boil pasta in salted water until al dente.\n2. In a saucepan, sauté minced garlic in olive oil.\n3. Add tomato sauce and cook until heated through.\n4. Stir in chopped basil and cooked pasta.\n5. Serve with grated Parmesan cheese on top."
    },
    {
        "name": "Burger",
        "img": "./images/img_3.jpg",
        "ingredients": ["Burger Bun", "Beef Patty", "Lettuce", "Tomato", "Onion", "Cheese", "Ketchup", "Mustard"],
        "recipe": "1. Grill the beef patty to desired doneness.\n2. Assemble the burger with lettuce, tomato, onion, and cheese on the bun.\n3. Add ketchup and mustard.\n4. Serve with fries or coleslaw."
    },
    {
        "name": "Sushi",
        "img": "./images/img_4.jpg",
        "ingredients": ["Sushi Rice", "Nori Seaweed", "Raw Fish (e.g. Salmon, Tuna)", "Cucumber", "Avocado", "Soy Sauce", "Wasabi", "Pickled Ginger"],
        "recipe": "1. Prepare sushi rice and season with rice vinegar.\n2. Lay out a sheet of nori on a bamboo mat.\n3. Spread rice evenly on the nori, leaving a border.\n4. Add thin slices of fish, cucumber, and avocado.\n5. Roll the sushi using the bamboo mat.\n6. Slice into bite-sized pieces and serve with soy sauce, wasabi, and pickled ginger."
    },
    {
        "name": "Chicken Stir-Fry",
        "img": "./images/img_5.jpg",
        "ingredients": ["Chicken Breast", "Assorted Vegetables (e.g. Bell Peppers, Broccoli, Carrots)", "Soy Sauce", "Ginger", "Garlic", "Sesame Oil", "Cornstarch", "Rice"],
        "recipe": "1. Marinate chicken in soy sauce, ginger, and garlic.\n2. Heat sesame oil in a pan and stir-fry chicken until cooked.\n3. Remove chicken from the pan.\n4. Stir-fry vegetables until tender-crisp.\n5. Add chicken back to the pan.\n6. Mix cornstarch with soy sauce and add to the pan to thicken the sauce.\n7. Serve over cooked rice."
    },
    {
        "name": "Chocolate Cake",
        "img": "./images/img_6.jpg",
        "ingredients": ["Flour", "Sugar", "Cocoa Powder", "Baking Powder", "Eggs", "Milk", "Vegetable Oil", "Vanilla Extract"],
        "recipe": "1. Preheat the oven to 350°F (175°C) and grease a cake pan.\n2. Mix dry ingredients (flour, sugar, cocoa powder, baking powder) in a bowl.\n3. Add eggs, milk, oil, and vanilla extract; mix until smooth.\n4. Pour batter into the pan and bake for 25-30 minutes.\n5. Let the cake cool before frosting or decorating."
    },
    {
        "name": "Spaghetti Carbonara",
        "img": "./images/img_7.jpg",
        "ingredients": ["Spaghetti", "Eggs", "Pancetta or Bacon", "Parmesan Cheese", "Black Pepper", "Garlic"],
        "recipe": "1. Cook spaghetti according to package instructions.\n2. In a pan, sauté pancetta or bacon until crispy.\n3. In a bowl, whisk eggs, grated Parmesan cheese, and black pepper.\n4. Drain cooked pasta and immediately toss with egg mixture.\n5. Add cooked pancetta or bacon.\n6. Serve with additional Parmesan cheese and black pepper."
    },
    {
        "name": "Fried Rice",
        "img": "./images/img_8.jpg",
        "ingredients": ["Cooked Rice", "Eggs", "Assorted Vegetables (e.g. Peas, Carrots, Corn)", "Cooked Chicken or Shrimp", "Soy Sauce", "Sesame Oil", "Green Onions"],
        "recipe": "1. Heat oil in a pan and scramble eggs.\n2. Push eggs to one side and add vegetables; stir-fry until tender.\n3. Add cooked chicken or shrimp and cooked rice.\n4. Drizzle with soy sauce and sesame oil.\n5. Stir-fry until heated through.\n6. Garnish with chopped green onions."
    },
    {
        "name": "Tacos",
        "img": "./images/img_9.jpg",
        "ingredients": ["Taco Shells", "Ground Beef", "Taco Seasoning", "Lettuce", "Tomato", "Onion", "Cheese", "Sour Cream", "Salsa"],
        "recipe": "1. Brown ground beef in a pan and drain excess fat.\n2. Add taco seasoning and water; simmer until thickened.\n3. Fill taco shells with beef mixture.\n4. Top with lettuce, tomato, onion, cheese, sour cream, and salsa.\n5. Serve with rice and beans."
    },
    {
        "name": "Chicken Noodle Soup",
        "img": "./images/img_10.jpg",
        "ingredients": ["Chicken Broth", "Cooked Chicken", "Egg Noodles", "Carrots", "Celery", "Onion", "Garlic", "Thyme"],
        "recipe": "1. Sauté chopped onion, celery, and carrots in a pot.\n2. Add minced garlic and cook briefly.\n3. Pour in chicken broth and bring to a simmer.\n4. Add cooked chicken, egg noodles, and thyme.\n5. Simmer until noodles are tender.\n6. Season with salt and pepper.\n7. Serve hot."
    },
    {
        "name": "Garden Salad",
        "img": "./images/img_11.jpg",
        "ingredients": ["Lettuce", "Tomato", "Cucumber", "Carrots", "Red Onion", "Bell Peppers", "Olives", "Feta Cheese", "Balsamic Vinaigrette"],
        "recipe": "1. Wash and chop lettuce, tomato, cucumber, carrots, red onion, and bell peppers.\n2. Toss vegetables in a bowl.\n3. Add olives and crumbled feta cheese.\n4. Drizzle with balsamic vinaigrette.\n5. Toss to coat and serve immediately."
    },
    {
        "name": "Omelette",
        "img": "./images/img_12.jpg",
        "ingredients": ["Eggs", "Milk", "Cheese", "Bell Peppers", "Onion", "Tomato", "Ham", "Salt", "Pepper"],
        "recipe": "1. Beat eggs and milk together.\n2. Heat a non-stick skillet and melt butter.\n3. Pour in beaten eggs.\n4. Add cheese, diced bell peppers, chopped onion, diced tomato, and diced ham.\n5. Season with salt and pepper.\n6. Cook until set, then fold omelette in half and serve."
    },
    {
        "name": "Fruit Smoothie",
        "img": "./images/img_13.jpg",
        "ingredients": ["Banana", "Frozen Berries", "Yogurt", "Milk", "Honey"],
        "recipe": "1. Blend banana, frozen berries, yogurt, milk, and honey.\n2. Blend until smooth and creamy.\n3. Pour into glasses and enjoy."
    },
    {
        "name": "Grilled Cheese Sandwich",
        "img": "./images/img_14.jpg",
        "ingredients": ["Bread", "Cheese", "Butter"],
        "recipe": "1. Butter one side of each bread slice.\n2. Place cheese between two slices with buttered sides facing out.\n3. Grill sandwich on a pan until bread is golden and cheese is melted.\n4. Cut and serve."
    },
    {
        "name": "Roast Chicken",
        "img": "./images/img_15.jpg",
        "ingredients": ["Whole Chicken", "Lemon", "Garlic", "Rosemary", "Olive Oil", "Salt", "Pepper"],
        "recipe": "1. Preheat oven to 425°F (220°C).\n2. Rinse and pat dry the chicken.\n3. Rub chicken with olive oil, salt, pepper, and minced garlic.\n4. Stuff cavity with lemon halves and rosemary.\n5. Roast in the oven until internal temperature reaches 165°F (74°C).\n6. Let chicken rest before carving."
    },
    {
        "name": "Mashed Potatoes",
        "img": "./images/img_16.jpg",
        "ingredients": ["Potatoes", "Butter", "Milk", "Salt", "Pepper"],
        "recipe": "1. Peel and chop potatoes.\n2. Boil potatoes until tender.\n3. Drain and mash with butter and milk.\n4. Season with salt and pepper.\n5. Serve hot."
    },
    {
        "name": "Chocolate Chip Cookies",
        "img": "./images/img_17.jpg",
        "ingredients": ["Flour", "Butter", "Brown Sugar", "White Sugar", "Egg", "Vanilla Extract", "Baking Soda", "Salt", "Chocolate Chips"],
        "recipe": "1. Preheat oven to 375°F (190°C).\n2. Cream butter, brown sugar, and white sugar.\n3. Add egg and vanilla extract; mix well.\n4. In a separate bowl, mix flour, baking soda, and salt.\n5. Gradually add dry ingredients to wet ingredients.\n6. Stir in chocolate chips.\n7. Drop spoonfuls onto baking sheets and bake for 10-12 minutes."
    },
    {
        "name": "Fried Chicken",
        "img": "./images/img_18.jpg",
        "ingredients": ["Chicken Pieces", "Buttermilk", "Flour", "Paprika", "Garlic Powder", "Salt", "Pepper", "Oil"],
        "recipe": "1. Marinate chicken pieces in buttermilk.\n2. In a bowl, mix flour, paprika, garlic powder, salt, and pepper.\n3. Dredge chicken in flour mixture.\n4. Heat oil in a pan and fry chicken until golden and cooked through.\n5. Drain on paper towels before serving."
    },

]


def generate_random_food():
    for widget in food_frame.winfo_children():
        widget.destroy()

    random_food = random.choice(foods)

    food_label = tk.Label(
        food_frame, text=random_food["name"], font=("Helvetica", 32))
    food_label.pack(pady=5)

    ingredients_text = "\n".join(random_food["ingredients"])
    ingredients_label = tk.Label(
        food_frame, text="Ingredients:", font=("Helvetica", 14))
    ingredients_label.pack()
    ingredients_text_label = tk.Label(
        food_frame, text=ingredients_text, font=("Helvetica", 12))
    ingredients_text_label.pack(pady=5)

    recipe_text = "Recipe:\n" + random_food["recipe"]
    recipe_label = tk.Label(food_frame, text=recipe_text,
                            font=("Helvetica", 12), justify="left")
    recipe_label.pack(pady=5)

    food_image_path = random_food["img"]
    pil_image = Image.open(food_image_path)
    food_image = ImageTk.PhotoImage(pil_image)
    food_image_label = tk.Label(food_frame, image=food_image)
    food_image_label.image = food_image
    food_image_label.pack(pady=5)


root = tk.Tk()
root.title("Random Food Generator")

generate_button = tk.Button(
    root, text="Generate Random Food", command=generate_random_food)
generate_button.pack(pady=5)

food_frame = tk.Frame(root)
food_frame.pack()

root.mainloop()
