"""calc43 - 一个简洁好用的命令行计算器
项目名: calc43_43 (学号后两位 43)
许可证: MIT License
"""

def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法，除数为 0 时抛出异常"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b

def main():
    print("欢迎使用 calc43 命令行计算器 (输入 q 退出)")
    while True:
        expr = input("calc43> ").strip()
        if expr.lower() == 'q':
            print("再见！")
            break
        try:
            # 只允许数字和四则运算符，保证安全
            if not all(c in '0123456789+-*/.() ' for c in expr):
                print("错误: 只支持数字和 + - * / 运算符")
                continue
            result = eval(expr)
            print(f"= {result}")
        except ZeroDivisionError:
            print("错误: 除数不能为 0")
        except Exception:
            print("错误: 表达式无法解析，请检查输入")

if __name__ == '__main__':
    main()
