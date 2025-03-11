# convert pdf to long image
import os
import subprocess
import sys

from pdf2image import convert_from_path
from PIL import Image  # ImageSequence

from cli_colors import (DCYAN, DGREEN, DMAGENTA, DBLUE, DYELLOW, RED, RESET)
from filemacBots import FBot


class LImage:
    def __init__(self, doc):
        self.doc = doc

    def preprocess(self):
        ext = self.doc.split('.')[-1].lower()
        if ext == "pdf":
            LI = LImage.pdf_2L_Img(self.doc)
            return LI
        if ext == 'doc' or ext == 'docx':
            conv = FBot()

            path = conv.word_to_pdf(self.doc)
            LI = LImage.pdf_2L_Img(path)
            return LI
        elif ext == 'odt':
            # pdf_file = ext = doc.split('.')[0] + 'docx'
            print(f"{DCYAN}Call soffice and wait ..{RESET}")
            subprocess.call(['soffice', '--convert-to',
                             'pdf', self.doc, '--outdir', os.path.dirname(
                                        self.doc)])
            pdf_file = os.path.abspath(os.path.dirname(
                self.doc) + '/' + (self.doc.split('/')[-1].split('.')[0]) + '.pdf')
            LI = LImage.pdf_2L_Img(pdf_file)
            return LI

    @staticmethod
    def pdf_2L_Img(pdf_file):
        try:
            print(f"{DYELLOW}Read pdf{RESET}")
            images = convert_from_path(pdf_file)
            out_img = pdf_file[:-4] + '.png'
            heights = [img.size[1] for img in images]
            total_height = sum(heights)
            max_width = max([img.size[0] for img in images])

            print(F"{DCYAN}Draw image ..{RESET}")
            new_im = Image.new('RGB', (max_width, total_height))

            y_offset = 0
            for i, img in enumerate(images):
                print(f"{DBLUE}{i}{RESET}", end='\r')
                new_im.paste(img, (0, y_offset))
                y_offset += img.size[1]
            print(f"{DYELLOW}Save dest: {DMAGENTA}{out_img}{RESET}")
            new_im.save(out_img)
            print(f"{DGREEN}Success😇✅{RESET}")
            return out_img
        except FileNotFoundError:
            print(f"{RED}File not found!{RESET}")
        except KeyboardInterrupt:
            print("\nQuit❕")
            sys.exit()
        except Exception as e:
            print(e)
            sys.exit(1)
