def brainfuck_interpreter(code):
    memory = [0] * 30000  # 30,000 memory cells as specified by the original Brainfuck specification
    pointer = 0  # Current memory cell pointer
    output = ""

    # Remove all characters from the code that are not Brainfuck commands
    code = ''.join(c for c in code if c in ['>', '<', '+', '-', '.', ',', '[', ']'])
    code_length = len(code)
    code_index = 0

    bracket_stack = []  # Stack to keep track of matching brackets

    while code_index < code_length:
        command = code[code_index]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '.':
            output += chr(memory[pointer])
        elif command == ',':
            # Read input from the user (character by character)
            input_char = input("Enter a single character: ")
            if len(input_char) > 0:
                memory[pointer] = ord(input_char[0])
        elif command == '[':
            if memory[pointer] == 0:
                # Find the matching closing bracket
                bracket_count = 1
                while bracket_count > 0:
                    code_index += 1
                    if code[code_index] == '[':
                        bracket_count += 1
                    elif code[code_index] == ']':
                        bracket_count -= 1
            else:
                bracket_stack.append(code_index)
        elif command == ']':
            if memory[pointer] != 0:
                code_index = bracket_stack[-1] - 1
            else:
                bracket_stack.pop()

        code_index += 1

    return output

if __name__ == "__main__":
    print("Brainfuck Interpreter (Type 'exit' to quit)")

    while True:
        user_input = input(">>> ")

        if user_input.lower() == "exit":
            print("Qutting... thanks for using!")
            break

        result = brainfuck_interpreter(user_input)
        print(result)