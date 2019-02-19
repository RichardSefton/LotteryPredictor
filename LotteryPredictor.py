import numpy as np
import pandas as pd
from Arrays import EuroMillionsArrays as ema
from Algorithms import EuroMillionsFreq as emf
from Algorithms import EuroMillionsCommons as emc

# import the dataset with pandas
dataset = pd.read_csv("CSV//EuroMillionsAll2Feb19.csv")

# arrays initialize
mainNumberSeq = ema.mainNumberSequence
luckyStarSeq = ema.luckyStarSequence

mainNumberFreq = ema.mainNumberFreq
luckyStarFreq = ema.luckyStarFreq

mainNumberOrderedFreq = ema.mainNumberOrdered
luckyStarOrderedFreq = ema.luckyStarOrdered

mainNumbersWeighted = ema.mainNumberWeighted
luckyStarWeighted = ema.luckyStarWeighted

mainNumberDrawHistory = ema.mainNumberDrawHistory
luckyStarDrawHistory = ema.luckyStarDrawHistory

mainNumberCommon = ema.mainNumberCommon
luckyStarCommon = ema.luckyStarCommon


# loop through the dataset
for index, row in dataset.iterrows():
    # get only the main numbers
    # print(index, row['N1'], row['N2'], row['N3'], row['N4'], row['N5'], row['L1'], row['L2'])
    n1, n2, n3, n4, n5 = row['N1'], row['N2'], row['N3'], row['N4'], row['N5']
    l1, l2 = row['L1'], row['L2']

    # write each line to the freq arrays
    mainNumberFreq = emf.main_number_freq(n1, n2, n3, n4, n5)
    luckyStarFreq = emf.lucky_number_freq(l1, l2)
    i = 0
    mainNumberCommon = n1, n2, n3, n4, n5
    luckyStarCommon = l1, l2
    # print(luckyStarCommon)
    # write each line to the draw history array
    mainNumberDrawHistory = np.append(mainNumberDrawHistory, np.array([[mainNumberCommon]]))
    luckyStarDrawHistory = np.append(luckyStarDrawHistory, np.array([[luckyStarCommon]]))

# reshape the mainnumberdrawhistory array
mainNumberDrawHistory = np.reshape(mainNumberDrawHistory, (-1,5))
luckyStarDrawHistory = np.reshape(luckyStarDrawHistory, (-1, 2))

print(luckyStarDrawHistory)
# run data through algorithms

# EuroMillions
# Frequency
mainNumberOrderedFreq = emf.sort_main_numbers()

# Sorted numbers
luckyStarOrderedFreq = emf.sort_lucky_stars()

# average freq
averageMain = emf.get_average_freq_main_numbers()
averageLuck = emf.get_average_freq_lucky_stars()

# weighted
mainNumberWeighted = emf.weight_main_numbers_freq(averageMain)
luckyStarWeighted = emf.weight_lucky_numbers_freq(averageLuck)

#get common doubles
mainNumberCommonDouble = emc.main_number_common_doubles(mainNumberDrawHistory)
luckyStarCommonDouble = emc.lucky_star_common_doubles(luckyStarDrawHistory)

# get common triplets
mainNumbersCommonTriple = emc.main_number_common_triplets(mainNumberDrawHistory)

# outputs
print("DRAW HISTORY")
print(mainNumberDrawHistory)

print("MAIN NUMBER FREQUENCY")
print(mainNumberSeq)
print(mainNumberFreq)

print("LUCKY STAR FREQ")
print(luckyStarSeq)
print(luckyStarFreq)

print("NUMBER FREQUENCY ORDERED LOW - HIGH")
print(mainNumberOrderedFreq)
print(luckyStarOrderedFreq)

print("THE AVERAGE FREQUENCYS ARE")
print(averageMain)
print(averageLuck)

print("COMMON NUMBER DOUBLE SETS")
print(mainNumberCommonDouble)
print(luckyStarCommonDouble)

print("COMMON NUMBER TRIPLE SETS")
print(mainNumbersCommonTriple)

print("THE MAIN BALLS WEIGHTS ARE")
print(mainNumberWeighted)

print("THE LUCKY STARS WEIGHTS ARE")
print(luckyStarWeighted)