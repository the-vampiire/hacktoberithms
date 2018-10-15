def checkout_time(customer_times, registers):
    time_elapsed = 0

    # each register takes the first customer in line
    registers = [customer_times.pop(0) for x in range(registers)]

    # while there is a line and all registers are not done
    while any(register > 0 for register in registers):
        # increment time
        time_elapsed += 1

        # for each register
        for x in range(0, len(registers)):
            # decrease customer times
            registers[x] -= 1

            # take the next customer in line
            if registers[x] == 0:
                if customer_times:
                    registers[x] = customer_times.pop(0)

                else:
                    registers[x] = 0

    return time_elapsed


if __name__ == "__main__":
    print(checkout_time([5, 1, 3], 1))
    print(checkout_time([10, 3, 4, 2], 2))
