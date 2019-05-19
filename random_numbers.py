import random

random.seed()
numbers = [random.randint(1,100)]

for i in range(100):
	numbers.append(random.randint(1,10))

print(numbers, len(numbers))

#if __name__ == "__main__":
#    import sys
#    
