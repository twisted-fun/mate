import sys
import os
from pathlib import Path

class MateConfig(object):
    def __init__(self):
        home = Path.home()
        self.mate_dir = (
            Path(".mate").resolve()
            if Path(".mate").exists()
            else Path(home / ".mate")
        )
        self.mate_conf = Path(self.mate_dir / ".mate.conf")
        self.mate_hist = Path(self.mate_dir / ".mate_history")

        self.project_dir = Path.cwd()
        self.output_dir = Path(self.mate_dir / "output")
        self.socket = None
        
        if not self.mate_dir.exists():
            self.mate_dir.mkdir(exist_ok=True)
            self.output_dir.mkdir(exist_ok=True)
            Path(self.mate_conf).touch()
            Path(self.mate_hist).touch()
        
        

