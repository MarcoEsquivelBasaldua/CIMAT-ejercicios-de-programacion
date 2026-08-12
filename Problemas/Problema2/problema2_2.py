def getMinMax(freeSeats):
    seatRemoved = freeSeats - 1

    _min = seatRemoved // 2
    _max = seatRemoved - _min

    return _min, _max


N = 8
K = 8

continousFreeSeats = [N]


for k in range(1, K+1):
    maxIndex = continousFreeSeats.index(max(continousFreeSeats))

    #if (continousFreeSeats[maxIndex] == 1)

    _min, _max = getMinMax(continousFreeSeats[maxIndex])

    continousFreeSeats.pop(maxIndex)
    continousFreeSeats.append(_min)
    continousFreeSeats.append(_max)

    print("For K = ", k, ", the min and max are: ", _min, ", ", _max)