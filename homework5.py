immutable_var=(3,5,"apple".upper(), False)
print(immutable_var)
print(type(immutable_var))
#immutable_var[2]=("coconut") кортеж неизменяемый тип данных
mutable_list=[2,6,"banana", True]
print(mutable_list)
print(type(mutable_list))
mutable_list[2]="coconut"
print(mutable_list)