
period = int(input())

doctors = 7
treated_patient = 0
untreated_patient = 0

for day in range(1, period + 1):
    if day % 3 == 0 and untreated_patient > treated_patient:
        doctors += 1
    current_patient = int(input())

    if current_patient <= doctors:
        treated_patient += current_patient
    else:
        treated_patient += doctors
        untreated_patient += (current_patient - doctors)

print(f"Treated patients: {treated_patient}.")
print(f"Untreated patients: {abs(untreated_patient)}.")

