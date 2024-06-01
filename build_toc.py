import datetime
import pathlib
import lxml.html

docs = pathlib.Path(__file__).parent / "docs"


for folder in docs.glob("*"):
    if not folder.is_dir():
        continue
    print(folder.name)

    with (folder / "readme.md").open("w", encoding="utf-8") as writer:
        header = ["Toolset", "Name", "Alias", "Description"]
        writer.write("| {} |\n| {} |\n".format(" | ".join(header), " | ".join(["---"] * len(header))))
        for f in folder.glob("*.html"):
            print(f"\t{f}")
            html: lxml.html.HtmlElement = lxml.html.parse(f).getroot()

            name = f"[{f.stem}](./{f.name})"
            alias = html.find_class("ContentHeader")[0].getparent().text_content().split("\t")[-1]
            description = ""
            toolset = ""
            for h in html.findall(".//h3"):
                if h.text == "Description":
                    pre = h.getnext().getnext()
                    if pre is not None:
                        description = pre.text_content()
                elif h.text == "Toolset":
                    toolset = h.tail
            writer.write("| {} |\n".format(" | ".join([toolset, name, alias, description])))

        writer.write(f"\n`Last built {datetime.date.today()}`\n")
