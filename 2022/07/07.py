
class Dir:
    """
    Dir is [String (listof File) (listof Dir)]
    interp. as: name is the name of the directory
                files is a list of files contained in the directory
                subdirs is a list of sub-directories contained in the directory
    """
    def __init__(self, name, parent):
        self.name = name
        self.files = {}
        self.subdirs = {}
        self.parent = parent
    
    def add_file(self, file):
        self.files[file.name] = file

    def add_subdir(self, subdir):
        self.subdirs[subdir.name] = subdir

    def __str__(self):
        to_print = str(self.name)
        to_print += "\n"
        for subdir in self.subdirs.values():
            to_print += subdir.__str__()
            to_print += "\n"
        for file in self.files.values():
            to_print += file.__str__()
            to_print += "\n"
        return to_print

    def get_size(self):
        total_file_size = 0
        for file in self.files.values():
            total_file_size += file.size
        total_subdir_size = 0
        for subdir in self.subdirs.values():
            total_subdir_size += subdir.get_size()
        return total_file_size + total_subdir_size

    def get_total_size_upto(self, threshold):
        total_size_upto = 0
        current_size = self.get_size()
        if current_size <= threshold:
            total_size_upto += current_size
        for subdir in self.subdirs.values():
            total_size_upto += subdir.get_total_size_upto(threshold)
        return total_size_upto

    def get_size_of_dir_to_delete(self, threshold, smallest_so_far):
        for subdir in self.subdirs.values():
            subdir_size = subdir.get_size()
            if threshold < subdir_size < smallest_so_far:
                smallest_so_far = subdir_size
            subdir_smallest_so_far = subdir.get_size_of_dir_to_delete(threshold, smallest_so_far)
            if subdir_smallest_so_far < smallest_so_far:
                smallest_so_far = subdir_smallest_so_far
        return smallest_so_far

class File:
    """
    File is [String Int]
    interp. as: name is the name of the file
                size is the size of the file
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return (str(self.size) + " " + str(self.name))

lines = []
with open("input.txt", "r") as file:
    lines = file.readlines()[:-1]

fs = Dir(None, None)
fs.add_subdir(Dir("/", fs))
current_dir = fs
i = 0
while i < len(lines):
    if lines[i][0] == "$":
        if lines[i][2:4] == "cd":
            if lines[i][5:7] == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.subdirs[lines[i][5:].strip()]
            i += 1
        elif lines[i][2:4] == "ls":
            i += 1
            while i < len(lines) and lines[i][0] != "$":
                words = lines[i].split()
                if words[0] == "dir":
                    current_dir.add_subdir(Dir(words[1], current_dir))
                else:
                    current_dir.add_file(File(words[1], int(words[0])))
                i += 1

print(fs.get_total_size_upto(100000))
print(fs.get_size())
delete_threshold = 30000000 - (70000000 - fs.get_size())
print(fs.get_size_of_dir_to_delete(delete_threshold, fs.get_size()))