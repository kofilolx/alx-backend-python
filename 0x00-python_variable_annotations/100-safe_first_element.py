#!/usr/bin/env python3

from typing import List, Optional, TyeVar

T = TypeVar('T)

def safe_list_element(lst: List[T)] -> Optional[T]:
  if lst:
    return lst[0]
  else:
      return None
