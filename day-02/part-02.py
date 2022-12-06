def read_file(file):
    file = open(file, 'r')
    data = []

    for line in file:
        opponent, my_respone = line.split()
        data.append((get_shape(opponent), get_outcome(my_respone)))

    return data

def get_shape(letter):
    if letter == 'A' or letter == 'X':
        return "Rock"
    elif letter == 'Y' or letter == 'B':
        return "Paper"
    else:
        return "Scissors"

def get_outcome(letter):
    if letter == 'X':
        return "Lose"
    elif letter == 'Y':
        return "Draw"
    else:
        return "Win"

def calculate_games(rounds):
    game_scores =[]
    for round in rounds:
        game_scores.append(calculate_game(round[0], round[1]))

    return game_scores


def calculate_game(opponent, my_response):
    my_points = 0

    if my_response == "Lose":
        my_points += 0
    elif my_response == "Draw":
        my_points += 3
    elif my_response == "Win":
        my_points += 6

    my_points += calculate_score(opponent,my_response)

    return my_points

def calculate_score(opponent, my_response):
    if opponent == "Rock" and my_response == "Win":
        return 2
    elif opponent == "Paper" and my_response == "Win":
        return 3
    elif opponent == "Scissors" and my_response == "Win":
        return 1
    elif opponent == "Rock" and my_response == "Lose":
        return 3
    elif opponent == "Paper" and my_response == "Lose":
        return 1
    elif opponent == "Scissors" and my_response == "Lose":
        return 2
    elif opponent == "Rock" and my_response == "Draw":
        return 1
    elif opponent == "Paper" and my_response == "Draw":
        return 2
    elif opponent == "Scissors" and my_response == "Draw":
        return 3

def main():
    file =  "./input.txt"
    data = read_file(file)

    game_scores = calculate_games(data)

    ans = sum(game_scores)
    print("Answer: %d" % (ans))

if __name__ == '__main__':
    main()