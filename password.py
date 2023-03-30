import random
passwordlen = int(input("Enter the Length of Password"))
X = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?<>/;"
Y = "".join(random.sample(X,passwordlen ))
print(Y)
