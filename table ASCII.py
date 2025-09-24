print(f"{'Char':^5} | {'Dec':^5} | {'Bin':^10} | {'Hex':^5}")
print("-" * 30)

for code in range(32, 127):
    char = chr(code)
    print(f"{char:^5} | {code:^5} | {bin(code)[2:].zfill(8):^10} | {hex(code)[2:].upper():^5}")
