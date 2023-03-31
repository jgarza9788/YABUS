        dest = row["fullpath_x"].replace(row["rootpath_x"], row["rootpath_y"])
        pathlib.Path('\\'.join(dest.split('\\')[:-1])).mkdir(parents=True, exist_ok=True)

        cmd = f'copy \"{row["fullpath_x"]}\" \"{dest}\" {row["options"]} '
        print(cmd)
        # os.system(cmd)
        sp.run(cmd)