filename = "motto.txt"
file_handle = open(filename, 'w')
file_handle.write("Fiat Lux!\n")
file_handle.close()


file_handle = open(filename, 'r')
print(file_handle.read())
file_handle.close()

file_handle = open(filename, 'w')
file_handle.write("\nLet there be light!")
file_handle.close()


file_handle = open(filename, 'r')
print(file_handle.read())
file_handle.close()