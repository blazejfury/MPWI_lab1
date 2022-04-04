def permute(input, answer, depth):
    if (depth == 0):
        print(answer)
        return

    for key, value in enumerate(input):
        left = input[0:key]
        right = input[key + 1:]
        rest = left + right
        permute(rest, answer + value, depth-1)


def main():
    input="1235"
    answer=""
    depth = 1
    permute(input, answer, depth)
    print(answer)

if __name__=="__main__":
    main()