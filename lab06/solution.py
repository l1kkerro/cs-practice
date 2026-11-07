
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
    for path in paths:
        if len(path.split('/')) > mx:
            mx = len(path.split('/'))
            mxpath = path
    return mxpath

    
    
    
paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

print(count_by_extension(paths))   # {"pdf": 1, "txt": 1, "png": 1, "": 1}
print(deepest_path(paths))         # "docs/img/logo.png"

# human_size(900)             # "900 Б"
# human_size(1536)            # "1.5 КБ"
# human_size(5 * 1024 * 1024) # "5.0 МБ"