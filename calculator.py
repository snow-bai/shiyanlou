# 原始收入，获取用户输入，转换为 int

# 税后收入
salary = 0
# 应纳税所得额
shouldPay = 0
# 纳税金额
tax = 0

def calculator(income):
    shouldPay = income-5000
    if income < 5000:
        salary = income
        print('你的税后薪资是：{:.2f}'.format(salary))
    if shouldPay < 3000:
        tax = shouldPay * 0.03 - 0
        salary = income - tax
        print('你的税后薪资是：{:.2f}'.format(salary))
    if shouldPay >3000 and shouldPay <12000:
        tax = shouldPay*0.1-210
        salary = income - tax
        print('你的税后薪资是：{:.2f}'.format(salary))
    if shouldPay >12000 and shouldPay <25000:
        tax = shouldPay*0.2-1410
        salary = income - tax
        print('你的税后薪资是：{:.2f}'.format(salary))
    if shouldPay >25000 and shouldPay <35000:
        tax = shouldPay*0.25-2660
        salary = income - tax
        print('你的税后薪资是：{:.2f}'.format(salary))
    if shouldPay >35000 and shouldPay <55000:
        tax = shouldPay*0.3-4410
        salary = income - tax
        print('你的税后薪资是：{:.2f}'.format(salary))
    if shouldPay >55000 and shouldPay <85000:
        tax = shouldPay*0.35-7170
        salary = income - tax
        print('你的税后薪资是：{:.2f}'.format(salary))
    if shouldPay >80000:
        tax = shouldPay*0.45-15160
        salary = income - tax
        print('你的税后薪资是：{:.2f}'.format(salary))

if __name__ == '__main__':
     s = int(input('请输入你的工资：'))
     calculator(s)