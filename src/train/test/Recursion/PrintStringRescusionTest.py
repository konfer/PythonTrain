#coding:utf-8

tree=[[[['human','chimpanzee'],'gorilla'],'orange-utan'],'gibbon']

def print_species(tree):
    
    for child in tree:
        if type(child)==list:
            print_species(child)
        else:
            print child

print_species(tree)