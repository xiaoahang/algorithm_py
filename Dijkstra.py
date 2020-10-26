import numpy


def dijstra(start: int, mgraph: np.ndarray) -> list:
    """
    docstring 
    :param start：the index of start point, start from 0
    :param mgraph：the neighbouring matrix
    :return a list of which is the distance form start to current
    """
    passed = [start]  # nodes that whos min distance is sure
    nopass = [x for x in range(len(mgraph)) if x != start]  # not sure

    dis = mgraph[start]  # results to be returned

    while len(nopass):
        idx = nopass[0]  # start from the 0 th in nopass
        for i in nopass:  # traverse nopass, find the min, move it form nopass to pased
            if dis[i] < dis[index]:
                idx = i
        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:  # 在剩下的点中，如果走折线更近，就更新dis start to i
            if dis[idx] + mgraph[idx][i] < dis[i]:
                dis[i] = dis[idx] + mgraph[idx][i]
    return dis
