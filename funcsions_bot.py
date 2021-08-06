def numbers(txt):
    try:
        bot_dict = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five'
        }
        return bot_dict[int(txt)]

    except Exception:
        return "Send me number!"
