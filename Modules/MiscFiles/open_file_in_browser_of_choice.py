import webbrowser

from check_if_process_exist import process_exists


list_of_formatted_items = []

with open("../MiscFiles/testing hyperlinks doc.txt", "r") as data_from_text_file:
    for each_line_in_text_file in data_from_text_file:
        list_of_formatted_items.append(each_line_in_text_file.strip())
print("What the fuck cunt")

process_state = ()
process_exists("vivaldi.exe")

print("This shit so buggy?????????")

if process_state == True:
    webbrowser.open_new_tab(webbrowser.get == str(("windows-default")))
else:
    process_state == False
    print("broke nibbah things")

print("FKN PRINTTTTTTTTTTTT")