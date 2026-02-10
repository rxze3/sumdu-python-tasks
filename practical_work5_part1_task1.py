people = [{"firstname" : "Ivan", "lastname" : "Ivanov", "height" : 184, "sex" : "male"},
          {"firstname" : "Mykhailo", "lastname" : "Yunyi", "height" : 155, "sex" : "male"},
          {"firstname" : "Oleg", "lastname" : "Zelenskiy", "height" : 177, "sex" : "male"},
          {"firstname" : "Mariya", "lastname" : "Savchenko", "height" : 162, "sex" : "female"},
          {"firstname" : "Mykhailo", "lastname" : "Sergeev", "height" : 191, "sex" : "male"},
          {"firstname" : "Sergei", "lastname" : "Ivanov", "height" : 184, "sex" : "male"},
          {"firstname" : "Anastasiya", "lastname" : "Umnaya", "height" : 171, "sex" : "female"},
          {"firstname" : "Violeta", "lastname" : "Usacheva", "height" : 166, "sex" : "female"},
          {"firstname" : "Alexander", "lastname" : "Pushkin", "height" : 188, "sex" : "male"},
          {"firstname" : "Taras", "lastname" : "Shevhenko", "height" : 190, "sex" : "male"}]

def avg_men_height(people):
    men_counter = 0
    height_sum = 0
    for person in people:
        if person["sex"] == "male":
            men_counter += 1
            height_sum += person["height"]
    avg_height = height_sum / men_counter
    print(avg_height)

avg_men_height(people)