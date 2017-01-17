"""file's operation collection
"""
import os

def remove_duplicate(fileA, fileB, dest=None):
    """Remove the element from fileB in FileA
       Return a new fileC
       @param fileA: file that is to remove duplicate
       @param fileB: where the fileA remove from
       @return file: new file that is removed
    """
    fileA_content = []
    fileB_content = []

    with open(fileA, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            fileA_content.append(line)

    with open(fileB, 'r') as fh:
        for line in fh:
            line = line.replace('\n', '')
            fileB_content.append(line)

    original_size = len(fileA_content)
    print("{0}中有{1}条记录， {2}中有{3}条记录".format(fileA, original_size, fileB, len(fileB_content)))

    for content in fileB_content:
        if content in fileA_content:
            fileA_content.remove(content)

    print("删除了{0}条记录".format(original_size-len(fileA_content)))

    if dest:
        filepath = dest + 'merged1.txt'
    else:
        filepath = 'merged1.txt'

    with open(filepath, 'w') as fd:
        for content in fileA_content:
            fd.write(content+'\n')

    if dest:
        print("去重记录已保存在{0}".format(filepath))
    print("去重记录已保存在{0}".format(os.getcwd()+'\\'+filepath))

def main():
    """Main function
    """
    remove_duplicate('merged.txt', 'usedUrls.txt')

if __name__ == '__main__':
    main()


