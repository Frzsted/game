import random, math, time, os, json

import json

def createCharacter():
    print("--- Create Character ---")
    
    # Get user input for character details
    name = input("Enter your character's name: ")
    gender = input("Choose a gender(Male, Female, Other): ")
    
    # Create a dictionary to store character details
    character = {
        "Name": name,
        "Gender": gender,
        # Add more attributes as needed
    }
    
    print("\nCharacter created successfully!\n")
    
    # Display the created character
    print("Character Details:")
    for key, value in character.items():
        print(f"{key}: {value}")
    
    # Save character to a file (optional)
    save_character(character)

def save_character(character):
    # Save character data to a JSON file
    filename = "character_data.json"
    
    try:
        with open(filename, "w") as file:
            json.dump(character, file)
            print(f"\nCharacter data saved to {filename}")
    except Exception as e:
        print(f"\nError saving character data: {e}")

createCharacter()