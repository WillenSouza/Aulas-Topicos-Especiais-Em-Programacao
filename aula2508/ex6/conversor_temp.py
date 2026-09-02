def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def converter():
    print("Conversor de Temperatura")
    print("1. Celsius -> Fahrenheit")
    print("2. Celsius -> Kelvin")
    print("3. Fahrenheit -> Celsius")
    print("4. Fahrenheit -> Kelvin")
    print("5. Kelvin -> Celsius")
    print("6. Kelvin -> Fahrenheit")

    escolha = input("Escolha (1-6): ")

    try:
        valor = float(input("Digite a temperatura: "))
    except ValueError:
        print("Valor inválido!")
        return

    if escolha == "1":
        print(f"{valor}°C = {celsius_para_fahrenheit(valor):.2f}°F")
    elif escolha == "2":
        print(f"{valor}°C = {celsius_para_kelvin(valor):.2f}K")
    elif escolha == "3":
        print(f"{valor}°F = {fahrenheit_para_celsius(valor):.2f}°C")
    elif escolha == "4":
        print(f"{valor}°F = {fahrenheit_para_kelvin(valor):.2f}K")
    elif escolha == "5":
        print(f"{valor}K = {kelvin_para_celsius(valor):.2f}°C")
    elif escolha == "6":
        print(f"{valor}K = {kelvin_para_fahrenheit(valor):.2f}°F")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    converter()