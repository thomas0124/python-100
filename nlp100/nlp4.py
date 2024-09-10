txt = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
txt = txt.replace(".", "")

lst = txt.split()

print(lst)

lst = [lst[i][:1] if i in [0, 4, 5, 6, 7, 8, 14, 15, 18] else lst[i][:2] for i in range(len(lst))]

print(lst)