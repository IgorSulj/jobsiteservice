import re
from typing import Annotated

from pydantic import Field, StrictStr


PHONE_REGEX = r'\+[0-9]+'
IMAGE_REGEX = r'data:image/([a-zA-Z]+);base64,(?:[A-Za-z0-9+/]{4})*={0,2}'


PhoneStr = Annotated[StrictStr, Field(pattern=PHONE_REGEX)]
Base64ImageStr = Annotated[StrictStr, Field(pattern=IMAGE_REGEX)]

IMAGE_REGEX_COMPILED = re.compile(
    r'data:image/([a-zA-Z]+);base64,((?:[A-Za-z0-9+/]{4})*={0,2})'
)


def get_binary_image_data(data: Base64ImageStr):
    matched = IMAGE_REGEX_COMPILED.match(data)
    if matched is None:
        return None
    binary_data: str = matched[2]
    return binary_data.encode()
