import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Suman Prasad"
tokens = enc.encode(text)

print("Tokens", tokens)
# Tokens [25216, 3274, 0, 3673, 1308, 382, 336, 9276, 2284, 99152]

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 336, 9276, 2284, 99152])

print("Decoded", decoded)
# Decoded Hey There! My name is Suman Prasad

# AIzaSyAT0PBPaAXmXOk6WQ-1nY08C5XiTTf7Y8Q