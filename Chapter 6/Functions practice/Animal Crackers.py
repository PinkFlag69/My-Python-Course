def animal_crackers(text):
    new_string = text.split()

    for i in range(len(new_string)-1):
        if new_string[i][0].lower() != new_string[i+1][0].lower():
            return False

    return True

result = animal_crackers("Cool Cucumber")
print(result)
