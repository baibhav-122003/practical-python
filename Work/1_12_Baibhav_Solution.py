# why does bool("False") returns True

check = bool("False")
print(check)

# Reason : bool(x) checks emptiness of the string, not the semantic meaning. It does not matter what is the string, if there is a non-empty string, it will be considered as True. Only empty string will be considered as False.
