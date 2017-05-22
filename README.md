# abby-alert
An alert system using Phillips Hue and phue.py

*Problem:*
How can Abby alert T-$ when she needs him and he's in another room, possibly
with headphones on?

*Solution:*
Abby Alerts!

Abby simply navigates to a webapp on her phone or iPad. It looks like this:

![screenshot 2017-05-21 20 30 49](https://cloud.githubusercontent.com/assets/57832/26291607/6639c65e-3e64-11e7-9b1f-cc802d1e884a.png)

The webapp is tunneled using [ngrok](https://ngrok.com/) to this application running
on T-$'s local desktop iMac.

She then taps one of the buttons on the screen and the app makes an AJAX request
to the simple Flask backend. The backend uses [phue.py](https://github.com/studioimaginaire/phue)
to change the colors of the lights in the Living Room, Kitchen and Bedroom to the
desired color. The bedroom light is changed even though Abby is likely there, in
order to confirm.

Once T-$ has responded to the Alert, the "reset" button can be used to reset the
lights to a soft white color.

Thanks Abby Alerts!
