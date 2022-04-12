class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None
    
class Lista:
    def __init__(self):
        self.prim = None
        

'''
crearea unei liste din valori citite pana la 0
'''
def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista

def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod


def copy_list(oldList):
    newList = Lista()
    oldNode = oldList.prim
    newList.prim = copy_list_rec(oldNode)
    return newList


def copy_list_rec(oldNode):
    if oldNode != None:
        newNode = Nod(oldNode.e)
        oldNode = oldNode.urm
        newNode.urm = copy_list_rec(oldNode)
        return newNode

'''
tiparirea elementelor unei liste
'''
def tipar(lista):
    tipar_rec(lista.prim)
    
def tipar_rec(nod):
    if nod != None:
        print(nod.e)
        tipar_rec(nod.urm)
        

'''
program pentru test
'''


def replace_element(list1, value, list2):
    list1.prim = replace_element_rec(list1.prim, None, value, list2)
    return list1


def replace_element_rec(node, prev_node, value, list2):
    if node is None:
        return None
    if node.e == value:
        nextValue = node.urm
        if list2.prim != None:
            newList = copy_list(list2)
            last_node = newList.prim
            while last_node.urm is not None:
                last_node = last_node.urm
            last_node.urm = nextValue
            if prev_node is not None:
                prev_node.urm = newList.prim
            replace_element_rec(nextValue, last_node, value, list2)
            return newList.prim
        else:
            prev_node.urm = nextValue
            replace_element_rec(nextValue, prev_node, value, list2)
    else:
        nextValue = node.urm
        replace_element_rec(nextValue, node, value, list2)
        return node


def find_element(list1, position):
    found_node = find_element_rec(list1.prim, position, 1)
    if found_node is None:
        print("The list does not have that many elements.")
    else:
        element = found_node.e
        print("The value of the node is: " + str(element))


def find_element_rec(node, position, current_position):
    if node is None:
        return None
    if position == current_position:
        return node
    else:
        node = node.urm
        find_element_rec(node, position, current_position+1)
        return node


def main():
    print("First list: ")
    list1 = creareLista()
    #tipar(list1)
    print("Second list: ")
    list2 = creareLista()
    #tipar(list2)

    find_element(list1, 3)

    replace_element(list1, 2, list2)

    print("The new first list: ")

    tipar(list1)

    
main()
