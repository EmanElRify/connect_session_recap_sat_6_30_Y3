# Example 1
# text = "Python-Programming"
# result = text[::2] + "-" + text[7:11]
# print(result)
#Pto-rgamn-Prog
#pto-rogrmmng-ming
#Pyt_prog
#pto-rogram
#Pto-rgamn-Prog
#Pto-rgamn-Prog


# Example 2
x = 10
y = "20"
output = str(x) + y[0] + y[1] + str(int(y) + x)
print(output)
#"1020" + "30"  = "102030"



# # # Example 3
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = data[1:9:2] + [data[0]] + [data[-1]]
print(res)
#[2, 4, 6, 8] + [1] + [10] = [2, 4, 6, 8, 1, 10]
