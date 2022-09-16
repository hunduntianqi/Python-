import os

path = r'D:\Users\Administrator\IdeaProjects\Python\python_爬虫\2022_2_13_小说抓取\文学作品'
list_dir = os.listdir(path)
for dir in list_dir:
    print(dir)
    path_type = path + '\\{}'.format(dir)
    list_type = os.listdir(path_type)
    for book in list_type:
        print(book)
        book_dir_path = path_type + '\\{}'.format(book)
        if os.path.exists(book_dir_path):
            list_file = os.listdir(book_dir_path)
            for file_path in list_file:
                print(file_path)
                if 'txt' in file_path:
                    if os.path.getsize(book_dir_path + '\\{}'.format(file_path)) <= 256:
                        os.remove(book_dir_path + '\\{}'.format(file_path))
            if len(list_file) != 3:
                for file in list_file:
                    os.remove(book_dir_path + '\\{}'.format(file))
                os.rmdir(book_dir_path)

