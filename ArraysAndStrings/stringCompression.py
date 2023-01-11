from io import StringIO

# My implementation


def stringCompress(string):

    if len(string) < 1:
        return ''

    curr_char = string[0]
    curr_count = 0
    compress_list = []

    for ch in string:

        if ch != curr_char:
            compress_list.append(curr_char)
            compress_list.append(str(curr_count))
            curr_char = ch
            curr_count = 1

        else:
            curr_count += 1

    compress_list.append(curr_char)
    compress_list.append(str(curr_count))

    compress_str = ''.join(compress_list)

    if len(string) <= len(compress_str):
        return string

    return compress_str


# ChatGPT's suggestion
# New tech: StringIO
"""
StringIO allows you to work with string input and output as if it were a file.
It is useful when you need to work with text-based IO streams, but you don't want to do it
using plain strings or file operations. 

It uses in-memory instead of disk, which is generally faster but it may not be as efficient 
with large files. Additionally, if the program crashes, memory storage would be lost but not disk.

Since we use the entire file at once in the end, memory is faster. But if we read the file multiple
times or read only a part of the file, disk may be more efficient.

> write(string): Writes the given string to the in-memory buffer
> writelines(lines): Writes a list of strings to the in-memory buffer
> read([size]): Reads up to the specified number of chars from the in-memory buffer and returns them as string
> readline(): Reads and returns the next line of the buffer as string
> readlines(): Reads and returns a list of all lines in the buffer
> seek(offset): Change the curr pos of buffer to specified offset
> tell(): Return curr pos of buffer
> truncate([size]): Truncate buffer to specificed number of chars
> getvalue(): Return entire contents of buffer as a string
> close(): Close the IO stream

"""


def stringCompressAI(string):

    if len(string) < 1:
        return ''

    curr_char = string[0]
    curr_count = 0
    s = StringIO()

    for ch in string:

        if ch != curr_char:
            s.write(curr_char)
            s.write(str(curr_count))
            curr_char = ch
            curr_count = 1

        else:
            curr_count += 1

    s.write(curr_char)
    s.write(str(curr_count))

    compress_str = s.getvalue()
    s.close()

    if len(string) <= len(compress_str):
        return string

    return compress_str


print(stringCompress('aabbccdd'))
print(stringCompressAI('aabbccddd'))
