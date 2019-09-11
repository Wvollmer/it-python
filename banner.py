
def banner(title, author):
    title_length = len(title)
    byline = f"by {author}"
    byline_length = len(byline)
    banner_length = max(title_length, byline_length) + 8

    print("=" * banner_length )
    print(F"{title:^{banner_length}}")
    print(F"{byline:^{banner_length}}")
    print("=" * banner_length)
    print("")

banner("Hello","=)")

name = input ("what is your name?")
title = input("what is the quest?")
banner(title, name)