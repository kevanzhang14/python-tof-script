import os

# absolute path of files
old_name1 = r"C:\Program Files\Tower Of Fantasy\Hotta\Content\Movies\HOTTA-LOGO.mp4"
new_name1 = r"C:\Program Files\Tower Of Fantasy\Hotta\Content\Movies\HOTTA-LOGO-noplay.mp4"

old_name2 = r"C:\Program Files\Tower Of Fantasy\Hotta\Content\Movies\TENCENT-LOGO.mp4"
new_name2 = r"C:\Program Files\Tower Of Fantasy\Hotta\Content\Movies\TENCENT-LOGO-noplay.mp4"



# check if filename1 exists
if os.path.isfile(new_name1):
    print("HOTTA-LOGO-noplay already esists")
else:
    # rename the file1
    os.rename(old_name1, new_name1)

# delete original file1
if os.path.exists(old_name1):
    os.remove(old_name1)
    print("HOTTO-LOGO has been deleted successfully")
else:
    print("HOTTO-LOGO does not exist!")



# check if filename2 exists
if os.path.isfile(new_name2):
    print("TENCENT-LOGO-noplay already esists")
else:
    # rename the file2
    os.rename(old_name2, new_name2)

# delete original file2
if os.path.exists(old_name2):
    os.remove(old_name2)
    print("TENCENT-LOGO has been deleted successfully")
else:
    print("TENCENT-LOGO does not exist!")
