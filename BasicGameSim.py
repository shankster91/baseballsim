def PAOutcome():

    import random

    ## hitter
    hOutFreq = 0.7
    hWalkFreq = 0.03
    hHRFreq = 0.02
    hTripleFreq = 0.01
    hDoubleFreq = 0.05
    hSingleFreq = 0.19

    ## league
    lOutFreq = 0.683289
    lWalkFreq = 0.090562
    lHRFreq = 0.022758
    lTripleFreq = 0.004615
    lDoubleFreq = 0.044240
    lSingleFreq = 0.154533

    ## pitcher
    pOutFreq = 0.65
    pWalkFreq = 0.06
    pHRFreq = 0.06
    pTripleFreq = 0.01
    pDoubleFreq = 0.06
    pSingleFreq = 0.16

    ## OUTCOME DETERMINATION

    ## out
    hOut = hOutFreq/(hOutFreq + hWalkFreq + hHRFreq + hTripleFreq + hDoubleFreq + hSingleFreq)
    lOut = lOutFreq/(lOutFreq + lWalkFreq + lHRFreq + lTripleFreq + lDoubleFreq + lSingleFreq)
    pOut = pOutFreq/(pOutFreq + pWalkFreq + pHRFreq + pTripleFreq + pDoubleFreq + pSingleFreq)

    hOutOdds = hOut/(1-hOut)
    lOutOdds = lOut/(1-lOut)
    pOutOdds = pOut/(1-pOut)

    outOdds = hOutOdds * (pOutOdds/lOutOdds)

    outProb = outOdds/(1+outOdds)

    outProbFinal = outProb

    ## walk if not out
    hWalk = hWalkFreq/(hWalkFreq + hHRFreq + hTripleFreq + hDoubleFreq + hSingleFreq)
    lWalk = lWalkFreq/(lWalkFreq + lHRFreq + lTripleFreq + lDoubleFreq + lSingleFreq)
    pWalk = pWalkFreq/(pWalkFreq + pHRFreq + pTripleFreq + pDoubleFreq + pSingleFreq)

    hWalkOdds = hWalk/(1-hWalk)
    lWalkOdds = lWalk/(1-lWalk)
    pWalkOdds = pWalk/(1-pWalk)

    walkOdds = hWalkOdds * (pWalkOdds/lWalkOdds)

    walkProb = walkOdds/(1+walkOdds)

    walkProbFinal = (1-outProbFinal) * walkProb

    ## homerun if not out and not walk
    hHR = hHRFreq/(hHRFreq + hTripleFreq + hDoubleFreq + hSingleFreq)
    lHR = lHRFreq/(lHRFreq + lTripleFreq + lDoubleFreq + lSingleFreq)
    pHR = pHRFreq/(pHRFreq + pTripleFreq + pDoubleFreq + pSingleFreq)

    hHROdds = hHR/(1-hHR)
    lHROdds = lHR/(1-lHR)
    pHROdds = pHR/(1-pHR)

    HROdds = hHROdds * (pHROdds/lHROdds)

    HRProb = HROdds/(1+HROdds)

    HRProbFinal = (1-outProbFinal-walkProbFinal) * HRProb

    ## triple if not out and if not walk and if not HR
    hTriple = hTripleFreq/(hTripleFreq + hDoubleFreq + hSingleFreq)
    lTriple = lTripleFreq/(lTripleFreq + lDoubleFreq + lSingleFreq)
    pTriple = pTripleFreq/(pTripleFreq + pDoubleFreq + pSingleFreq)

    hTripleOdds = hTriple/(1-hTriple)
    lTripleOdds = lTriple/(1-lTriple)
    pTripleOdds = pTriple/(1-pTriple)

    tripleOdds = hTripleOdds * (pTripleOdds/lTripleOdds)

    tripleProb = tripleOdds/(1+tripleOdds)

    tripleProbFinal = (1-outProbFinal-walkProbFinal-HRProbFinal) * tripleProb

    ## double if not out and if not walk and if not HR and if not triple
    hDouble = hDoubleFreq/(hDoubleFreq + hSingleFreq)
    lDouble = lDoubleFreq/(lDoubleFreq + lSingleFreq)
    pDouble = pDoubleFreq/(pDoubleFreq + pSingleFreq)

    hDoubleOdds = hDouble/(1-hDouble)
    lDoubleOdds = lDouble/(1-lDouble)
    pDoubleOdds = pDouble/(1-pDouble)

    doubleOdds = hDoubleOdds * (pDoubleOdds/lDoubleOdds)

    doubleProb = doubleOdds/(1+doubleOdds)

    doubleProbFinal = (1-outProbFinal-walkProbFinal-HRProbFinal-tripleProbFinal) * doubleProb

    ## single if not out and if not walk and if not HR and if not triple and if not double
    singleProb = 1

    singleProbFinal = (1-outProbFinal-walkProbFinal-HRProbFinal-tripleProbFinal-doubleProbFinal) * singleProb
     
##  determine outcome of PA
    roll = random.random()
    if roll <= outProbFinal:
        outcome = "out"
    elif roll > outProbFinal and roll <= (outProbFinal + walkProbFinal):
        outcome = "walk"
    elif roll > (outProbFinal + walkProbFinal) and roll <= (outProbFinal + walkProbFinal + HRProbFinal):
        outcome = "homerun"
    elif roll > (outProbFinal + walkProbFinal + HRProbFinal) and roll <= (outProbFinal + walkProbFinal + HRProbFinal + tripleProbFinal):
        outcome = "triple"
    elif roll > (outProbFinal + walkProbFinal + HRProbFinal + tripleProbFinal) and roll <= (outProbFinal + walkProbFinal + HRProbFinal + tripleProbFinal + doubleProbFinal):
        outcome = "double"
    else:
        outcome = "single"

    return outcome
    

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
            outcome = PAOutcome()
            if outcome == "out":
                a_outs = a_outs + 1
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
            outcome = PAOutcome()
            if outcome == "out":
                h_outs = h_outs + 1
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

def PAAgg(numPA):

    PA = 0
    outCount = 0
    walkCount = 0
    HRCount = 0
    tripleCount = 0
    doubleCount = 0
    singleCount = 0
    
    while PA <= numPA:
        outcome = PAOutcome()
        if outcome == "out":
            outCount = outCount + 1
        elif outcome == "walk":
            walkCount = walkCount + 1
        elif outcome == "homerun":
            HRCount = HRCount + 1
        elif outcome == "triple":
            tripleCount = tripleCount + 1
        elif outcome == "double":
            doubleCount = doubleCount + 1
        elif outcome == "single":
            singleCount = singleCount + 1
        PA = PA + 1

    outProp = outCount/(outCount + walkCount + HRCount + tripleCount + doubleCount + singleCount)
    walkProp = walkCount/(outCount + walkCount + HRCount + tripleCount + doubleCount + singleCount)
    HRProp = HRCount/(outCount + walkCount + HRCount + tripleCount + doubleCount + singleCount)
    tripleProp = tripleCount/(outCount + walkCount + HRCount + tripleCount + doubleCount + singleCount)
    doubleProp = doubleCount/(outCount + walkCount + HRCount + tripleCount + doubleCount + singleCount)
    singleProp = singleCount/(outCount + walkCount + HRCount + tripleCount + doubleCount + singleCount)

    return outProp,walkProp,HRProp,tripleProp,doubleProp,singleProp
