def to_camel_case(text):
    sr = []
    text = text.replace("-","_")
    camel=""
    if "_" in text:
        sr = text.split("_")
        for i in range(1, len(sr)):
            sr[i] = sr[i].capitalize()
        camel = "".join(sr)
    return camel


print(to_camel_case("the-steal-warrior"))