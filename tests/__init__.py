from mate.__main__ import get_plugin_manager
from mate.modules.core import MateRecord
from mate.config import mate_config

pm = get_plugin_manager()
record = MateRecord("mate", pm.hook)
record.add_modules()
mate_config.module_record = record
