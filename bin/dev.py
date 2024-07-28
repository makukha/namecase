from configparser import ConfigParser
from pathlib import Path
import re
from typing import Annotated, Optional

import mistletoe
import typer
from typer import Typer


app = Typer(no_args_is_help=True, add_completion=False)


@app.command()
def get_python_versions(
    path: Annotated[Path, typer.Argument()] = 'tox.ini',
):
    """Gather python versions from tox.ini [tox].env_list."""
    conf = ConfigParser()
    conf.read(path)
    env_list = conf['tox']['env_list']
    versions = re.match(r'\bpy\{([^}]+)\}', env_list).group(1).split(',')
    print(' '.join(versions))


@app.command()
def get_markdown_code(
    path: Annotated[Path, typer.Argument()],
    lang: Annotated[Optional[list[str]], typer.Option()] = None,
):
    """Gather Markdown code blocks."""
    for item in mistletoe.Document(path.read_text()).children:
        match item:
            case mistletoe.block_token.CodeFence():
                if lang and item.language not in lang:
                    continue
                print(item.content)


if __name__ == '__main__':
    app()
