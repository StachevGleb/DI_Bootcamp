# class Door():
#     def __init__(self, is_opened):
#         self.is_opened = is_opened
#     def open_door():
#         print("Door opening")
#     def close_door():
#         print("Door closing")
# class BlockedDoor(Door):
#     def open_door():
#         print("Blocked door cannot be opened")
#     def close_door():
#         print("Blocked door cannot be closed")


class A():

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis()