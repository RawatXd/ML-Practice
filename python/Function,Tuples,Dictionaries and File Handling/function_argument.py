def sum_all(*args):
    total = 0
    for num in args:
        total+=num
    return total

total = sum_all(1,2,3,4,5,6)
print(total)

def company_info(**kwargs):
    for key in kwargs:
        print(key , kwargs[key])

company_info(ticker = "AAPL",ceo = "Tim Cook",revenue = "100 billion")
