import webbrowser

lines = []
with open("../../MiscFiles/hyperlinks_from_MS_Edge.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
        webbrowser.get("windows-default")
        webbrowser.open_new(line)
print(lines)
