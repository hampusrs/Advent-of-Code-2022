def read_file(file):
    file = open(file, 'r')
    data = []

    for line in file:
        opponent, my_respone = line.split()
        data.append((get_shape(opponent), get_shape(my_respone)))

    return data

def get_shape(letter):
    if letter == 'A' or letter == 'X':
        return "Rock"
    elif letter == 'Y' or letter == 'B':
        return "Paper"
    else:
        return "Scissors"

def calculate_games(rounds):
    game_scores =[]
    for round in rounds:
        game_scores.append(calculate_game(round[0], round[1]))

    return game_scores


def calculate_game(opponent, my_response):
    my_points = 0

    if my_response == "Rock":
        my_points += 1
    elif my_response == "Paper":
        my_points += 2
    elif my_response == "Scissors":
        my_points += 3

    my_points += calculate_score(opponent,my_response)

    return my_points

def calculate_score(opponent, my_response):
    if opponent == my_response:
        return 3
    if opponent == "Rock" and my_response == "Paper":
        return 6
    elif opponent == "Paper" and my_response == "Scissors":
        return 6
    elif opponent == "Scissors" and my_response == "Rock":
        return 6
    else:
        return 0

def main():
    file =  "./input.txt"
    data = read_file(file)

    game_scores = calculate_games(data)

    ans = sum(game_scores)
    print("Answer: %d" % (ans))

if __name__ == '__main__':
    main()