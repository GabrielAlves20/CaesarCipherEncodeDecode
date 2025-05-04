from tkinter import *
from cipher import encrypt, decrypt

window = Tk()
window.title("Caesar Encode/Decode")

def handle_encode(text):
    result = encrypt(text)
    label_encode_result.config(text=f"Result: {result}")

def handle_decode(text):
    result = decrypt(text)
    label_decode_result.config(text=f"Result: {result}")

#####
Label(window, text="Text to encode:").grid(column=0, row=0)
entry_encode = Entry(window, width=40)
entry_encode.grid(column=1, row=0)

#####
button_encode = Button(window, text="Encode", command=lambda: handle_encode(entry_encode.get()))
button_encode.grid(column=2, row=0)

#####
label_encode_result = Label(window, text="Result: ")
label_encode_result.grid(column=1, row=1)

#####
Label(window, text="Text to decode:").grid(column=0, row=2)
entry_decode = Entry(window, width=40)
entry_decode.grid(column=1, row=2)

#####
button_decode = Button(window, text="Decode", command=lambda: handle_decode(entry_decode.get()))
button_decode.grid(column=2, row=2)

#####
label_decode_result = Label(window, text="Result: ")
label_decode_result.grid(column=1, row=3)

window.mainloop()
