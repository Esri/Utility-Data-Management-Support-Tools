import pathlib

docs = pathlib.Path(__file__).parent / 'docs'


for folder in docs.glob('*'):
    if not folder.is_dir():
        continue
    print(folder.name)

    with (folder / 'readme.md').open('w', encoding='utf-8') as writer:
        for f in folder.glob('*.html'):
            writer.write(f'- [{f.stem}](./{f.name})\n')
