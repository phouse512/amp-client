# amp-client
flask application built for raspbian 

## Design Goals:
- no internet connection
- can be pinged/identity requested across lan
- can divulge status
- write actions to local disk cache
- to be published


## ## user goals
- plug-and-play: minimal effort on the user side, plug in and go



## master goals:
- scan on button press
-

## developer goals
- testable across unix environments without necessarily being a raspberry pi
- unit tested

### NOTES TO REMEMBER
- COMBINE CLIENT/MASTER INTO ONE REPO
- write wrapper around rpi.gpio to allow for testing locally
    - custom inits, setting/getting pin values, etc
    - consider using the imp library to optionally import files
    - don't forget to pull down your read values by using a resister from read pin to ground.
        - don't forget read pin