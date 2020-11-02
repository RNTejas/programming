def banner_text(text):
    screen_width = 50
    if len(text) > screen_width - 4:
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
        # instead of doing this you can do this by arising the ValueError
        raise ValueError("String {} is larger than Specified width {}".format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of Life...")
banner_text("if life seems Jolly rotten,")
banner_text("There's something you have forgotten!")
banner_text("And that's to laugh and smile and Dance and sing,")
banner_text(" ")
banner_text("When you are feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse you lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")
