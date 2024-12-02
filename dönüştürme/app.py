import os
import aspose.pdf as ap
import aspose.slides as slides

# Dosya yolu
g_pdf = "FIFA.pdf"  # PDF dosyası
g_pptx = "aa.pptx"  # PPTX dosyası
o_pptx = "pdf.pptx"  # PDF ->PPTX 
o_pdf = "pptx.pdf"  # PPTX ->PDF

def pdfd(g_pdf, o_pptx):
    try:
        #
        document = ap.Document(g_pdf)
        save_option = ap.PptxSaveOptions()
        document.save(o_pptx, save_option)
        print(f"PDF'den PPTX'ye dönüşüm başarılı: {o_pptx}")
    except Exception as e:
        print(f"PDF hata oluştu: {e}")

def pptxd(g_pptx, o_pdf):
    try:
        presentation = slides.Presentation(g_pptx)
        presentation.save(o_pdf, slides.export.SaveFormat.PDF)
        print(f"PPTX'ten PDF'ye dönüşüm başarılı: {o_pdf}")
    except Exception as e:
        print(f"PPTX hata oluştu: {e}")


pdfd(g_pdf, o_pptx)


pptxd(g_pptx, o_pdf)
