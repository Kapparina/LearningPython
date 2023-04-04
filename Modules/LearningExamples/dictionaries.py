monthConversions = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December",
}

print(monthConversions.get("Luv", "Not a valid key."))  # The value after the comma is a 'default value'.
# print(monthConversions["Luv", "Not gonna work."])  # Remove the '#' before 'print' to see contrast.
# A note on 'default values' and the 'get()' method:

# Default values act as fall-backs for the 'get()' method in cases where the dictionary key entered does not match any
# key present in the elected dictionary. For an example of this, refer to the code above.