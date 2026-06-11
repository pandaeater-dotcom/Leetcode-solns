class ThroneInheritance:
    class Person:
        def __init__(self, name: str):
            self.name: str = name
            self.children: list[str] = []
            self.parent: Person = None
            self.is_alive: bool = True

    def __init__(self, kingName: str):
        self.king = self.Person(kingName)
        self.people = {kingName: self.king}
        
    def birth(self, parentName: str, childName: str) -> None:
        child = self.Person(childName)
        self.people[parentName].children.append(childName)
        self.people[childName] = child

    def death(self, name: str) -> None:
        self.people[name].is_alive = False

    def getInheritanceOrder(self) -> List[str]:
        preorder = []

        def _recursiveSuccessor(person: Person) -> None:
            nonlocal preorder
            if person.is_alive:
                preorder.append(person.name)
            for child in person.children:
                _recursiveSuccessor(self.people[child])
        _recursiveSuccessor(self.king)
        return preorder

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
