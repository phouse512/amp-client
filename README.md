# amp-client
flask application built for raspbian 

## Design Goals:
- no internet connection
- can be pinged/identity requested across lan
- can give status to requesting
- write actions to local disk cache
- to be published
- secure
- plug-and-play: minimal effort on the user side, plug in and go
    - button press scanning


### NOTES TO REMEMBER
- write wrapper around rpi.gpio to allow for testing locally
    - custom inits, setting/getting pin values, etc
    - consider using the imp library to optionally import files
    - don't forget to pull down your read values by using a resister from read pin to ground.
        - don't forget read pin
