text=input("Enter the text:")
shift= 3
result= ""
text=text.upper()
for ch in text:
    if ch>="A" and ch <="Z":
        position=ord(ch)-ord("A")
        new_position=(position+shift)%26
        encrypted_char=chr(new_position+ord("A"))
        result=result+encrypted_char
        
    else:
        result=result+ch
        

print("Encrypted text:",result)

decrypted_result = ""
for ch in result:
    if ch>="A" and ch <="Z":
        position=ord(ch)-ord("A")
        new_position=(position-shift)%26
        decrypted_char=chr(new_position+ord("A"))
        decrypted_result = decrypted_result + decrypted_char
    else:
        decrypted_result = decrypted_result + ch
        
print("Decrypted text:",decrypted_result)
    


