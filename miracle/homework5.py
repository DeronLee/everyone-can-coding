# 输入一个数字n
# 判断它的奇偶性
 
def number_deal(a):
    # 判断x是否为偶数
    if a % 2 == 0:
        # 返回“it's an even"
        return "it's an even" 
    #返回“it's an odd"
    return "it's an odd"

a=5
print number_deal(5)
