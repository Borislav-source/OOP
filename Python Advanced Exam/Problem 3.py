def flights(*args):
    flights_dict = {}
    for index in range(0, len(args), 2):
        if not args[index] == 'Finish':
            if args[index] not in flights_dict:
                flights_dict[args[index]] = args[index+1]
            else:
                flights_dict[args[index]] += args[index + 1]
        else:
            return flights_dict
    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))