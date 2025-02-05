import random

# Predefined Google Dork queries
dork_queries = [
    "inurl:admin",
    "inurl:login",
    "intitle:index of",
    "inurl:wp-content",
    "inurl:php?id=",
    "inurl:.php?search=",
    "ext:sql | ext:db | ext:dbf | ext:mdb",
    "inurl:/cgi-bin/",
    "filetype:log",
    "site:.gov inurl:admin",
    "inurl:signup",
    "intext:password filetype:log",
    "ext:xml inurl:webconfig",
    "intitle:\"webcam 7\""
]

# Function to generate random dorks
def generate_dorks(n, keywords):
    all_dorks = dork_queries[:]
    
    # If user provides keywords, create custom dorks
    if keywords:
        for keyword in keywords:
            all_dorks.append(f"inurl:{keyword}")
            all_dorks.append(f"intitle:{keyword}")
            all_dorks.append(f"intext:{keyword}")
            all_dorks.append(f"site:.com inurl:{keyword}")

    # Print random dorks
    for _ in range(n):
        print(random.choice(all_dorks))

# Get user input for custom keywords
keywords = []
add_keywords = input("Do you want to add keywords? (yes/no): ").strip().lower()

if add_keywords == "yes":
    keywords = input("Enter keywords separated by commas: ").split(",")

# Get user input for number of dorks
try:
    num = int(input("Enter the number of dorks to generate: "))
    generate_dorks(num, keywords)
except ValueError:
    print("Invalid input! Please enter a number.")