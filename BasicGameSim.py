def BaseballSim():

    import random

    ## Game setup
    innings = 9
    current_inning = 1
    ## h_hits = 0
    h_runs = 0
    ## a_hits = 0
    a_runs = 0

    ## Game start
    
    while current_inning <= innings:
        ## reset half of inning
        a_outs = 0
        first_base = 0
        second_base = 0
        third_base = 0
        print("Top " + repr(current_inning) + "\n")

        ## top half of inning
        while a_outs < 3:
            ## determine outcome of PA
            roll = random.random()
            if roll <= 0.683289:
                outcome = "out"
                a_outs = a_outs + 1
            elif roll > 0.683289 and roll <= 0.837822409:
                outcome = "single"
            elif roll > 0.837822409 and roll <= 0.92838502:
                outcome = "walk"
            elif roll > 0.92838502 and roll <= 0.972625158:
                outcome = "double"
            elif roll > 0.972625158 and roll <= 0.977241094:
                outcome = "triple"
            else:
                outcome = "homerun"

            print(outcome)

            ## Base changes

            ## bases empty
            if first_base == 0 and second_base == 0 and third_base == 0:
                if outcome == "single" or outcome == "walk":
                    first_base = 1
                elif outcome == "double":
                    second_base = 1
                elif outcome == "triple":
                    third_base = 1
                elif outcome == "homerun":
                    a_runs = a_runs + 1

            ## runner on first
            elif first_base == 1 and second_base == 0 and third_base == 0:
                if outcome == "walk":
                    second_base = 1
                elif outcome == "single":
                    bsr = random.random()
                    if bsr <= 0.72:
                        second_base = 1
                    else:
                        third_base = 1
                elif outcome == "double":
                    first_base = 0
                    second_base = 1
                    bsr = random.random()
                    if bsr <= 0.38:
                        third_base = 1
                    else:
                        a_runs = a_runs + 1
                elif outcome == "triple":
                    first_base = 0
                    third_base = 1
                    a_runs = a_runs + 1
                elif outcome == "homerun":
                    first_base = 0
                    a_runs = a_runs + 2

            ## runner on second
            elif first_base == 0 and second_base == 1 and third_base == 0:
                if outcome == "walk":
                    first_base = 1
                elif outcome == "single":
                    first_base = 1
                    second_base = 0
                    bsr = random.random()
                    if bsr <= 0.42:
                        third_base = 1
                    else:
                        a_runs = a_runs + 1
                elif outcome == "double":
                    second_base = 1
                    a_runs = a_runs + 1
                elif outcome == "triple":
                    second_base = 0
                    third_base = 1
                    a_runs = a_runs + 1
                elif outcome == "homerun":
                    second_base = 0
                    a_runs = a_runs + 2

             ## runner on third
            elif first_base == 0 and second_base == 0 and third_base == 1:
                if outcome == "walk":
                    first_base = 1
                elif outcome == "single":
                    first_base = 1
                    third_base = 0
                    a_runs = a_runs + 1
                elif outcome == "double":
                    second_base = 1
                    third_base = 0
                    a_runs = a_runs + 1
                elif outcome == "triple":
                    third_base = 1
                    a_runs = a_runs + 1
                elif outcome == "homerun":
                    third_base = 0
                    a_runs = a_runs + 2

            ## runners on first and second
            elif first_base == 1 and second_base == 1 and third_base == 0:
                if outcome == "walk":
                    third_base = 1
                elif outcome == "single":
                    bsr = random.random()
                    if bsr <= 0.42:
                        third_base = 1
                    else:
                        a_runs = a_runs + 1
                    bsr_2 = random.random()
                    if bsr > 0.42 and bsr_2 > 0.72:
                        second_base = 0
                        third_base = 1
                elif outcome == "double":
                    first_base = 0
                    bsr = random.random()
                    if bsr <= 0.38:
                        third_base = 1
                        a_runs = a_runs + 1
                    else:
                        a_runs = a_runs + 2
                elif outcome == "triple":
                    first_base = 0
                    second_base = 0
                    third_base = 1
                    a_runs = a_runs + 2
                elif outcome == "homerun":
                    first_base = 0
                    second_base = 0
                    a_runs = a_runs + 3

            ## runners on first and third
            elif first_base == 1 and second_base == 0 and third_base == 1:
                if outcome == "walk":
                    second_base = 1
                elif outcome == "single":
                    bsr = random.random()
                    if bsr <= 0.72:
                        second_base = 1
                        third_base = 0
                    else:
                        third_base = 1
                    a_runs = a_runs + 1
                elif outcome == "double":
                    first_base = 0
                    second_base = 1
                    bsr = random.random()
                    if bsr <= 0.38:
                        third_base = 1
                        a_runs = a_runs + 1
                    else:
                        third_base = 0
                        a_runs = a_runs + 2
                elif outcome == "triple":
                    first_base = 0
                    third_base = 1
                    a_runs = a_runs + 2
                elif outcome == "homerun":
                    first_base = 0
                    third_base = 0
                    a_runs = a_runs + 3

            ## runners on second and third
            elif first_base == 0 and second_base == 1 and third_base == 1:
                if outcome == "walk":
                    first_base = 1
                elif outcome == "single":
                    first_base = 1
                    second_base = 0
                    bsr = random.random()
                    if bsr <= 0.42:
                        third_base = 1
                        a_runs = a_runs + 1
                    else:
                        third_base = 0
                        a_runs = a_runs + 2
                elif outcome == "double":
                    second_base = 1
                    third_base = 0
                    a_runs = a_runs + 2
                elif outcome == "triple":
                    second_base = 0
                    third_base = 1
                    a_runs = a_runs + 2
                elif outcome == "homerun":
                    second_base = 0
                    third_base = 0
                    a_runs = a_runs + 3

            ## bases loaded
            elif first_base == 1 and second_base == 1 and third_base == 1:
                if outcome == "walk":
                    a_runs = a_runs + 1
                elif outcome == "single":
                    bsr = random.random()
                    if bsr <= 0.42:
                        a_runs = a_runs + 1
                    else:
                        a_runs = a_runs + 2
                    bsr_2 = random.random()
                    if bsr > 0.42 and bsr_2 > 0.72:
                        second_base = 0
                    else:
                        third_base = 0
                elif outcome == "double":
                    first_base = 0
                    second_base = 1
                    bsr = random.random()
                    if bsr <= 0.38:
                        third_base = 1
                        a_runs = a_runs + 2
                    else:
                        third_base = 0
                        a_runs = a_runs + 3
                elif outcome == "triple":
                    first_base = 0
                    second_base = 0
                    third_base = 1
                    a_runs = a_runs + 3
                elif outcome == "homerun":
                    first_base = 0
                    second_base = 0
                    third_base = 0
                    print("Grand Slam HR for the away team!")
                    a_runs = a_runs + 4

        print("\n" + "After top " + repr(current_inning) + " the score is Home " + repr(h_runs) + "," + " Away " + repr(a_runs) + "\n")

        ## reset half of inning
        h_outs = 0
        first_base = 0
        second_base = 0
        third_base = 0
        print("Bottom " + repr(current_inning) + "\n")

         ## bottom half of inning
        while h_outs < 3:
            ## determine outcome of PA
            roll = random.random()
            if roll <= 0.683289:
                outcome = "out"
                h_outs = h_outs + 1
            elif roll > 0.683289 and roll <= 0.837822409:
                outcome = "single"
            elif roll > 0.837822409 and roll <= 0.92838502:
                outcome = "walk"
            elif roll > 0.92838502 and roll <= 0.972625158:
                outcome = "double"
            elif roll > 0.972625158 and roll <= 0.977241094:
                outcome = "triple"
            else:
                outcome = "homerun"

             print(outcome)

            ## Base changes

            ## bases empty
            if first_base == 0 and second_base == 0 and third_base == 0:
                if outcome == "single" or outcome == "walk":
                    first_base = 1
                elif outcome == "double":
                    second_base = 1
                elif outcome == "triple":
                    third_base = 1
                elif outcome == "homerun":
                    h_runs = h_runs + 1

            ## runner on first
            elif first_base == 1 and second_base == 0 and third_base == 0:
                if outcome == "single" or outcome == "walk":
                    first_base = 1
                    second_base = 1
                elif outcome == "double":
                    first_base = 0
                    second_base = 1
                    third_base = 1
                elif outcome == "triple":
                    first_base = 0
                    third_base = 1
                    h_runs = h_runs + 1
                elif outcome == "homerun":
                    first_base = 0
                    h_runs = h_runs + 2

            ## runner on second
            elif first_base == 0 and second_base == 1 and third_base == 0:
                if outcome == "walk":
                    first_base = 1
                elif outcome == "single":
                    first_base = 1
                    second_base = 0
                    third_base = 1
                elif outcome == "double":
                    second_base = 1
                    h_runs = h_runs + 1
                elif outcome == "triple":
                    second_base = 0
                    third_base = 1
                    h_runs = h_runs + 1
                elif outcome == "homerun":
                    second_base = 0
                    h_runs = h_runs + 2

             ## runner on third
            elif first_base == 0 and second_base == 0 and third_base == 1:
                if outcome == "walk":
                    first_base = 1
                elif outcome == "single":
                    first_base = 1
                    third_base = 0
                    h_runs = h_runs + 1
                elif outcome == "double":
                    second_base = 1
                    third_base = 0
                    h_runs = h_runs + 1
                elif outcome == "triple":
                    third_base = 1
                    h_runs = h_runs + 1
                elif outcome == "homerun":
                    third_base = 0
                    h_runs = h_runs + 2

            ## runners on first and second
            elif first_base == 1 and second_base == 1 and third_base == 0:
                if outcome == "walk":
                    third_base = 1
                elif outcome == "single":
                    third_base = 1
                elif outcome == "double":
                    first_base = 0
                    second_base = 1
                    third_base = 1
                    h_runs = h_runs + 1
                elif outcome == "triple":
                    first_base = 0
                    second_base = 0
                    third_base = 1
                    h_runs = h_runs + 2
                elif outcome == "homerun":
                    first_base = 0
                    second_base = 0
                    h_runs = h_runs + 3

            ## runners on first and third
            elif first_base == 1 and second_base == 0 and third_base == 1:
                if outcome == "walk":
                    second_base = 1
                elif outcome == "single":
                    second_base = 1
                    third_base = 0
                    h_runs = h_runs + 1
                elif outcome == "double":
                    first_base = 0
                    second_base = 1
                    third_base = 1
                    h_runs = h_runs + 1
                elif outcome == "triple":
                    first_base = 0
                    third_base = 1
                    h_runs = h_runs + 2
                elif outcome == "homerun":
                    first_base = 0
                    third_base = 0
                    h_runs = h_runs + 3

            ## runners on second and third
            elif first_base == 0 and second_base == 1 and third_base == 1:
                if outcome == "walk":
                    first_base = 1
                elif outcome == "single":
                    first_base = 1
                    second_base = 0
                    third_base = 1
                    h_runs = h_runs + 1
                elif outcome == "double":
                    second_base = 1
                    third_base = 0
                    h_runs = h_runs + 2
                elif outcome == "triple":
                    second_base = 0
                    third_base = 1
                    h_runs = h_runs + 2
                elif outcome == "homerun":
                    second_base = 0
                    third_base = 0
                    h_runs = h_runs + 3

            ## bases loaded
            elif first_base == 1 and second_base == 1 and third_base == 1:
                if outcome == "walk":
                    h_runs = h_runs + 1
                elif outcome == "single":
                    h_runs = h_runs + 1
                elif outcome == "double":
                    first_base = 0
                    second_base = 1
                    third_base = 1
                    h_runs = h_runs + 2
                elif outcome == "triple":
                    first_base = 0
                    second_base = 0
                    third_base = 1
                    h_runs = h_runs + 3
                elif outcome == "homerun":
                    first_base = 0
                    second_base = 0
                    third_base = 0
                    print("Grand Slam HR for the home team!")
                    h_runs = h_runs + 4

        print("\n"+ "After bottom " + repr(current_inning) + " the score is Home " + repr(h_runs) + "," + " Away " + repr(a_runs) + "\n")

        ## increment inning
        current_inning = current_inning + 1

    print("Game over!")
    return h_runs, a_runs


def SimAgg(num_games):

    import numpy

    global HomeScores
    HomeScores = []
    HomeWins = 0

    global AwayScores
    AwayScores = []
    AwayWins = 0

    Ties = 0
    games_simmed = 0

    while games_simmed <= num_games:
        h_runs, a_runs = BaseballSim()
        HomeScores.append(h_runs)
        AwayScores.append(a_runs)
        if h_runs > a_runs:
            HomeWins = HomeWins + 1
        elif h_runs == a_runs:
            Ties = Ties + 1
        elif h_runs < a_runs:
            AwayWins = AwayWins + 1
        games_simmed = games_simmed + 1

    print("Home Wins: " + repr(HomeWins))
    print("Ties: " + repr(Ties))
    print("Away Wins: " + repr(AwayWins) + "\n")
        
    print("Home Score Average is " + repr(float((sum(HomeScores))/(len(HomeScores)))) + " runs per game")
    print("Away Score Average is " + repr(float((sum(AwayScores))/(len(AwayScores)))) + " runs per game")
