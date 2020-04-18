#while文

counter = 0
while counter < 10:
    counter += 1
    print(counter)

counter = 0
while True:
    counter += 1
    print(counter)
    if counter == 10:
        break

#break
for num in range(100):
    print(num)
    if num == 10:
        break