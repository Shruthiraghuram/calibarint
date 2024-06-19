def findNeedle(haystack):
    for index, item in enumerate(haystack):
        if item == "needle":
            return f"found the needle at position {index} "
    return "needle not found"

haystack = ["hay", "junk", "hay", "hay" , "morejunk", "needle", "randomjunk"]
print(findNeedle(haystack))