import logging
import logging.handlers
import os
import sys

import cv2
import pytesseract
from PIL import Image
from rich.progress import Progress
from cli_colors import BBWHITE, DGREEN, DYELLOW, FMAGENTA, RED, RESET

###############################################################################
logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')
logger = logging.getLogger(__name__)


class ExtractText:
    ###############################################################################
    '''Do OCR text extraction from a given image file and display the extracted
    text to the screen finally save it to a text file assuming the name of the input
    file'''

    ###############################################################################

    def __init__(self, input_obj):
        self.input_obj = input_obj

    def preprocess(self):
        '''Check input object whether it`s a file or a directory if a file append
    the file to a set and return it otherwise append directory full path
    content to the set and return the set file. The returned set will be
    evaluated in the next step as required on the basis of requested operation
    For every requested operation, the output file if any is automatically
    generated on the basis of the input filename and saved in the same
    directory as the input file.
    Exit if the folder is empty
    '''

        files_to_process = []

        if os.path.isfile(self.input_obj):
            files_to_process.append(self.input_obj)
        elif os.path.isdir(self.input_obj):
            if os.listdir(self.input_obj) is None:
                print(f"{RED}Cannot work with empty folder{RESET}")
                sys.exit(1)
            for file in os.listdir(self.input_obj):
                file_path = os.path.join(self.input_obj, file)
                if os.path.isfile(file_path) and file_path.split('.')[-1].lower() in {'png', 'jpg', 'jpeg'}:
                    files_to_process.append(file_path)

        return files_to_process

    def OCR(self):
        image_list = self.preprocess()

        def ocr_text_extraction(image_path):
            '''Load image using OpenCV'''
            img = cv2.imread(image_path)

            # logger.info(f"{FMAGENTA}processing {image_path}...{RESET}")

            try:
                '''Preprocess image for better OCR results'''
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                thresh = cv2.threshold(
                    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
                img_pil = Image.fromarray(thresh)

                '''Perform OCR using pytesseract'''
                config = ("-l eng --oem 3 --psm 6")
                text = pytesseract.image_to_string((img_pil), config=config)

                '''Remove extra whitespaces and newlines
                text = ' '.join(text.split()).strip()'''
                # logger.info(F"{CYAN}Found:\n{RESET}")
                # print(text)
                current_path = os.getcwd()
                file_path = os.path.join(current_path, OCR_file)
                ''' Save the extracted text to specified file '''
                # logger.info(f"{DGREEN}Generating text file for the extracted text..{RESET}")

                with open(file_path, 'w') as file:
                    file.write(text)
                # logger.info(f"File saved as {DYELLOW}{OCR_file}{RESET}:")
                '''If there are multiple candidate images for text extraction,
                wait for key press before proceeding to the next
                image otherwise don't wait
                size = [i for i in enumerate(image_list)]'''

                if len(image_list) >= 2:
                    input(F"{BBWHITE}Press Enter to continue{RESET}")
                return text
            except KeyboardInterrupt:
                print("\nExiting")
                sys.exit(0)
            except FileNotFoundError as e:
                logger.error(f"Error: {str(e)}")
            except IOError as e:
                logger.error(
                    f"Could not write to output file '{OCR_file}'. \
Reason: {str(e)}{RESET}")
            except Exception as e:
                logger.error(f"{type(e).__name__}: {str(e)}")
                logger.error(f"{RED}{e}{RESET}")
            # except Exception as e:
            # logger.error(f"Error:>>{RED}{e}{RESET}")

        # _file_list_ = [None]
        if len(image_list) >= 1:
            with Progress() as progress:
                task = progress.add_task("[magenta] Extracting")
                for image_path in image_list:
                    OCR_file = image_path[:-4] + ".txt"
                    return ocr_text_extraction(image_path)
                    task.update(task, advance=1)
                    # _file_list_.append(OCR_file)
        else:
            for image_path in image_list:
                OCR_file = image_path[:-4] + ".txt"
                return ocr_text_extraction(image_path)
                task.update(task, advance=1)

