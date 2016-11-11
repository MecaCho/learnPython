# encoding=utf-8
# 在Windows和Mac OS X平台上统计PDF的文档的页数

# Windows
# 借助于PyPdf
# 1.下载http://pybrary.net/pyPdf/pyPdf-1.13.zip
# 2.注册Python环境变量path中假如D:\Python27
# 3.cmd中 cd D:\Python27\pyPdf-1.13
# 4.setup.py install
# 5.安装库完成
from pyPdf import PdfFileWriter, PdfFileReader


def getPdfPageNum(path):
    doc = PdfFileReader(file(path, "rb"))
    return doc.getNumPages()


print getPdfPageNum(r"D:\Disk\Photoshop.pdf")
# Mac OS X 有自带内容 ，以下为参考代码
import sys
if sys.platform == 'darwin':
    import CoreGraphics
    def pageCount(pdfPath):
        "Return the number of pages for the PDF document at the given path."
        pdf = CoreGraphics.CGPDFDocumentCreateWithProvider(
            CoreGraphics.CGDataProviderCreateWithFilename(pdfPath)
        )
        return pdf.getNumberOfPages()