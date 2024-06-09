import kivy
from kivy.app import App
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.uix.button import Button
from kivy.clock import Clock


# kivy.require('1.9.0')


class TreeMap(MapView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.marker_event = None

    def on_map_touch_down(self, mapview, touch):

        lat, lon = self.get_latlon_at(*touch.pos)
        print(f"Touch at {lat}, {lon}")
        self.marker_event = Clock.schedule_once(lambda dt: self.add_marker_directly(lat, lon),1)

    def on_touch_up(self, touch, *kwarg):
       if self.marker_event:
          self.marker_event.cancel()
          self.marker_event = None

    def add_marker_directly(self, lat, lon):
        marker = MapMarkerPopup(lat=lat, lon=lon)
        self.add_widget(marker)


class TreeFinder(App):
    def on_start(self):
        marker = MapMarkerPopup(lat=42, lon=9.2)
        self.root.add_widget(marker)

    def build(self):
        return TreeMap()


app = TreeFinder()
app.run()
