from opps_project import chatbook


g=chatbook()


# print(g.name)

print(g.get_name())
g.set_name("harshit")

print(g.get_name())





from opps import Emp

H = Emp()
print(H.user)
# print(H._Emp__name)

# print(H.user)


G=Emp()
print(G.user)

L=Emp()

print(L.user)


#  ^print("after static method")

# G=Emp()
# j=Emp()
# l=Emp()

# print(G.id)
# print(j.id)
# print(l.id)

#! static method with getter and setter
G=Emp()

print(G.id)

Emp.set_method(50)

K=Emp()

print(K.id)
