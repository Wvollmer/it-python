def tags_in (phrase):
    tags = "<>"
    count = 0
    for char in phrase:
        if char in tags:
            count = count +1
    return count