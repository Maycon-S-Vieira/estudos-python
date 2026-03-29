import random

def main():
    matriz = [[random.randint(0, 255) for _ in range(10)] for _ in range(10)]
    print("Matriz 10x10:")
    for row in matriz:
        print(row)

if __name__ == "__main__":
    main()