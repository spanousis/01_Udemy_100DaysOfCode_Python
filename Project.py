#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

print("Welcome to the band name generator.")

city = input("In which city did you grow up?\n")

petName = input("Which is your pet's name?\n")

bandName = city + " " + petName
print(f"Your band name could be: {bandName}")