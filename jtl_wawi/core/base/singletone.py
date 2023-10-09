from typing import Any

# --
# ...
# --


class cSingletone(type):
    _instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self._instance is None:
            self._instance = super().__call__(*args, **kwds)

        return self._instance