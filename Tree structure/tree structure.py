class Tree:
    def __init__(self, parent, *child):
        self.parent = parent
        self.child = child

    def print_tree(self):
        print(self.parent)
        for child in self.child:
            for branch in child:
                print("  " + branch.parent)
                for leaf in branch.child:
                    for i in leaf:
                        print("    " + i)


def build_tree():
    lap_childs = ["Mac", "HP", "Dell"]
    laptop = Tree("Laptop", lap_childs)

    ph_childs = ["Iphone", "Android"]
    phone = Tree("Phone", ph_childs)

    tv_childs = ["Panasonic", "LG"]
    tv = Tree("TV", tv_childs)

    child = [laptop, phone, tv]
    electronics = Tree("Electronics", child)
    electronics.print_tree()


build_tree()
