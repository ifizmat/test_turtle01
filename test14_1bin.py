bin_str = b'\xbaxuWf\xd3'
print(f"bin_str: {bin_str}")

num_hex = bin_str.hex()
print(f"num_hex: {num_hex}")

num_dec = int(num_hex, 16)
print(f"num_dec: {num_dec}")

num_bin = bin(num_dec)
print(f"num_bin: {num_bin}")

num_bin = num_bin[2:]
print(f"num_bin: {num_bin}")
