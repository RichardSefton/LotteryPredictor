import numpy as np
from Arrays import EuroMillionsArrays as ema

# define the arrays to be used
mainFreq = ema.mainNumberFreq
luckFreq = ema.luckyStarFreq
mainSeq = ema.mainNumberSequence
luckSeq = ema.luckyStarSequence
luckFreqWeight = ema.luckyStarWeighted
zippedMain = zip()
zippedLuck = zip()
mainWeights = ema.mainNumberWeighted


# set the frequency of the main numbers
def main_number_freq(n1, n2, n3, n4, n5):
    # increment the values in the array by one at each balls index (ballnum - 1)
    mainFreq[n1 - 1] = mainFreq[n1 - 1] + 1
    mainFreq[n2 - 1] = mainFreq[n2 - 1] + 1
    mainFreq[n3 - 1] = mainFreq[n3 - 1] + 1
    mainFreq[n4 - 1] = mainFreq[n4 - 1] + 1
    mainFreq[n5 - 1] = mainFreq[n5 - 1] + 1

    return mainFreq

# set the frequency of the lucky stars
def lucky_number_freq(l1, l2):
    # increment the values in the array by one at each balls index (ballnum - 1)
    luckFreq[l1 - 1] = luckFreq[l1 - 1] + 1
    luckFreq[l2 - 1] = luckFreq[l2 - 1] + 1

    return luckFreq

# zip the main numbers and write to array
def sort_main_numbers():
    # zip the pairs to show the numbers in sequence of most to least freq
    zippedPairsShowNumbers = zip(mainFreq, mainSeq)

    # sort the numbers into an array
    mainNumbersSequenceSorted = [x for _, x in sorted(zippedPairsShowNumbers)]

    # print the array of sorted numbers
    return mainNumbersSequenceSorted


def sort_lucky_stars():
    # zip the pairs to show the numbers in sequence of most to least freq
    zippedPairsShowNumbers = zip(luckFreq, luckSeq)

    # sort the numbers into an array
    luckyStarSequenceSorted = [x for _, x in sorted(zippedPairsShowNumbers)]

    return luckyStarSequenceSorted


# get the average of the main numbers freq
def get_average_freq_main_numbers():
    average = np.average(mainFreq)

    return average


#assign weights to the main numbers based on how far from average they are
def weight_main_numbers_freq(average):
    iterator = 0
    weightBracketDivider = 10
    while iterator < len(mainFreq):
        if mainFreq[iterator] < average:
            mainFreq[iterator] -= 1
        if mainFreq[iterator] > average:
            mainFreq[iterator] += 1
        # get the value at each array index and subtract the average
        valueForWeight = mainFreq[iterator] - average
        # print(valueForWeight)
        # divide by the weighted bracket amount
        weightedValue = valueForWeight / weightBracketDivider

        # write the ball weight to an array
        mainWeights[iterator] = weightedValue

        iterator += 1

    return mainWeights


# get the average of the lucky stars
def get_average_freq_lucky_stars():
    average = np.average(luckFreq)

    return average


# assign weights to the main numbers based on how far from average they are
def weight_lucky_numbers_freq(average):
    iterator = 0
    weightBracketDivider = 10
    luckFreqWeight = luckFreq
    while iterator < len(luckFreq):
        if luckFreq[iterator] < average:
            luckFreqWeight[iterator] -= 1
        if luckFreq[iterator] > average:
            luckFreqWeight[iterator] += 1

        # get the value at each array index and subtract the average
        valueForWeight = luckFreqWeight[iterator] - average
        #print(valueForWeight)
        # divide by the weighted bracket amount
        weightedValue = valueForWeight / weightBracketDivider

        # write the ball weight to an array
        luckFreqWeight[iterator] = weightedValue

        iterator += 1

    return luckFreqWeight

