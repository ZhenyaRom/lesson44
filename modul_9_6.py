def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)):
            if (j + i) > (len(text) - 1):
                break
            yield text[j:j + i + 1]

a = all_variants("abc")
for i in a:
    print(i)
    