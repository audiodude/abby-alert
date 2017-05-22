import random

import flask
from phue import Bridge
from rgb_xy import GamutC, Converter

converter = Converter(GamutC)
b = Bridge(ip='10.0.0.57')

app = flask.Flask(__name__)

@app.route('/')
def hello():
  return flask.render_template('index.html')

@app.route('/api/change')
def change():
  color = flask.request.args.get('color')

  lights = b.lights
  for light in lights:
    light.brightness = 255

    if color == 'green':
      light.xy = converter.rgb_to_xy(0, 255, 0)
    elif color == 'purple':
      light.xy = converter.rgb_to_xy(128, 0, 128)
    elif color == 'red':
      light.xy = converter.rgb_to_xy(255, 0, 0)
    elif color == 'reset':
      light.colortemp = 400

  return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
