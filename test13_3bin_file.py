with open('input.zip', mode='rb') as bin_file:
    data3 = bin_file.read(55)
    data = bin_file.read()
print(type(data))
print(data)
print(f"input.zip - 55 bytes: {data3}")
print(f"input.zip - Hex dump 55 bytes: {data3.hex()}")
print(f"input.zip - Hex dump 55 bytes: {data3.hex(sep=' ', bytes_per_sep=-2)}")

chunk_size = 8
with open('input.zip', mode='rb') as bin_file:
    while True:
        chunk = bin_file.read(chunk_size)
        if not chunk:
            break

        print(f"Read {len(chunk)} bytes: {chunk}")
        print(f"Read {len(chunk)} bytes - hex: {chunk.hex()}")
        print(f"Read {len(chunk)} bytes - bin: {bin(int(chunk.hex(), 16))}")
