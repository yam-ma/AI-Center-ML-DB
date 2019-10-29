##
## dump_by_grib_mesg: 武藤さん作。gribファイルを、EXPO Legacy形式に分割する。
##                    Oct. 18. 2019
##

import os
import pygrib

def get_ru_header_binary(file, buffer_size=512):
    header = bytes()
    with open(file, 'rb') as f:
        while True:
            buffer = f.read(buffer_size)
            if not buffer:
                break
            magic_idx = buffer.find(b'\x04\x1a')  # from b'\x04\x1a'
            if magic_idx >= 0:
                header += buffer[:(magic_idx + 2)]
                break
            elif buffer[(buffer_size - 1):buffer_size] == b'\x04':
                header += buffer
                temp = f.read(1)
                if temp == b'\x1a':
                    header += temp
                    break
                else:
                    f.seek(f.tell() - 1)
            else:
                header += buffer
    return header

if __name__ == '__main__':
    ## set some variables
    grib_full_path = "some/where/grib/file/path"
    grib_full_path = "/home/ai-corner/part1/MSM/surface/bt00/vt0015/20191010_000000.000/20191010_000000.000"
    grib_file_name = os.path.basename(grib_full_path)
    # dumped_base_file_path = "some/where/dump/grib/file/base/path"
    dumped_base_file_path = "."

    ## get ru_header binary
    binary_ru = get_ru_header_binary(grib_full_path)

    ## open grib file and dump with ru_header
    gribs = pygrib.open(grib_full_path)
    for i, grib in enumerate(gribs):
        ## dump 1 grib msg in the local
        dumped_file_path = dumped_base_file_path + "/" + grib_file_name + "." + str(i+1)
        print(dumped_file_path)
        with open(dumped_file_path,'wb') as f:
            f.write(binary_ru)
            f.write(grib.tostring())
