import numpy as np

# array for main number frequency
mainNumberFreq = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# array for main number sequence
mainNumberSequence = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                               21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                               31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                               41, 42, 43, 44, 45, 46, 46, 48, 49, 50])

# array for lucky star frequency
luckyStarFreq = np.array([0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0])

# array for lucky star sequence
luckyStarSequence = np.array([1, 2, 3, 4, 5, 6,
                              7, 8, 9, 10, 11, 12])

# array for ordered main numbers (from zip)
mainNumberOrdered = np.array([])

# array for ordered lucky stars (from zip)
luckyStarOrdered = np.array([])


# arrays for accumulating weights to the numbers
mainNumberWeighted = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype='f')

luckyStarWeighted = np.array([0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0], dtype='f')

# arrays for ordered accumulated weights (from zip)
mainNumberOrderedWeighted = np.array([], dtype='f')
luckyStarOrderedWeighted = np.array([], dtype='f')

# array for finding common values
mainNumberCommon = np.array([0, 0, 0, 0, 0])
luckyStarCommon = np.array([0, 0])

#draw history
mainNumberDrawHistory = np.empty([0, 5], int)
luckyStarDrawHistory = np.empty([0, 2], int)