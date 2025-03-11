from filemacBots import ABot, FBot, FSBot, IBot, ScannerBot, VBot

fbot = FBot
fsbot = FSBot
scannerBot = ScannerBot
Abot = ABot
Vbot = VBot
Ibot = IBot


def method_mapper(res):
    """
    Args:
     res -> the filter category ie(doc_method_map, video_method_map, audio_method_map, image_method_map) that the method is expected to return
        It acts like get request, returning only the requested resource.
    Returns:
    dict(res)
    """
    # create dictionary for maping file conversion to respective method
    doc_method_map = {
        "xls": {
            "csv": fbot.convert_xls_to_csv,
            "audio": fsbot().audiofy,
            "docx": fbot().convert_xls_to_word,
        },
        "csv": {"xls": fbot().convert_csv_to_xls},
        "docx": {
            "text": fbot().convert_word_to_text,
            "pdf": fbot().convert_word_to_pdf,
            "audio": fsbot().audiofy,
            "pptx": fbot().word_to_pptx,
        },
        "pdf": {
            "text": fbot().convert_pdf_to_text,
            "word": fbot().convert_pdf_to_word,
            "LongImage": scannerBot().scanAsLongImg,
            "audio": fsbot().audiofy,
            "image": fbot().pdf2image,
        },
        "text": {
            "audio": fsbot().audiofy,
            "pdf": fbot().txt_to_pdf,
            "docx": fbot().text_to_word,
        },
        "pptx": {
            "text": fbot().pptx_to_txt,
            "docx": fbot().ppt_to_word,
        },
    }

    check = {"doc_method_map": doc_method_map}

    return check.get(res)


print(method_mapper("doc_method_map").keys())
