def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b == 0: raise ValueError("Cannot divide by zero")
    return a/b

if __name__ == "__main__":
    print("Simple Calculator")
    op = input("Enter op (+ - * /): ").strip()
    a = float(input("a: "))
    b = float(input("b: "))
    if op == "+":
        print(add(a,b))
    elif op == "-":
        print(sub(a,b))
    elif op == "*":
        print(mul(a,b))
    elif op == "/":
        print(div(a,b))
    else:
        print("Unknown op")
