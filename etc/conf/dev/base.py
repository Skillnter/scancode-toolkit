"""
This base config script gets automatically executed for all platforms via
configure if the "dev" sub-configuration is specified (which is the default).
"""

import os


def setup_dev_mode():
    from scancode import root_dir
    with open(os.path.join(root_dir, 'SCANCODE_DEV_MODE'), 'wb') as sdm:
        sdm.write('This is a tag file to notify that ScanCode is used in development mode. '
                  'In this mode, ScanCode does not rely on license data to remain untouched and will '
                  'always check the license index cache for consistency, rebuilding it if necessary.')


setup_dev_mode()
