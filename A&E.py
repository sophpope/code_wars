def patients_waiting(times):
    times.sort()
    total_wait = 0
    for i in range(0, len(times)):
        total_wait += sum(times[:i])
    return total_wait
    

print(patients_waiting([5, 1, 4]))