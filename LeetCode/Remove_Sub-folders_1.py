class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.in_list = False
        self.subfolders = dict()

    def add(self, name):
        if name not in self.subfolders.keys():
            self.subfolders[name] = Folder(name, self)
        return self.subfolders[name]

    def is_subfolder(self):
        if self.name == '':
            return False
        else:
            return self.parent.in_list or self.parent.is_subfolder


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        myfolder = [r.split('/')[1:] for r in folder]
        true_folder = []
        root = Folder('', None)
        for r in myfolder:
            parent = root
            for d in r:
                parent = parent.add(d)
            parent.in_list = True
            true_folder.append(parent)
        return [folder[i] for i, t in enumerate(true_folder) if not t.is_subfolder()]

