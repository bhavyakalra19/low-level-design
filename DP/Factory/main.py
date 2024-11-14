from abc import ABC, abstractmethod

class Component(ABC):
    
    @abstractmethod
    def render(self):
        pass
    

class WindowsPlayButton(Component):
    def render(self):
        return "render windows play button"

class WindowsTimeline(Component):
    def render(self):
        return "render windows timeline"
    
class WindowsWindow(Component):
    def render(self):
        return "render windows window"
    

class MacPlayButton(Component):
    def render(self):
        return "render mac play button"

class MacTimeline(Component):
    def render(self):
        return "render mac timeline"
    
class MacWindow(Component):
    def render(self):
        return "render mac window"
    

class AbstractPlayerComponentFactory(ABC):
    @abstractmethod
    def create_component(self, component_type):
        pass

class WindowsPlayerComponentFactory:
    def create_component(self, component_type):
        if component_type == 'play_button':
            return WindowsPlayButton()
        elif component_type == 'timeline':
            return WindowsTimeline()
        elif component_type == 'window':
            return WindowsWindow()
    
class MacPlayerComponentFactory:
    def create_component(self, component_type):
        if component_type == 'play_button':
            return MacPlayButton()
        elif component_type == 'timeline':
            return MacTimeline()
        elif component_type == 'window':
            return MacWindow()
        
def client(factory):
    window = factory.create_component("window")
    timeline = factory.create_component("timeline")
    play_button = factory.create_component("play_button")
    
    print(window.render(), timeline.render(), play_button.render())
        
if __name__ == "__main__":
    curr_os = 'window'
    
    if curr_os == 'window':
        client(WindowsPlayerComponentFactory())