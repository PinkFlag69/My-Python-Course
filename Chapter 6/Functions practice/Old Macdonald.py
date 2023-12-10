'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald

Note: 'macdonald'.capitalize() returns 'Macdonald'
'''

def old_macdonald(text):
    # Capitalize the first and fourth letters
    new_text = text[0].capitalize() + text[1:3] + text[3].capitalize() + text[4:]
    return new_text

result = old_macdonald("macdonald")
print(result)