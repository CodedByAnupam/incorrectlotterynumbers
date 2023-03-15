# Write your solution here
def filter_incorrect():
    with open("correct_numbers.csv", "w") as new_file:
        pass
    with open("lottery_numbers.csv") as new_file1:
        for line in new_file1:
            line = line.replace("\n", "")
            parts = line.split(";")
            week = parts[0].split(" ")[1]
            numbers = parts[1]
            is_valid_line = True
            try:
                week = int(week)
                number = numbers.split(",")
                if len(number) != 7:
                    continue
                for num in number:
                    if int(num) < 1 or int(num) > 39 or number.count(num) > 1:
                        is_valid_line = False
            except:
                continue
            if is_valid_line:
                with open("correct_numbers.csv", "a") as new_file2:
                    new_file2.write(line + "\n")


if __name__ == "__main__":
    filter_incorrect()
