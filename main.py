# Morse Code Dictionary
morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/',  # Space represented as slash
}


def morse_code_converter(text: str) -> str:
    """
    Converts text to Morse code. Unsupported characters are skipped with a warning.
    
    Parameters:
    text (str): The input text to convert.

    Returns:
    str: Morse code string with characters separated by commas.
    """
    text = text.upper()
    
    if not text.strip():
        raise ValueError("Input text cannot be empty.")
    
    morse_parts = []
    unsupported_chars = set()

    for char in text:
        if char in morse_code_dict:
            morse_parts.append(morse_code_dict[char])
        else:
            unsupported_chars.add(char)

    if unsupported_chars:
        print(f"Warning: The following characters are unsupported and were skipped: {', '.join(unsupported_chars)}")

    return ','.join(morse_parts)


# --- Main Program ---
while True:
    try:
        user_input = input("Enter the text: ")
        morse_result = morse_code_converter(user_input)
        print("Morse Code:", morse_result)
        break
    except ValueError as e:
        print(f"Error: {e} Please try again.\n")
