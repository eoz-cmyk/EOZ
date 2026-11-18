"""CEO özeti PDF üreticisi.

Kullanım:  python3 araclar/ceo_ozeti_pdf.py girdi.json cikti.pdf

JSON alanları:
  baslik, alt_baslik, tarih, karar, karar_detay,
  metrikler: [{etiket, deger, not}]  (en fazla 3)
  bolumler:  [{etiket, metin}]       (metin: paragraf veya madde listesi)
  guven, kaynak_notu
Tasarım: A4, editoryal minimal, siyah/beyaz/altın, ızgara yerleşim.
"""
import json, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)
from reportlab.lib.styles import ParagraphStyle

GF = "/usr/share/fonts/truetype/google-fonts/ofl/"
pdfmetrics.registerFont(TTFont("Serif", GF + "crimsontext/CrimsonText-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Serif-SB", GF + "crimsontext/CrimsonText-SemiBold.ttf"))
pdfmetrics.registerFont(TTFont("Serif-I", GF + "crimsontext/CrimsonText-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Sans", GF + "firasans/FiraSans-Light.ttf"))
pdfmetrics.registerFont(TTFont("Sans-R", GF + "firasans/FiraSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-M", GF + "firasans/FiraSans-Medium.ttf"))

INK = HexColor("#111111")
GREY = HexColor("#6B6B6B")
RULE = HexColor("#D9D9D9")
GOLD = HexColor("#A88A4E")

W, H = A4
ML = MR = 22 * mm
MT, MB = 18 * mm, 20 * mm
CW = W - ML - MR
LABEL_W = 38 * mm

S = {
    "kicker": ParagraphStyle("k", fontName="Sans-M", fontSize=7.5, leading=10, textColor=GOLD, spaceAfter=6, charSpace=1.2),
    "title": ParagraphStyle("t", fontName="Serif-SB", fontSize=24, leading=28, textColor=INK, spaceAfter=4),
    "sub": ParagraphStyle("s", fontName="Serif-I", fontSize=12, leading=16, textColor=GREY),
    "label": ParagraphStyle("l", fontName="Sans-M", fontSize=7.5, leading=11, textColor=GOLD, charSpace=1),
    "body": ParagraphStyle("b", fontName="Sans", fontSize=9.3, leading=13.2, textColor=INK),
    "bullet": ParagraphStyle("bl", fontName="Sans", fontSize=9.3, leading=13.2, textColor=INK, leftIndent=9, bulletIndent=0, spaceAfter=2),
    "verdict": ParagraphStyle("v", fontName="Serif-SB", fontSize=15, leading=19, textColor=INK),
    "verdict_d": ParagraphStyle("vd", fontName="Sans", fontSize=9.6, leading=14, textColor=INK),
    "mval": ParagraphStyle("mv", fontName="Serif-SB", fontSize=17, leading=20, textColor=INK),
    "mlab": ParagraphStyle("ml", fontName="Sans-M", fontSize=7, leading=9, textColor=GREY, charSpace=0.8),
    "mnote": ParagraphStyle("mn", fontName="Sans", fontSize=8, leading=10.5, textColor=GREY),
    "foot": ParagraphStyle("f", fontName="Sans", fontSize=7.5, leading=10, textColor=GREY),
}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def rich(t):
    # **kalın** desteği
    out, bold = [], False
    for part in esc(t).split("**"):
        out.append(f"<font name='Sans-R'>{part}</font>" if bold else part)
        bold = not bold
    return "".join(out)


def footer(c, doc, meta):
    c.saveState()
    c.setStrokeColor(RULE); c.setLineWidth(0.4)
    c.line(ML, MB - 8 * mm, W - MR, MB - 8 * mm)
    c.setFont("Sans", 7.5); c.setFillColor(GREY)
    c.drawString(ML, MB - 12.5 * mm, meta)
    c.drawRightString(W - MR, MB - 12.5 * mm, f"{doc.page}")
    c.restoreState()


def build(data, out):
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
                          title=data["baslik"], author="CEO özeti")
    meta = f"CEO özeti · {data['tarih']} · Gizli — yalnızca iç değerlendirme"
    doc.addPageTemplates([PageTemplate(frames=[Frame(ML, MB, CW, H - MT - MB, 0, 0, 0, 0)],
                                       onPage=lambda c, d: footer(c, d, meta))])
    st = []
    st.append(Paragraph(f"CEO ÖZETİ  ·  {esc(data['tarih'])}", S["kicker"]))
    st.append(Paragraph(esc(data["baslik"]), S["title"]))
    if data.get("alt_baslik"):
        st.append(Paragraph(esc(data["alt_baslik"]), S["sub"]))
    st.append(Spacer(1, 6 * mm))

    # Karar bloğu: altın sol çizgi
    v = Table([[Paragraph(esc(data["karar"]), S["verdict"])],
               [Paragraph(rich(data.get("karar_detay", "")), S["verdict_d"])]], colWidths=[CW - 6 * mm])
    v.setStyle(TableStyle([
        ("LINEBEFORE", (0, 0), (0, -1), 2, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 5 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 2),
    ]))
    st.append(v)
    st.append(Spacer(1, 6 * mm))

    # Metrik şeridi
    ms = data.get("metrikler", [])[:3]
    if ms:
        cw = CW / len(ms)
        cells = [[Paragraph(esc(m["etiket"]).upper(), S["mlab"]), Spacer(1, 3),
                  Paragraph(esc(m["deger"]), S["mval"]), Spacer(1, 2),
                  Paragraph(esc(m.get("not", "")), S["mnote"])] for m in ms]
        t = Table([cells], colWidths=[cw] * len(ms))
        t.setStyle(TableStyle([
            ("LINEABOVE", (0, 0), (-1, 0), 0.6, INK), ("LINEBELOW", (0, 0), (-1, 0), 0.4, RULE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6 * mm),
            ("TOPPADDING", (0, 0), (-1, -1), 3 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
        ]))
        st.append(t)
        st.append(Spacer(1, 3 * mm))

    # Bölümler: sol etiket sütunu + sağ metin
    for b in data["bolumler"]:
        m = b["metin"]
        if isinstance(m, list):
            content = [Paragraph(rich(x), S["bullet"], bulletText="–") for x in m]
        else:
            content = [Paragraph(rich(m), S["body"])]
        row = Table([[Paragraph(esc(b["etiket"]).upper(), S["label"]), content]],
                    colWidths=[LABEL_W, CW - LABEL_W])
        row.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEABOVE", (0, 0), (-1, 0), 0.4, RULE),
            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 2.6 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4 * mm),
        ]))
        st.append(KeepTogether(row))

    if data.get("kaynak_notu"):
        st.append(Spacer(1, 3 * mm))
        st.append(Paragraph(esc(data["kaynak_notu"]), S["foot"]))
    doc.build(st)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        build(json.load(f), sys.argv[2])
