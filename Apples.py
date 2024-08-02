def distribute_apples():
    total_amount = 100
    payments = {
        "Ram": 50,
        "Sham": 30,
        "Rahim": 20
    }

   #calculate share
    shares = {person: (payment / total_amount) for person, payment in payments.items()}

   
    apple_weights = []

    
    while True:
        weight = int(input("Enter apple weight in grams (-1 to stop): "))
        if weight == -1:
            break
        apple_weights.append(weight)

    apple_weights.sort(reverse=True)
    distribution = {
        "Ram": [],
        "Sham": [],
        "Rahim": []
    }

    current_weight = {
        "Ram": 0,
        "Sham": 0,
        "Rahim": 0
    }

    total_apple_weight = sum(apple_weights)

    # update wt for each person
    target_weights = {person: shares[person] * total_apple_weight for person in payments.keys()}

    for weight in apple_weights:
        best_person = None
        smallest_difference = float('inf')

        for person in payments.keys():
            projected_weight = current_weight[person] + weight
            difference = abs(projected_weight - target_weights[person])
            target_met_ratio = projected_weight / target_weights[person]
            if difference < smallest_difference and target_met_ratio <= 1.0:
                smallest_difference = difference
                best_person = person
        if best_person is None:
            best_person = min(payments.keys(), key=lambda person: abs(current_weight[person] + weight - target_weights[person]))
        distribution[best_person].append(weight)
        current_weight[best_person] += weight
    print("\nDistribution Result:")
    for person, apples in distribution.items():
        apples_list = ", ".join(map(str, apples))
        print(f"{person}: {apples_list}")


distribute_apples()
