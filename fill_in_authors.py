import argparse
import re


def clean_authors(authors):
    """Remove dates of birth, death.
    """
    cleaned_authors = re.sub("\s*\[.+\]*", "", authors)
    return cleaned_authors


def fill_authors(input_file):
    with open(input_file, "r") as handle:
        data = handle.readlines()

    new_data = []
    authors = ""
    for raw_line in data:
        line = raw_line.rstrip().replace("\t", " ")
        if line.startswith("**"):
            authors = clean_authors(line)
        elif line.strip() != "" and authors != "":
            new_line = "{0}. {1}".format(authors, line)
            new_line = new_line.replace("..", ".")
            new_data.append(new_line)
        elif line.strip() == "":
            continue
        else:
            new_data.append(line)

    with open("output.txt", "w") as handle:
        handle.write("\n".join(new_data))


def main():
    parser = argparse.ArgumentParser(description="Takes a .md version of Lamas' "
                                                 "bibliography of butterflies and "
                                                 "adds authors to each reference. ")
    parser.add_argument('-i', '--input', dest='input_file', action='store',
                        help='filename of .md file containing biblio references.')

    args = parser.parse_args()
    input_file = args.input_file
    if input_file:
        fill_authors(input_file)


if __name__ == "__main__":
    main()
