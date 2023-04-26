DIGIT_CHECKS = 0
INDEX_CHECKS = 0
test_list = [1, 2, 3, 4]
def bookmark_check(value_to_check, digit_check=DIGIT_CHECKS, index_check=INDEX_CHECKS):
    if digit_check <= 0:
        print("\nYou must enter a number; I will allow 3 more attempts to do so.")
    if index_check <= 0:
        print("Likewise, you must enter an index number present in the list; again - you have 3 attempts.\n")
    while True:
        print("Please enter a bookmark's corresponding index number below.")
        value_to_check = input("\tBookmark number: ")

        if value_to_check.isdigit():
            digit_check += 1

            if int(value_to_check) in test_list:
                break
            else:
                print("No value exists at that index...")
                index_check += 1
                if 1 <= index_check <= 3:
                    print(f"- Index check attempt {index_check}/3 -")
                elif index_check >= 3:
                    print("\nThat's 3/3 index checks completed - continuing without bookmarks.")
                    return "/"

        else:
            print("\nI require a valid integer/whole number...\n")
            digit_check += 1
            if 1 <= digit_check <= 3:
                print(f"- Integer check attempt {digit_check}/3 -")
            elif digit_check >= 3:
                print("\n3/3 integer checks performed - continuing without bookmarks.")
                return "/"

    return value_to_check


value = input("gimme number: ")
if value.isdigit() is False:
    value = bookmark_check(value)
elif int(value) not in test_list:
    value = bookmark_check(value)

print("good")


# digit_checks = 0
#     while value_to_check.isdigit() is False:
#         if digit_checks <= 0:
#             print("The bookmark index must be a number; you have 3 retries available.")
#             value_to_check = input("\tEnter a valid number: ")
#             digit_checks += 1
#         elif 1 <= digit_checks <= 3:
#             print(f"{digit_checks}/3 allowed retries attempted...")
#             value_to_check = input("\tPlease enter a valid number: ")
#             digit_checks += 1
#         elif digit_checks >= 3:
#             print("3/3 allowed retries attempted, continuing without bookmarks...")
#             return "/"