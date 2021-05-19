import os
import os.path
import shutil

shutil.copytree("../../../Desktop/module2/tests", "tests/tests")

for current_dir, dirs, files in os.walk("../../../Desktop/module2"):
    print(current_dir, dirs, files)