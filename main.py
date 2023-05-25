import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GObject
from ventana import ExampleDialog

class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.set_default_size(800, 250)

        self.set_title("Ventana principal")

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)                                               

        self.box1.append(self.box2)                                             

        self.box1.append(self.box3)                                             

        self.grid1 = Gtk.GridView()

        self.box3.append(self.grid1)

        self.label = Gtk.Label()

        self.box3.append(self.label)                                           

        self.label1 = Gtk.Label()

        self.label1.set_text("Color favorito")

        self.box3.append(self.label1)

        self.label2 = Gtk.Label()

        self.label2.set_text("______________________")

        self.box3.append(self.label2)

        
        self.button_color = Gtk.Button(label="Colores")                            # Ponerle nombre al boton

        self.button_color.connect('clicked', self.button_colores)                        # Hace la funcion(hello)

        self.box2.append(self.button_color)
       
        self.entry = Gtk.Entry()

        self.box3.append(self.entry)
        self.button_aceptar = Gtk.Button(label="Aceptar")
        self.box3.append(self.button_aceptar)
        
        

    def button_acepta(self, button):
        print("Presionó el botón aceptar.")
        help = self.entry.get_text()
        self.label.set_text(help)

    def button_colores(self, button):

        print("Presionó el botón colores.")

        self.label.set_text("Cuál es tu")



class MyApp(Gtk.Application):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.connect('activate', self.on_activate)

    def on_activate(self, app):

        self.win = MainWindow(application=app)

        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")

app.run(sys.argv)
