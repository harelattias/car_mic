let moveMotorZIP : Kitronik_Move_Motor.MoveMotorZIP = null
input.onSound(DetectedSound.Loud, function on_sound_loud() {
    
    Kitronik_Move_Motor.soundSiren(Kitronik_Move_Motor.OnOffSelection.On)
    moveMotorZIP = Kitronik_Move_Motor.createMoveMotorZIPLED(4)
    moveMotorZIP.setZipLedColor(0, Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Red))
    moveMotorZIP.setZipLedColor(1, Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Blue))
    moveMotorZIP.setZipLedColor(2, Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Red))
    moveMotorZIP.setZipLedColor(3, Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Blue))
    moveMotorZIP.show()
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 100)
    basic.pause(2000)
    Kitronik_Move_Motor.stop()
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Reverse, 100)
    basic.pause(2000)
    Kitronik_Move_Motor.stop()
    for (let index = 0; index < 20; index++) {
        moveMotorZIP.rotate(1)
        moveMotorZIP.show()
        basic.pause(100)
    }
})
basic.forever(function on_forever() {
    
})
