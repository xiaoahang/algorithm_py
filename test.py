# # n = 3
# # m = 3
# # a = 0.5
# # b = 0.5

# # # p = [1]

# # # for i in range(1,m):
# # #     pm = [1]
# # #     for j in range(n):
# # #         if j == n:
# # #             pp = (1-pm[j-1]) * b**j
# # #         elif j == 0:
# # #             pp = pm[j-1] * (1-a)
# # #         else:
# # #             pp = (1-pm[j-1]) * b**j * (1-a)
# # #         pm.append(pp)
# # #     print(pm)
# # # #     p.append(p1)

# # # # print(sum(p))

# # p = [[]]


# # #隐马尔科链模型前向算法
# # def hmm_forward(A, PI, B, O):
# #     M = shape(PI)[0]   #观测序列大小
# #     N = shape(A)[1]    #状态序列大小
# #     T = M   
# #     alpha = mat(zeros((M, N)))
# #     P = 0.0

# #     for i in range(N):  
# #         alpha[0, i] = PI[i, 0] * B[i, 0]

# #     for t in range(T - 1):
# #         for i in range(N):
# #             temp_value = 0.0
# #             for j in range(N):
# #                 temp_value += alpha[t, j] * A[j, i]
# #             index = 0
# #             if(O[t + 1, 0] == 0):
# #                 index = 0
# #             else:
# #                 index = 1
# #             alpha[t + 1, i] = temp_value * B[i, index]  
# #     for i in range(N):
# #         P += alpha[T - 1, i]
# #     return P,alpha

# # a = 0.5
# # b = 0.5
# # pi = [1, 0, 0]
# # A = [[a, (1-a)*b, (1-a)*b*b],
# #     [(1-a)*b,ab+(1-a),a],
# #     [(1-a)*b*b],(1-a)b + a*b*b,(1-a)(1-b)]]


# # n = 2
# # m = 2
# # a = 0.5
# # b = 0.5
# # p=[1]
# # for i in range(1,m):
# #     pp = p[i-1] * (1-a) + (1-p[i-1]) * b
# #     p.append(pp)

# # print(sum(p))

# import numpy
# p=[[1,0,0]]
# pdzs = [1]

# n = 3
# m = 3
# a = 0.5
# b = 0.5

# for i in range(1,m):
#     p11 = a
#     p12 = (1-a) * b
#     p13 = 0
#     p21 = (1-a) * b
#     p22 = a * b + (1-a) * (1-b)
#     p23 = a * (1-b)
#     p31 = (1-a) * b * b
#     p32 = b
#     p33 = (1-b) * (1-b)

#     st = [[p11,p12,p13],[p21,p22,p23],[p31,p32,p33]]

#     pdz = p[i-1][0] * p11 + p[i-1][1] * p21 + p[i-1][2] * p31
#     pp = p[i-1] @ st[0]
#     print(pp)
#     pdzs.append(pdz)
