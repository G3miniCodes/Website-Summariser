import magic

try:
    mime = magic.Magic(mime=True)
    print(mime.from_buffer(b"Hello, world!"))
except Exception as e:
    print("Error:", e)