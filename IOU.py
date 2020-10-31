
import numpy


def IoU(a, b):
    """求两个矩形a和b的交并比

    Args:
        a (2*2 matrix): 矩形a，两行两列，一个是左上角的点，一个是右下角的点
        b (2*2 matrix): 矩形a，两行两列，一个是左上角的点，一个是右下角的点

    Returns:
        flost: 交集面积比并集面积
    """
    x_a1 = min(a[:][0])
    x_a2 = max(a[:][0])
    y_a1 = min(a[:][1])
    y_a2 = min(a[:][1])

    x_b1 = min(b[:][0])
    x_b2 = max(b[:][0])
    y_b1 = min(b[:][1])
    y_b2 = min(b[:][1])

    inter = (x_a2 - x_b1) * (y_a2 - y_b1)  # 交集面积
    union = (x_a2 - x_a1) * (y_a2-y_a1) + (x_b2 - x_b1) * \
        (y_b2-y_b1) - (x_a2 - x_b1) * (y_a2 - y_b1)  # 并集面积

    return inter / union


def NMS(rectangles, threshold, gt):
    """非极大值抑制的python实现

    Args:
        rectangles (tuple): 三元组，前两个元素是矩形两个顶点，第三个元素是类别sco
        threshold ([type]): [description]
        gt (list)): 真实值，矩形

    Returns:
        tuple: 返回最佳的长方形
    """
    rectangles_sorted = sorted(
        rectangles, key=lambda x: x[2], reverse=True)  # 按照那个类别分数先排个序，分高的排在前面

    for rec in rectangles_sorted:
        if IoU(rec, gt) >= threshold:
            return rec

    return None
