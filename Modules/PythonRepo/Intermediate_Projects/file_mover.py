import os
import shutil
import textwrap


class UserFilePath:
    bookmarks: dict = {}
    bookmark_flag: bool = None

    def __init__(self, directory=str(), name=str(), extension=str(), index_num=int(), alias=str()):
        self.directory = directory
        self.name = name
        self.extension = extension
        self.index_num = index_num
        self.alias = alias

        UserFilePath.bookmarks.update({self.index_num: self.directory})

    def get_directory(self):
        return self.directory

    def get_name(self):
        return self.name

    def get_extension(self):
        return self.extension

    def get_index_num(self):
        return self.index_num

    def character_removal(self):
        removed_chars = ("/", "\\", "\"", "\'")

        if self.directory.startswith(removed_chars):
            self.directory = self.directory[1:]
        if self.directory.endswith(removed_chars) and 3 >= len(self.directory):
            self.directory = self.directory[:-1]
        if self.name.startswith(removed_chars):
            self.name = self.name[1:]
        if self.name.endswith(removed_chars):
            self.name = self.name[:-1]

    @classmethod
    def instantiate_from_file(cls):
        current_directory = os.getcwd()
        directories_file = f"{current_directory}/directories.txt"
        if os.path.isfile(directories_file) is False:
            open(directories_file, "x").close()

        with open(directories_file, "r") as f:
            directories = dict(enumerate(line.strip() for line in f))

        for k, v in directories.items():
            UserFilePath(
                        directory = v,
                        index_num = k,
                        )

    @classmethod
    def save_instances_to_file(cls):
        current_directory = os.getcwd()
        with open(f"{current_directory}/directories.txt", "w") as f:
            for item in UserFilePath.bookmarks.values():
                f.write("%s\n" % item)

    @classmethod
    def save_to_bookmarks(cls, *new_bookmark):
        UserFilePath.bookmarks.update({len(UserFilePath.bookmarks.keys()) + 1: new_bookmark})

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.index_num}', {self.directory})"


def bookmark_selection():
    UserFilePath.instantiate_from_file()
    UserFilePath.bookmark_flag = False

    if len(UserFilePath.bookmarks.items()) <= 1:
        print("There aren't any directories bookmarked.")
        return "/"
    else:
        print("These are previously bookmarked directories:")
        index_list = []

        for index, directory in UserFilePath.bookmarks.items():
            print(f"| {index} | {directory} |")
            index_list.append(index)

        bookmark_index = input("\nInput a bookmark's corresponding index number: ")

        while bookmark_index.isdigit() is False:
            bookmark_index = input("\tThe bookmark index must be a number: ")

        return UserFilePath.bookmarks.get(int(bookmark_index))
# TODO: Complete bookmark functionality.
# TODO: Fix bookmark index validation.
def src_file_path():
    src_file = UserFilePath()

    if UserFilePath.bookmark_flag:
        src_file.directory = bookmark_selection()
    else:
        print("Tell me where the source file lives...")
        src_file.directory = input("\tSource directory: ")

    src_file.character_removal()

    while os.path.isdir(src_file.directory.casefold()) is False:
        print("\nPlease, tell me where the source file lives: ")
        src_file.directory = input("\tSource directory: ")
        src_file.character_removal()

    return src_file


def src_file_name(src_file):
    print("Tell me the name of the source file...")
    src_file.name = input("\tSource file name: ")

    while os.path.isfile(f"{src_file.directory}/{src_file.name}".casefold()) is False:
        print("\nNo such file exists in this directory. Tell me the name of the source file:")
        src_file.name = input("\tSource file name: ")
        src_file.character_removal()

    src_file.name, src_file.extension = os.path.splitext(src_file.name)
    UserFilePath.bookmark_flag = False
    return src_file


def dest_file_path(src_file):
    dest_path = UserFilePath()

    if UserFilePath.bookmark_flag:
        dest_path.directory = bookmark_selection()
    else:
        print("Give the file a new home...")
        dest_path.directory = input("\tDestination directory: ")

    dest_path.character_removal()

    while os.path.isdir(dest_path.directory.casefold()) is False:
        print("\nPlease, give me a valid destination:")
        dest_path.directory = input("\tNew destination: ")
        dest_path.character_removal()

    print("\nWould you like to rename the resulting file?")

    if (rename_file := input("\tY/N: ").casefold()) == "y":
        print("Give the resulting file a new name...")
        rename_file = input("\tNew file name: ")
        dest_path.name = rename_file
        dest_path.name, dest_path.extension = os.path.splitext(dest_path.name)
        dest_path.character_removal()
    elif rename_file.casefold() == "n":
        dest_path.name = src_file.name
        dest_path.extension = src_file.extension
    else:
        print("...Opting not to rename file...\n")

    return dest_path


def move_file(src_file, dest_path):
    print(textwrap.dedent(f"""
        Confirm whether I should move:
        | {src_file.name}{src_file.extension} | 
        from: 
        | {src_file.directory} |
        to: 
        | {dest_path.directory} | 
        with the resulting name: 
        | {dest_path.name}{dest_path.extension} |
        
        NOTE: 
        If a file named {dest_path.name}{dest_path.extension} exists in {dest_path.directory}, it will be replaced.
                        """))

    if (confirm_move := input("Y/N: ").casefold()) == "y":
        final_src_path = f"{src_file.directory}/{src_file.name}{src_file.extension}"
        final_dest_path = f"{dest_path.directory}/{dest_path.name}{dest_path.extension}"
        shutil.move(final_src_path, final_dest_path)
        print("File moved successfully!")
    elif confirm_move.casefold() == "n":
        print("Aborting as directed.")
    else:
        print("Indecisiveness detected! Aborting operation.")


# noinspection PyUnusedLocal
def main():
    print("Would you like to use a bookmark as a source directory?")

    if (bookmark_choice := input("\tY/N: ").casefold()) == "y":
        UserFilePath.bookmark_flag = True
    else:
        print("Continuing to choose custom source directory...\n")

    src_file_name(source_file := src_file_path())
    print("Would you like to use a bookmark as a destination directory?")

    if (bookmark_choice := input("\tY/N: ").casefold()) == "y":
        UserFilePath.bookmark_flag = True
    else:
        print("Continuing to choose custom destination directory...\n")

    destination_file = dest_file_path(source_file)
    move_file(source_file, destination_file)

    print("Would you like to save the source directory, the destination directory, or both, as a bookmark?")

    if bm_add := "source" in input(f"\t'Source'/'Dest'/'Both': ").casefold():
        UserFilePath.save_to_bookmarks(source_file.directory)
    elif bm_add == "dest":
        UserFilePath.save_to_bookmarks(destination_file.directory)
    elif bm_add == "dest":
        UserFilePath.save_to_bookmarks(source_file.directory, destination_file.directory)

    UserFilePath.save_instances_to_file()


main()




# directory_list = []
# for item in UserFilePath.all:
#     directory_list.append(item)


# source_file = src_file_path()
# destination_file = dest_file_path(source_file)
# move_file(source_file, destination_file)
