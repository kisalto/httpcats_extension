import json
import random

import vscode

ext = vscode.Extension(
    name="HTTP Cats",
    metadata=vscode.ExtensionMetadata(
        publisher="kisalto",
        version="0.0.1",
        icon="continue.png",
        repository="https://github.com/kisalto/httpcats_extension",
        display_name="HTTP Cats",
        description="Abre um gato HTTP aleatório no Simple Browser",
    ),
)


@ext.event
async def on_activate():
    vscode.log(f"The Extension '{ext.name}' has started")


status_list = [
    100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 214, 226,
    300, 301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404, 405, 406,
    407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421,
    422, 423, 424, 425, 426, 428, 429, 431, 444, 450, 451, 495, 496, 497, 498,
    499, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 511, 521, 522, 523,
    525, 530, 599
]


@ext.command(name="Http Cats")
async def open_browser(ctx) -> None:
    status_code = random.choice(status_list)
    url = f"https://http.cat/{status_code}"

    # Roda JS no extension host: chama o comando nativo do Simple Browser.
    # json.dumps gera uma string JS válida (com aspas e escapes).
    await ctx.ws.run_code(
        f"vscode.commands.executeCommand('simpleBrowser.show', {json.dumps(url)})",
        wait_for_response=False,
    )
    # return await ctx.show(InfoMessage(f"Showing HTTP Cat for status code {status_code}!"))


ext.run()