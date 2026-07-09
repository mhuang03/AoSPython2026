def c_to_f(temp_c):
    return 9/5*temp_c + 32

def f_to_c(temp_f):
    return (temp_f - 32) * 5/9



temps_c = [0, 20, 37, 100]
fahrenheit = []
for t in temps_c:
    fahrenheit.append(c_to_f(t))
print(fahrenheit)

celsius = []
for t in fahrenheit:
    celsius.append(f_to_c(t))
print(celsius)