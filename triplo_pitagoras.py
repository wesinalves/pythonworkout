def main():
    a = 0
    b = 0
    hip = 0

    for l1 in range(1,21):
        for l2 in range(1,21):
            for h in range(1,21):
                if (l1 * l1 + l2 * l2) == (h * h):
                    print(f"l1: {l1}, l2: {l2}, h: {h}")
    
if __name__ == '__main__':
    main()


"""
l1: 3, l2: 4, h: 5
l1: 4, l2: 3, h: 5
l1: 5, l2: 12, h: 13
l1: 6, l2: 8, h: 10
l1: 8, l2: 6, h: 10
l1: 8, l2: 15, h: 17
l1: 9, l2: 12, h: 15
l1: 12, l2: 5, h: 13
l1: 12, l2: 9, h: 15
l1: 12, l2: 16, h: 20
l1: 15, l2: 8, h: 17
l1: 16, l2: 12, h: 20
"""