def merge_the_tools(string, k):
# your code goes here
    while string:
        s = string[0:k]
        seen = ''
        for c in s:
            if c not in seen:
                seen += c
            print(seen)
            string = string[k:]
