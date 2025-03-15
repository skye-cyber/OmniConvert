# multimedia_cli/formats.py
from cli_colors import (CYAN, DBLUE, DMAGENTA, DYELLOW, FCYAN, FYELLOW,
                        IMAGENTA, RESET)

SUPPORTED_DOC_FORMATS = f"""
|---------------------------------------------------------------------------
|{DBLUE}Input format{RESET}                    |{DBLUE}Output format{RESET}                             |
|________________________________|__________________________________________|
|   xlsx    {DYELLOW}-------------------->{RESET}|csv txt doc/docx db(sql)                  |
|                                |                                          |
|   doc/docx{DYELLOW}-------------------->{RESET}|txt pdf ppt/pptx audio(ogg)               |
|                                |                                          |
|   txt     {DYELLOW}-------------------->{RESET}|pdf docx/doc audio(ogg)                   |
|                                |                                          |
|   pdf     {DYELLOW}-------------------->{RESET}|doc/docx txt audio(ogg)                   |
|                                |                                          |
|   pptx/ppt{DYELLOW}-------------------->{RESET}|doc/docx                                  |
|                                                                           |
|___________________________________________________________________________|
"""


# Add supported input and output formats for each media type
SUPPORTED_AUDIO_FORMATS_INPUT = ["wav",  # Waveform Audio File Format
                                 "mp3",  # MPEG Audio Layer III
                                 "ogg",
                                 "flv",
                                 "ogv",
                                 "webm",
                                 "aiff",
                                 "flac",
                                 "m4a",
                                 "raw",
                                 "bpf",
                                 # Advanced Audio Codec]  (Free Lossless Audio Codec)
                                 "aac"]

SUPPORTED_AUDIO_FORMATS_OUTPUT = ["mp3",
                                  "wav",
                                  "raw",
                                  "ogg",
                                  "aiff",
                                  "flac",
                                  "flv",  # Flash Video
                                  "webm",
                                  "ogv"]  # Video
SUPPORTED_AUDIO_FORMATS_SHOW = f'''
|==============================|
|  {DBLUE}Supported I/O formats {RESET}      |
|==============================|
|          {CYAN} wav {DYELLOW}               |
|          {CYAN} mp3 {DYELLOW}               |
|          {CYAN} ogg {DYELLOW}               |
|          {CYAN} flv {DYELLOW}               |
|          {CYAN} ogv {DYELLOW}               |
|          {CYAN} mov {DYELLOW}               |
|          {CYAN} webm {DYELLOW}              |
|          {CYAN} aac {DYELLOW}-------------->|{IMAGENTA}Pending Implementation{RESET}{DYELLOW}
|          {CYAN} bpf {DYELLOW}-------------->|{IMAGENTA}Pending Implementation{RESET}{DYELLOW}
|          {CYAN} m4a {DYELLOW}               |
|          {CYAN} raw {DYELLOW}               |
|          {CYAN} aiff {DYELLOW}              |
--------------------------------

'''

SUPPORTED_VIDEO_FORMATS = ["MP4",  # MPEG-4 part 14 Bitrate - 860kb/s
                           "AVI",  # Audio Video Interleave
                           "OGV",
                           "WEBM",
                           "MOV",  # QuickTime video Bitrate - 1.01mb/s
                           "MKV",  # Matroska video - MKV is known for its support of high-quality content. Bitrate-1.01mb/s
                           "FLV",  # Flash video Bitrate
                           "WMV"]


Video_codecs = {
    "MP4": "mpeg4",
    "AVI": "rawvideo",
    # "OGV": "avc",
    "WEBM": "libvpx",
    "MOV": "mpeg4",  # QuickTime video
    "MKV": "mpeg4",  # Matroska video
    "FLV": "flv"
    # "WMV": "WMV"
}
SUPPORTED_VIDEO_FORMATS_SHOW = f'''
,_______________________________________,
|x| {DBLUE}Supported I/O formats{RESET}             |x|
|x|-----------------------------------{DYELLOW}|x|
|x|               {DMAGENTA} MP4 {DYELLOW}               |x|
|x|               {DMAGENTA} AVI {DYELLOW}               |x|
|x|               {DMAGENTA} OGV {DYELLOW}-------------->|x|{IMAGENTA}Pending Implementation{RESET}{DYELLOW}
|x|               {DMAGENTA} WEBM{DYELLOW}               |x|
|x|               {DMAGENTA} MOV {DYELLOW}               |x|
|x|               {DMAGENTA} MKV {DYELLOW}               |x|
|x|               {DMAGENTA} FLV {DYELLOW}               |x|
|x|               {DMAGENTA} WMV {DYELLOW}-------------->|x|{IMAGENTA}Pending Implementation{RESET}{DYELLOW}
|,|___________________________________|,|{DYELLOW}
'''

SUPPORTED_IMAGE_FORMATS = {
    "JPEG": ".jpeg",  # Joint Photographic Experts Group -Lossy compression
    "JPG": ".jpg",
    "PNG": ".png",  # Joint Photographic Experts Group - not lossy
    "GIF": ".gif",  # Graphics Interchange Format
    "BMP": ".bmp",  # Windows BMP image
    "DIB": ".dib",  # Windows BMP image
    "TIFF": ".tiff",  # Tagged Image File Format A flexible and high-quality image format that supports lossless compression
    "PIC": ".pic",
    "PDF": ".pdf",
    "WEBP": ".webp",
    "EPS": ".eps",
    "ICNS": ".icns",  # MacOS X icon
    # Waiting Implementation 👇
    "PSD": ".psd",
    "SVG": ".svg",  # Scalable vector Graphics
    "EXR": ".exr",
    "DXF": ".dxf",  # Autocad format 2D
    "PICT": "pct",
    "PS": ".ps",  # PostSciript
    "POSTSCRIPT": ".ps"}

SUPPORTED_IMAGE_FORMATS_SHOW = f'''
__________________________________________
|x|{DBLUE}Supported I/O formats{RESET}                |x|
|x|_____________________________________{DYELLOW}|x|
|x|               {DMAGENTA} JPEG {DYELLOW}                |x|
|x|               {DMAGENTA} PNG  {DYELLOW}                 |x|
|x|               {DMAGENTA} GIF  {DYELLOW}                 |x|
|x|               {DMAGENTA} BMP  {DYELLOW}                 |x|
|x|               {DMAGENTA} DIB  {DYELLOW}                 |x|
|x|               {DMAGENTA} TIFF {DYELLOW}                 |x|
|x|               {DMAGENTA} PIC  {DYELLOW}                 |x|
|x|               {DMAGENTA} EXR  {FYELLOW}---------------->|x|{FCYAN} Pending Implementation{RESET}{DYELLOW}
|x|               {DMAGENTA} PDF  {DYELLOW}                 |x|
|x|               {DMAGENTA} WebP {DYELLOW}                 |x|
|x|               {DMAGENTA} ICNS {DYELLOW}                 |x|
|x|               {DMAGENTA} PSD  {FYELLOW}---------------->|x|{FCYAN} Pending Implementation{RESET}{DYELLOW}
|x|               {DMAGENTA} SVG  {FYELLOW}---------------->|x|{FCYAN} Pending Implementation{RESET}{DYELLOW}
|x|               {DMAGENTA} EPS  {DYELLOW}                 |x|
|x|               {DMAGENTA} Postscript {FYELLOW}---------->|x|{FCYAN} Pending Implementation{RESET}{DYELLOW}
|x|               {DMAGENTA} PICT {FYELLOW}---------------->|x|{FCYAN} Pending Implementation{RESET}{DYELLOW}
|_|_____________________________________|x|
'''

SUPPORTED_DOCUMENT_FORMATS = ['pdf', 'doc', 'docx', 'csv', 'xlsx', 'xls',
                              'ppt', 'pptx', 'txt', 'ogg', 'mp3', 'audio']
