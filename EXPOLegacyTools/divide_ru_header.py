def split_file_to_ruheader_body(file, buffer_size=512):
    header = bytes()
    body = bytes()

    with open(file, 'rb') as f:
        while True:
            buffer = f.read(buffer_size)

            if not buffer:
                break

            magic_idx = buffer.find(b'\x04\x1a')  # from b'\x04\x1a'
            if magic_idx >= 0:
                header += buffer[:(magic_idx + 2)]
                body = buffer[(magic_idx + 2):] + f.read()

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
    return header, body

if __name__ == '__main__':
    # file_path = "some/where/grib/file/path"
    file_path = "./20191017_000000.000"
    
    grib_header, grib_body = split_file_to_ruheader_body(file_path) 

    print(grib_body)
