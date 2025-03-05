
# tb_class_super.py

class A:
    def get_ver(self):
        return 0

class B(A):
    def get_ver(self):
        return 1

class C(B):
    def get_ver(self):
        return 2

    def get_b_ver(self):
        return super().get_ver()
    
    def get_a_ver(self):
        return super(B, self).get_ver()

c=C()
print(c.get_ver())
print(c.get_b_ver(), B.get_ver(c))
print(c.get_a_ver(), A.get_ver(c))

