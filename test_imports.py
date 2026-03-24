#!/usr/bin/env python3
"""Quick test to verify all new imports work"""

try:
    from remnapy.models import (
        GetSubpageConfigByShortUuidResponseDto,
        ReorderConfigProfilesRequestDto,
        ReorderExternalSquadsRequestDto,
        ReorderInternalSquadsRequestDto,
        ReorderSubscriptionTemplatesRequestDto,
    )

    print("✅ Все новые модели успешно импортируются!")
    print("   - ReorderConfigProfilesRequestDto")
    print("   - ReorderSubscriptionTemplatesRequestDto")
    print("   - ReorderInternalSquadsRequestDto")
    print("   - ReorderExternalSquadsRequestDto")
    print("   - GetSubpageConfigByShortUuidResponseDto")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    exit(1)
