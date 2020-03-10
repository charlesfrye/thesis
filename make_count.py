#! /usr/bin/env python3
import datetime
from pathlib import Path
import subprocess

NUM_CHAPTERS = 3
THESIS_DIR = Path("~").expanduser() / "research" / "thesis"
CHAPTERS_DIR = THESIS_DIR / "chapters"
PDFS_DIR = THESIS_DIR / "pdfs"

OUTFILE = "counts.csv"


def main():

    now = datetime.datetime.now()
    now_string = now.strftime("%d/%m/%Y %H:%M:%S")

    subprocess.run(["make", "thesis"])

    # thesis_pdf = PDFS_DIR / "thesis.pdf"
    # chapter_pdfs = [PDFS_DIR / ("chapter" + str(ii) + ".pdf")
    #                for ii in range(1, NUM_CHAPTERS + 1)]

    chapter_dirs = [CHAPTERS_DIR / ("chapter" + str(ii))
                    for ii in range(1, NUM_CHAPTERS + 1)]
    chapter_texs = [chapter_dir / ("chapter" + str(ii) + ".tex")
                    for chapter_dir, ii
                    in zip(chapter_dirs, range(1, NUM_CHAPTERS + 1))]

    outlines = []
    for tex in chapter_texs:
        completed_linecount_process = subprocess.run(
                ["wc", "-l", f"{tex}"], capture_output=True)
        process_stdout_as_str = \
            completed_linecount_process.stdout.decode("UTF-8")
        linecount = process_stdout_as_str.split(" ")[0]
        outlines.append(",".join([now_string, linecount, tex.name+"\n"]))

    with open(OUTFILE, "a") as f:
        f.writelines(outlines)


if __name__ == "__main__":
    main()
