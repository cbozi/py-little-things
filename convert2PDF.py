import os
import win32com.client

def doc2pdf(filename):
    try:
        doc = msword.Documents.Open(filename)
    except:
        print(filename,'not successful')
        return
    pdf_name = os.path.splitext(filename)[0] + '.pdf'
    doc.SaveAs(pdf_name, 17)
    doc.Close()

def ppt2pdf(filename):
    try:
        ppt = msppt.Presentations.Open(filename, WithWindow=0)
    except:
        print(filename,'not successful')
        return
    pdf_name = os.path.splitext(filename)[0] + '.pdf'
    ppt.SaveAs(pdf_name, 32)
    ppt.Close()
    
if __name__ == '__main__':
    msword = win32com.client.Dispatch('Word.Application')
    msppt = win32com.client.Dispatch('PowerPoint.Application')
    for file in os.listdir():
        if not os.path.isfile(file):
            continue
        if os.path.splitext(file)[1]=='.doc' or os.path.splitext(file)[1]=='.docx':
            print('Converting', file, '...')
            doc2pdf(os.getcwd()+os.sep+file)
        if os.path.splitext(file)[1]=='.ppt' or os.path.splitext(file)[1]=='.pptx':
            print('Converting', file, '...')
            ppt2pdf(os.getcwd()+os.sep+file)
    msword.Quit()
    msppt.Quit()

    input()
