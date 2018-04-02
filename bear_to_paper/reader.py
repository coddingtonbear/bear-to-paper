import io
import os
from typing import Dict, Text


class Reader(object):
    def __init__(self, path: Text) -> None:
        if not os.path.isfile(path):
            raise ValueError("File does not exist.")

        self._path = path

        super().__init__()

    def get_name(self) -> Text:
        return os.path.splitext(
            os.path.basename(
                self._path
            )
        )[0]

    def get_asset_map(self) -> Dict[Text, Text]:
        assets: Dict[Text, Text] = {}
        asset_dir = os.path.join(
            os.path.splitext(self._path)[0]
        )

        if not os.path.isdir(asset_dir):
            return assets

        for asset_path in os.listdir(asset_dir):
            assets[asset_path] = os.path.realpath(
                os.path.join(asset_dir, asset_path)
            )

        return assets

    def get_markdown(self) -> Text:
        with io.open(self._path, encoding='utf-8') as inf:
            return inf.read()

    def __str__(self):
        return "Bear Document at {path}".format(path=self._path)
