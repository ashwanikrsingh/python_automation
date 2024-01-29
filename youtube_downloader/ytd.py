from pytube import YouTube
from sys import argv

def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    done = int(50 * current / stream.filesize)

    print(
        "\r[{}{}] {} MB / {} MB".format('=' * done, ' ' * (50 - done), "{:.2f}".format(bytes_to_megabytes(current)),
                                        "{:.2f}".format(bytes_to_megabytes(stream.filesize))))
    # print("\r[{}{}] {} bytes / {} bytes".format('=' * done, ' ' * (50 - done), current, stream.filesize))


def bytes_to_megabytes(bytes_size):
    megabytes_size = bytes_size / (1024 ** 2)
    return megabytes_size

link = argv[1]

yt = YouTube(link, on_progress_callback=progress_func)

print("title : ", yt.title)

print("views : ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.filesize

yd.download("/Users/asingh/python_automation")

