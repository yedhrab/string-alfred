from asyncio import run
from json import dumps
from urllib.parse import parse_qs, quote_plus, unquote_plus, urlsplit

from alfred.client import AlfredClient


async def main(client: AlfredClient):
    await client.update("yedhrab", "string-alfred")

    encoded_string = quote_plus(client.query)
    decoded_string = unquote_plus(client.query)

    parsed = urlsplit(client.query)
    parsedurl = dumps({'origin': parsed.netloc, 'path': parsed.path, 'query': parse_qs(parsed.query)})

    client.add_result(encoded_string, "Encoded", arg=encoded_string)
    client.add_result(decoded_string, "Decoded", arg=decoded_string)
    client.add_result("Parsed url", parsedurl, arg=parsedurl)
    client.response()


if __name__ == "__main__":
    run(main(AlfredClient()))
