from typing import Annotated

from rapid_api_client import Path, Query

from remnapy.models import (
    GetNodesUsageByRangeResponseDto,
    GetNodeUserUsageByRangeResponseDto,
)
from remnapy.rapid import BaseController, get
