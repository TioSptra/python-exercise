import logging
import os
import time
from docx import Document
import re

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s')
log = logging.getLogger()

class Compare:
    def __init__(self,doc1,doc2):
        self.doc1 = doc1
        self.doc2 = doc2

    def line_spacing(self):
        docA = Document(self.doc1)
        docB = Document(self.doc2)
        
        lineA = docA.paragraphs
        lineB = docB.paragraphs
        diff = 0

        for i in range(min(len(lineA),len(lineB))):
            spacingA = lineA[i].paragraph_format.line_spacing
            spacingB = lineB[i].paragraph_format.line_spacing

            if spacingA != spacingB:
                if spacingA is not None and spacingB is not None:
                    diff = spacingB - spacingA
                else:
                    diff = "N/A"
        print(f"line spacing    | Document A: {spacingA:.2f} spacing -  Document B: {spacingB:.2f} spacing - Perbedaan: {diff:.2f}")

    def bullet_numbering(self):
        docA = Document(self.doc1)
        docB = Document(self.doc2)

        lineA = docA.paragraphs
        lineB = docB.paragraphs
        diff = 0

        for i in range(min(len(lineA), len(lineB))):
            textA = lineA[i].text.strip()
            textB = lineB[i].text.strip()

            typeA = None
            typeB = None

            # Detect numbering / bullet Document A
            if re.match(r'^[A-Z][\.\)]', textA):
                typeA = "A)"
            elif re.match(r'^[a-z][\.\)]', textA):
                typeA = "a)"
            elif re.match(r'^\d+[\.\)]', textA):
                typeA = "1."
            elif re.match(r'^[ivxlcdm]+[\.\)]', textA, re.I):
                typeA = "i)"
            elif re.match(r'^[\•\-\*]', textA):
                typeA = "bullet"

            # Detect numbering / bullet Document B
            if re.match(r'^[A-Z][\.\)]', textB):
                typeB = "A)"
            elif re.match(r'^[a-z][\.\)]', textB):
                typeB = "a)"
            elif re.match(r'^\d+[\.\)]', textB):
                typeB = "1."
            elif re.match(r'^[ivxlcdm]+[\.\)]', textB, re.I):
                typeB = "i)"
            elif re.match(r'^[\•\-\*]', textB):
                typeB = "bullet"

            if typeA != typeB:
                diff = 1
        print(f"Numbering/Bullet| Document A: {typeA} - Document B: {typeB} - Perbedaan: {diff}")

    def identity_spacing(self):
        docA = Document(self.doc1)
        docB = Document(self.doc2)

        pA = docA.paragraphs
        pB = docB.paragraphs


        for i in range(min(len(pA), len(pB))):
            indentA = pA[i].paragraph_format.left_indent
            indentB = pB[i].paragraph_format.left_indent

            # Konversi ke cm (1 cm = 28.35 points)
            valA = (indentA.pt / 28.35) if indentA else 0
            valB = (indentB.pt / 28.35) if indentB else 0
            diff = valB - valA
        
        print(f"Indent spacing  | Document A: {valA:.2f} cm      -  Document B: {valB:.2f} cm      - Perbedaan: {diff:.2f} cm")

    def printing_effect(self):
        docA = Document(self.doc1)
        docB = Document(self.doc2)

        total_diff = 0

        for i in range(min(len(docA.paragraphs), len(docB.paragraphs))):
            runsA = docA.paragraphs[i].runs
            runsB = docB.paragraphs[i].runs

            for j in range(min(len(runsA), len(runsB))):
                rA = runsA[j]
                rB = runsB[j]

                # hanya bandingkan jika teks sama dan tidak kosong
                if rA.text.strip() and rA.text == rB.text:

                    # efek dokumen A
                    effectsA = {
                        "bold": bool(rA.bold),
                        "italic": bool(rA.italic),
                        "underline": bool(rA.underline)
                    }

                    # efek dokumen B
                    effectsB = {
                        "bold": bool(rB.bold),
                        "italic": bool(rB.italic),
                        "underline": bool(rB.underline)
                    }

                    diff_effects = 0

                    for ef in effectsA:
                        if effectsA[ef] != effectsB[ef]:
                            diff_effects += 1

                    if diff_effects > 0:
                        total_diff += diff_effects

                        effectA_text = ", ".join(
                            [k for k, v in effectsA.items() if v]
                        ) or "regular"

                        effectB_text = ", ".join(
                            [k for k, v in effectsB.items() if v]
                        ) or "regular"

                        print(
                            f"Dokumen A = {rA.text} - {effectA_text}\n"
                            f"Dokumen B = {rB.text} - {effectB_text}\n"
                            f"Perbedaan = {diff_effects} efek\n"
                        )

        print(f"TOTAL PERBEDAAN EFEK: {total_diff}")

    # def typo(self):
    #     from docx import Document
    #     import nltk
    #     from nltk.tokenize import word_tokenize
    #     from collections import Counter
    #     import string

    #     nltk.download('punkt', quiet=True)

    #     def read_docx(path):
    #         doc = Document(path)
    #         return " ".join(p.text for p in doc.paragraphs).lower()

    #     def tokenize(text):
    #         tokens = word_tokenize(text)
    #         return [t for t in tokens if t not in string.punctuation]

    #     # Baca & tokenize
    #     wordsA = tokenize(read_docx(self.doc1))
    #     wordsB = tokenize(read_docx(self.doc))

    #     counterA = Counter(wordsA)
    #     counterB = Counter(wordsB)

    #     all_words = set(counterA) | set(counterB)

    #     total_salah = 0

    #     print("Perbedaan kata per dokumen:\n")

    #     for word in sorted(all_words):
    #         a = counterA.get(word, 0)
    #         b = counterB.get(word, 0)
    #         if a != b:
    #             print(f"{word} -> Dokumen A: {a}, Dokumen B: {b}")
    #             total_salah += abs(a - b)

    #     print("\nTotal kata yang berbeda / salah:", total_salah)

if __name__ == '__main__':
    a = os.path.join("doc","Dokumen A.docx")
    b = os.path.join("doc","Dokumen B.docx")
    document = Compare(a,b)
    document.line_spacing()
    document.bullet_numbering()
    document.identity_spacing()
    document.printing_effect()
    # document.typo()