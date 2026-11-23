
def count_by_extension(paths):
    extensions = {}
    for path in paths:
        if len(path.split('.')) >= 2:
            extension = path.split('.')[-1].lower()
        else:
            extension = ""
        extensions[extension] = extensions.get(extension, 0) + 1
    return extensions
    
def deepest_path(paths):
    mx = 0
    mxpath = ""
    for path in paths:
        if len(path.split('/')) > mx:
            mx = len(path.split('/'))
            mxpath = path
    return mxpath

def human_size(size):
    depth = 0
    s = size
    while s // 1024 != 0:
        depth += 1 
        s //= 1024
    depths = ["Б","КБ","МБ","ГБ", "ТБ"]
    return str(round(size / 1024 ** depth, 1)) + " " + depths[depth]

