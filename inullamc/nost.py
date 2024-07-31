def counter(start, stop):
    output = ""
    if start > stop:
        output += "Counting down: "
        for i in range(start, stop-1, -1):
            output += str(i) + ", "
    else:
        output += "Counting up: "
        for i in range(start, stop+1):
            output += str(i) + ", "
    return output.rstrip(", ")  # remove any trailing comma and space
