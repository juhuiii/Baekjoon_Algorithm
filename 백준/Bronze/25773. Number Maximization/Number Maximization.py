def number_maximization(number):
    number_list = list(number)
    
    max_num = sorted(number_list, reverse=True)
    
    return "".join(max_num)


if __name__ == "__main__":
    number = input()
    
    print(number_maximization(number=number))