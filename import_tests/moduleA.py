import glob
class A ():
    def __init__(self, arg1,  arg2="kenneth", arg3="barth"):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

        print("inside A constructor")

    def print_args(self):
        print("Name: {} {} {}".format(self.arg1, self.arg2, self.arg3))
        return glob.glob("*.*")

#
# class B(A):
#     def __init__(self, arg1):
#         self.arg1 = arg1
#         print("inside B arg1 = {}".format(self.arg1))
#         self.print_args()
#
# a = A('scott','James', 'Barth')
# b = B('scott')



# for item in a.print_args():
#     print(item)
#
# b = ["1" + i for i in a.print_args()]