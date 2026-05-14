"""
Q12.
"""

def do_thing(i):
    return "*" * (2 * i)

def main():
    for i in range(5):
        print(do_thing(i))

if __name__ == '__main__':
    main()
