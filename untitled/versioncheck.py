# Filename versioncheck.py

import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn("Для выполнения этйо программы необходима как минимум \
                  версия Python 3.0",
            RuntimeWarning)
else:
    print('Нормальное продолжение')