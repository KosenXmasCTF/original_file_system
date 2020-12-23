image = open('prob1.img','wb')

image.write(b'\xde\xad\xbe\xaf')
image.write(b'\x00\x00\x00\x08')
image.write(b'\x00')
image.write(b'mydir\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
image.write(b'\x00\x00\x00\x00')
image.write(b'\x00\x00\x00\x01')
offset = (image.tell()+1).to_bytes(4,byteorder='big')
image.write(offset)
image.write(b'\x02')

key =  "xm4s!xm4s!xm4s!xm4s!xm4s!xm"
flag = "xm4s{you_find_a_file_name!}"
key = [ord(j) for j in key]
flag = [ord(j) for j in flag]

enc = [key[j] ^ flag[j] for j in range(len(flag))]
enc = b''.join([j.to_bytes(1,byteorder='big') for j in enc])

image.write(enc)

image.write(b'\x00\x00\x00\x00')
image.write(b'\x00\x00\x00\x00')
image.write(b'\x00\x00\x00\x00')
