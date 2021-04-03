from mate.__main__ import get_plugin_manager, mate_config
from mate.modules.core import MateRecord

pm = get_plugin_manager()
record = MateRecord("mate", pm.hook)
record.add_modules()
mate_config.module_record = record
