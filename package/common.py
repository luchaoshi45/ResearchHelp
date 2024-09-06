import os

def out_dir_check(out_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
