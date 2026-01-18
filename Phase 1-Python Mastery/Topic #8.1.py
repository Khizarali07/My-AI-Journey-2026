def weird_calculation():
    numbers = [10, 20, 30, 40, 50, 60, 70]
    current_sum = 0

    # Loop with an index 'i' and the 'number'
    for i, number in enumerate(numbers):
        # HIDDEN BUG: We are doing some weird math here
        if i % 2 == 0:
            current_sum += number
        else:
            current_sum -= number // 2

        # --- SET BREAKPOINT ON THE LINE BELOW ---
        print(f"Index: {i}, Current Sum: {current_sum}")

    return current_sum


final_result = weird_calculation()
print(f"Final: {final_result}")
