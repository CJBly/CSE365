#!/bin/bash
binary_string="1110010011011001100000101101110111111010101111001100010010011001"

# Function to convert binary to hex
binary_to_hex() {
    echo "obase=16; ibase=2; $1" | bc
}

# Split binary string into 8-bit chunks and convert to hex
hex_string=""
for ((i=0; i<${#binary_string}; i+=8)); do
    byte=${binary_string:i:8}
    hex=$(binary_to_hex $byte)
    hex_string+="\\x$hex"
done

# Output the hex string
echo -e "$hex_string" | /challenge/runme
