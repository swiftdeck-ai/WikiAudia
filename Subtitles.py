def formatdatetimetosub(dt):
    subformat = str(dt).split()[1].replace(".", ",")
    if "," not in subformat:
        subformat += ",000"
    else:
        subformat = subformat[:-3]
    return subformat
