name = "Monty Python"

# Write a function that takes an email and returns the domain.
# index and slicing only
email1 = "rafael.avigad@nmtafe.wa.edu.au"
email2 = "blazegreenhalgh1943@gmail.com"

def find_domain(email):
    index_of_at = email.index("@")
    return email[index_of_at+1:]

print(find_domain(email1))
print(find_domain(email2))