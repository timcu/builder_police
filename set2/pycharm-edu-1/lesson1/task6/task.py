from time import sleep
final_action = "blast off"
print("Countdown")
for counter in range(5, 0, -1):
    print(counter)
    sleep(1)
print(final_action)
