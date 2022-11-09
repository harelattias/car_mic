moveMotorZIP: Kitronik_Move_Motor.MoveMotorZIP = None

def on_sound_loud():
    global moveMotorZIP
    Kitronik_Move_Motor.sound_siren(Kitronik_Move_Motor.OnOffSelection.ON)
    moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)
    moveMotorZIP.set_zip_led_color(0,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.set_zip_led_color(1,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLUE))
    moveMotorZIP.set_zip_led_color(2,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    moveMotorZIP.set_zip_led_color(3,
        Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLUE))
    moveMotorZIP.show()
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 100)
    basic.pause(2000)
    Kitronik_Move_Motor.stop()
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE, 100)
    basic.pause(2000)
    Kitronik_Move_Motor.stop()
    for index in range(20):
        moveMotorZIP.rotate(1)
        moveMotorZIP.show()
        basic.pause(100)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_forever():
    pass
basic.forever(on_forever)
