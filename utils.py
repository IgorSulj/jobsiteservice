from typing import Annotated

from pydantic import Field, StrictStr


PHONE_REGEX = r'\+[0-9]+'


PhoneStr = Annotated[StrictStr, Field(pattern=PHONE_REGEX)]
