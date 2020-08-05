from pyvue import Vue, Component
from components.directory import Directory
from components.messages import Messages


class App(Vue):
    template = "#app-template"
    data = {
        "mode": 0  # UI mode
    }
    components = {
        "directory": Directory.get_component(),
        "messages": Messages.get_component()
    }




