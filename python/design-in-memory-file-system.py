class Node:
    def __init__(self, name: str, is_dir: bool):
        self.name = name
        self.is_dir = is_dir
        self.children = []
        self.content = ""

class FileSystem:

    def __init__(self):
        self.fs = Node("", True)

    def ls(self, path: str) -> List[str]:
        res = []
        def recursiveLS(rem: list[str], cursor: Node):
            nonlocal res
            if not rem:
                if cursor.is_dir:
                    res = sorted([child.name for child in cursor.children])
                else:
                    res = [cursor.name]
                return
            for child in cursor.children:
                if child.name == rem[0]:
                    rem.pop(0)
                    recursiveLS(rem, child)
                    return
        if path == "/":
            return sorted([child.name for child in self.fs.children])
        lst = path.split("/")
        lst.pop(0)
        recursiveLS(lst, self.fs)
        return res
    
    def mkdir(self, path: str) -> None:
        def recursiveMk(rem: list[str], cursor: Node):
            if not rem:
                return
            for child in cursor.children:
                if child.name == rem[0] and child.is_dir:
                    rem.pop(0)
                    recursiveMk(rem, child)
                    return
            newChild = Node(rem[0], True)
            cursor.children.append(newChild)
            rem.pop(0)
            recursiveMk(rem, newChild)
        lst = path.split("/")
        lst.pop(0)
        recursiveMk(lst, self.fs)

    def addContentToFile(self, filePath: str, content: str) -> None:
        def recursiveAdd(rem: list[str], cursor: Node):
            if not rem:
                if not cursor.is_dir:
                    cursor.content += content
                return
            for child in cursor.children:
                if child.name == rem[0]:
                    rem.pop(0)
                    recursiveAdd(rem, child)
                    return
            newFile = Node(rem.pop(), False)
            cursor.children.append(newFile)
            recursiveAdd(rem, newFile)
        lst = filePath.split("/")
        lst.pop(0)
        recursiveAdd(lst, self.fs)

    def readContentFromFile(self, filePath: str) -> str:
        content = ""
        def recursiveRead(rem: list[str], cursor: Node):
            nonlocal content
            if not rem:
                if not cursor.is_dir:
                    content = cursor.content
                return
            for child in cursor.children:
                if child.name == rem[0]:
                    rem.pop(0)
                    recursiveRead(rem, child)
                    return
        lst = filePath.split("/")
        lst.pop(0)
        recursiveRead(lst, self.fs)
        return content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
