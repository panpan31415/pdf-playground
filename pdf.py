import PyPDF2
import sys


# with open("./PDF/dummy.pdf", "rb") as dummy_pdf:
#     reader = PyPDF2.PdfFileReader(dummy_pdf)
#     page1 = reader.getPage(0)
#     page1.rotateClockwise(180)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page1)
#     with open("./PDF/rotated_dummy_1.pdf", "wb") as rotated_dummy_1:
#         writer.write(rotated_dummy_1)


pdf_files = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_files:
        print(pdf)
        merger.append(pdf)

    merger.write("one.pdf")


# pdf_combiner(pdf_files)


def water_mark():
    with open("one.pdf", "rb") as target:
        target_reader = PyPDF2.PdfFileReader(target)
        with open("PDF/wtr.pdf", "rb") as water_marker:
            wtm_reader = PyPDF2.PdfFileReader(water_marker)
            mark = wtm_reader.getPage(0)
            file_writer = PyPDF2.PdfFileWriter()
            for index in range(target_reader.numPages):
                page = target_reader.getPage(index)
                page.mergePage(mark) 
                file_writer.addPage(page)
            with open("water_marked_one.pdf", "wb") as water_marked_one:
                file_writer.write(water_marked_one)


water_mark()
