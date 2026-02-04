import re
from enum import Enum 

class link_t(Enum):
    Null = "empty"
    LinkNotfound = "zero link"
    MoreOneLink  = "More than one"


def find_link(text):
    if not text:
        return link_t.Null  
    
    links = re.findall(r"https?://\S+",text)

    if len(links) == 0:
        return link_t.LinkNotfound
    elif len(links) > 1:
        return link_t.MoreOneLink
    
    link = links[0].strip()

    return link
