from __future__ import annotations

from ..nameable_type import NameableType


class Semver(NameableType):
    BASE = 1024

    @classmethod
    def to_int(cls, s: str) -> int | None:
        if s.startswith("v"):
            s2 = s[1:]
            try:
                p = [int(i) for i in s2.split(".")]
            except Exception:
                return None

            if len(p) == 3 and all(i < cls.BASE for i in p):
                v = p[2] + cls.BASE * (p[1] + cls.BASE * p[0])
                return v * cls.BASE
        return None

    @classmethod
    def int_to_type(cls, i: int) -> str | None:
        if i >= 0:
            d0, m0 = divmod(i, cls.BASE)
            if not m0:
                d1, m1 = divmod(d0, cls.BASE)
                d2, m2 = divmod(d1, cls.BASE)
                d3, m3 = divmod(d2, cls.BASE)
                if not d3:
                    return f"v{m3}.{m2}.{m1}"
        return None
