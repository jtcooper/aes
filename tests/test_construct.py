
l = 51

def construct(s: str):
    for i in range(int(len(s) / l)):
        print(s[i * l:(i+1) * l])
