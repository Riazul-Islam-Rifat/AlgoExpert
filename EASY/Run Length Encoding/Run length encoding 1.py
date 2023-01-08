def runLengthEncoding(string):
    counter = 1
    long_run = []
    last_str = string[0]
    found_nine = False
    for item in range(len(string) - 1):

        if string[item] == string[item + 1]:
            if counter < 9:
                found_nine = False
                counter += 1
                if counter == 9:
                    found_nine = True
                    split_run = str(counter) + string[item]
                    long_run.append(split_run)

                    counter = 0
        else:
            if not found_nine:
                split_run = str(counter) + string[item]
                long_run.append(split_run)

                counter = 1
            else:
                counter += 1

        last_str = string[item + 1]

    split_run = str(counter) + last_str
    long_run.append(split_run)

    return ''.join(long_run)


