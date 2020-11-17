from argparse import Namespace
from typing import Optional, Union


class Configuration:
    fields = ['api_id', 'api_hash', 'group_name', 'group_id']
    api_id: int
    api_hash: str
    group_name: Optional[str]
    group_id: Optional[int] = None

    @classmethod
    def from_args(cls, args: Namespace):
        dictionary = {key: getattr(args, key) for key in cls.fields}
        return cls(**dictionary)

    def __init__(self,
                 api_id: Union[int, str],
                 api_hash: str,
                 group_name: Optional[str] = None,
                 group_id: Union[int, str, None] = None):
        if not group_name and not group_id:
            raise NameError('You didn\'t pass a group name and group id.')
        self.api_id = int(api_id)
        self.api_hash = api_hash
        self.group_name = group_name
        if group_id:
            self.group_id = int(group_id)
