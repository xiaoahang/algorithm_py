def IOU(a,b):
    x_a1 = min(a[:][0])
    x_a2 = max(a[:][0])
    y_a1 = min(a[:][1])
    y_a2 = min(a[:][1])

    x_b1 = min(b[:][0])
    x_b2 = max(b[:][0])
    y_b1 = min(b[:][1])
    y_b2 = min(b[:][1])


    inter = ( x_a2 - x_b1) * (y_a2 - y_b1)
    union  = (x_a2 - x_a1) * (y_a2-y_a1) + (x_b2 - x_b1) * (y_b2-y_b1) - ( x_a2 - x_b1) * (y_a2 - y_b1)    

    return inter / union