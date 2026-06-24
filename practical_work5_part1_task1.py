people = [
    {"firstname": "Ivan", "lastname": "Ivanov", "height": 184, "sex": "male"},
    {"firstname": "Mykhailo", "lastname": "Yunyi", "height": 155, "sex": "male"},
    {"firstname": "Oleg", "lastname": "Zelenskiy", "height": 177, "sex": "male"},
    {"firstname": "Mariya", "lastname": "Savchenko", "height": 162, "sex": "female"},
    {"firstname": "Mykhailo", "lastname": "Sergeev", "height": 191, "sex": "male"},
    {"firstname": "Sergei", "lastname": "Ivanov", "height": 184, "sex": "male"},
    {"firstname": "Anastasiya", "lastname": "Umnaya", "height": 171, "sex": "female"},
    {"firstname": "Violeta", "lastname": "Usacheva", "height": 166, "sex": "female"},
    {"firstname": "Alexander", "lastname": "Pushkin", "height": 188, "sex": "male"},
    {"firstname": "Taras", "lastname": "Shevhenko", "height": 190, "sex": "male"}
]

def print_all_records(data):
    print("--- All records ---")
    for person in data:
        print(person)
    print()

def add_record(data, firstname, lastname, height, sex):
    new_person = {"firstname": firstname, "lastname": lastname, "height": height, "sex": sex}
    data.append(new_person)
    print(f"--- Record ({firstname} {lastname}) successfully added ---\n")

def remove_record(data, lastname):
    for i in range(len(data)):
        if data[i]["lastname"] == lastname:
            del data[i]
            print(f"--- Record with lastname '{lastname}' successfully deleted ---\n")
            return
    print(f"--- Record with lastname '{lastname}' not found ---\n")

def print_sorted_keys(data):
    print("--- Records by sorted keys ---")
    for person in data:
        sorted_keys = sorted(person.keys())
        output = ", ".join([f"'{key}': '{person[key]}'" for key in sorted_keys])
        print("{" + output + "}")
    print()

def avg_men_height(data):
    print("--- Variant task: Average men's height ---")
    men_counter = 0
    height_sum = 0
    for person in data:
        if person["sex"] == "male":
            men_counter += 1
            height_sum += person["height"]
            
    if men_counter > 0:
        avg_height = height_sum / men_counter
        print(f"Average height: {avg_height}")
    else:
        print("No men found in the list.")
    print()

print_all_records(people)
add_record(people, "Anna", "Kovalenko", 168, "female")
remove_record(people, "Yunyi")
print_sorted_keys(people)
avg_men_height(people)