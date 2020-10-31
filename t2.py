#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。

(N, M, T, P) = (10, 4, 3, 3)
s = 'fnfnfnffxfnnnnn'


def warn_predict(N, M, T, P, s):
    warn = []
    s = list(s)

    flag = 1
    l = len(s)
    # for i in range(l):

    i = 0
    while i < l:
        if i < l:
            # 未知态
            if s[i] =='x' and i >0:
                flag = warn[i-1]
                s.pop(i)
                l -=1
                i -=1
            else:
                if i < N:
                    flag = 0
                elif sum_state(s[i-N:i],'f') == N:
                    flag = 1

                if i < M and sum_state(s[:i],'f') >=T:
                    flag = 1
                elif sum_state(s[i-M:i],'f') >=T:
                    flag = 1
                
                if i >= P and sum(warn[i-P:i]) == P:
                    flag = 0
            
        warn.append(flag)
        i = i+1

    print(s)
    print(warn)

    return sum(warn)

def sum_state(state_arr,state):
    re = 0
    for i in state_arr:
        if i == state:
            re+=1
    return re

re = warn_predict(N, M, T, P, s)
print(re)
