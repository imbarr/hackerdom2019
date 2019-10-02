import re
import base64

eng_to_morse = {
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
    '9': '----.' 
}

morse_to_eng = { value: key for key, value in eng_to_morse.items()}

text = '''BBBBX B XBBBB XBB BBBBX B XBBBB XBBB BBBBX XBB XXBBB BX BBBBB BBBBB BBBXX BXXXX BBBBX B XBBBB XBB BBBBB
	BBXXX XBBBB XBXB BBBBB XXXXB XBBBB BX BBBBX BBXXX XBBBB XBBB BBBBB XXXXB BBBBB BBBBX BBBBB BBBBB BBBXX
	XXXXX BBBBB XXXXB XBBBB XBB BBBBX B XBBBB XXXBB BBBBX XBB BBBBX BBBBX BBBBB XXXXB XXBBB XXBBB BBBBB
	XXXXB XBBBB BX BBBBB BBXXX XBBBB BX BBBBX XBB XXBBB BX XBBBB XBBB BBBXX XXXXX BBBBX B XXBBB BX XBBBB
	XBBB BBBXX BBBBX BBBBX XBB XXBBB BX XBBBB XBBB BBBXX XBB'''

def to_letter(xb):
	morse = xb.replace('B', '.').replace('X', '-')
	return morse_to_eng[morse]

hex_number = [ to_letter(xb) for xb in re.split(r'\s', text) if xb != '']

hex_bytes = [ ''.join(hex_number[i:i+2]) for i in range(0, len(hex_number), 2)]

ascii_chars = [ chr(int(b, 16)) for b in hex_bytes ]

b64content = base64.b64decode(''.join(ascii_chars))

another_number = b64content.decode('ascii')

print(another_number)
print("now use rainbow tables or go to https://crackstation.net/")
