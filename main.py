from asyncio import run
from re import sub

from alfred.client import AlfredClient


async def main(client: AlfredClient):
    await client.update("yedhrab", "string-alfred")

    char_count = str(len(client.query))
    word_count = str(len(client.query.split(" ")))
    line_count = str(len(client.query.split("\n")))

    remove_dublication = " ".join(dict.fromkeys(client.query.split(" ")))

    upper_case = client.query.upper()
    lower_case = client.query.lower()
    capitalized = client.query.capitalize()
    template = sub(r"[a-zA-Z0-9]", "X", client.query)

    client.add_result(char_count, "Characters", arg=char_count)
    client.add_result(word_count, "Words", arg=word_count)
    client.add_result(line_count, "Lines", arg=line_count)
    client.add_result(upper_case, "Upper Case", arg=upper_case)
    client.add_result(lower_case, "Lower Case", arg=lower_case)

    client.add_result(remove_dublication, "Remove dublication", arg=remove_dublication)
    client.add_result(capitalized, "Capitalized", arg=capitalized)
    client.add_result(template, "Template", arg=template)
    client.response()


if __name__ == "__main__":
    run(main(AlfredClient()))
