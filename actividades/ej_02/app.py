# Aplicación del servidor
from boot import do_connect
from microdot import Microdot, send_file
from machine import Pin
import neopixel

# Definición de pines para los LEDs
led1 = Pin(32, Pin.OUT, value=0)
led2 = Pin(33, Pin.OUT, value=0)
led3 = Pin(25, Pin.OUT, value=0)

# Configuración del NeoPixel
strip = neopixel.NeoPixel(Pin(27), 4)
for i in range(4):
    strip[i] = (0, 0, 0)

strip.write()

do_connect()
server = Microdot()

@server.route('/')
async def main_page(request):
    return send_file('index.html')

@server.route('/<folder>/<filename>')
async def static_files(request, folder, filename):
    return send_file("/{}/{}".format(folder, filename))

@server.route('/led/switch/<led_id>')
async def led_switch(request, led_id):
    global led1, led2, led3
    
    if led_id == 'LED1':
        led1.value(not led1.value())
    elif led_id == 'LED2':
        led2.value(not led2.value())
    elif led_id == 'LED3':
        led3.value(not led3.value())
        
    return {"status": "OK"}

@server.route('/rgb/set/red/<int:red_value>')
async def set_red(request, red_value):
    global strip
    green = strip[0][1]
    blue = strip[0][2]
    
    for pixel in range(4):
        strip[pixel] = (red_value, green, blue)
        
    strip.write()
    
@server.route('/rgb/set/blue/<int:blue_value>')
async def set_blue(request, blue_value):
    global strip
    
    red = strip[0][0]
    green = strip[0][1]
    
    for pixel in range(4):
        strip[pixel] = (red, green, blue_value)
        
    strip.write()
    
@server.route('/rgb/set/green/<int:green_value>')
async def set_green(request, green_value):
    global strip
    
    red = strip[0][0]
    blue = strip[0][2]
    
    for pixel in range(4):
        strip[pixel] = (red, green_value, blue)
        
    strip.write()

server.run(port=80)