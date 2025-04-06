import nbformat
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edit notebook metadata.")
    parser.add_argument("notebook_path", help="Path to the .ipynb file")
    parser.add_argument("--title", required=True, help="Title of the notebook")
    parser.add_argument("--author", required=True, help="Author of the notebook")
    parser.add_argument("--affiliation", required=False, help="Affiliation of the author")

    args = parser.parse_args()

    with open(args.notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    nb.metadata["title"] = args.title

    author = {"name": args.author}
    if args.affiliation:
        author["affiliation"] = args.affiliation
    nb.metadata["authors"] = [author]
    
    nb.metadata.setdefault("tags", []).extend(["auto-generated"])

    with open(args.notebook_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
