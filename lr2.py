def print_ascii_codes(*parts):
    full_name = " ".join(parts)
    for char in full_name:
        if char == " ":
            print()  
            continue
        print(char)
        print(f"10: {ord(char)}")
        print(f"2: {bin(ord(char))[2:].zfill(8)}")
        print(f"16: {hex(ord(char))[2:].upper()}")
        print()

print_ascii_codes(
    "Kuzmynskiy", "Kirill",
    "Bulavka", "Oleksandr",
    def print_ascii_codes(*parts):
    full_name = " ".join(parts)
    for char in full_name:
        if char == " ":
            print()  
            continue
        print(char)
        print(f"10: {ord(char)}")
        print(f"2: {bin(ord(char))[2:].zfill(8)}")
        print(f"16: {hex(ord(char))[2:].upper()}")
        print()

print_ascii_codes(
    "Kuzmynskiy", "Kirill",
    "Bulavka", "Oleksandr",
     "Dmytro", "Yukhymovych",
)





