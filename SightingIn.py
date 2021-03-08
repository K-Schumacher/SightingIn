import math

# Distance Calculator

inchSize = input('In inches, how tall is your target? ')
milSize = input('In mils, how tall is your target? ')
yardDistance = float(inchSize) * 27.8 / float(milSize)
meterDistance = ((float(inchSize) / 39.4) * 1000) / float(milSize)

print(f'Your target is {yardDistance} yards away.')
print(f'Your target is {meterDistance} meters away.')

# Elevation Section

def onTargetElevation():
    global hitTargetElevation
    highOrLow = input('Was your elevation on target? ')
    if highOrLow.lower() == 'yes':
        hitTargetElevation = True
        return hitTargetElevation
    elif highOrLow.lower() == 'no':
        hitTargetElevation = False
        return hitTargetElevation
    else:
        print('Please response with yes or no.')

def onTargetWindage():
    global hitTargetWindage
    leftOrRight = input("Was your windage on target? " )
    if leftOrRight.lower() == 'yes':
        hitTargetWindage = True
        return hitTargetWindage
    elif leftOrRight.lower() == 'no':
        hitTargetWindage = False
        return hitTargetWindage
    else:
        print('Please response with yes or no.')

# Windage Section

onTargetElevation()
while hitTargetElevation == False:
    elevationCorrection = input('In inches, how far off target were you? ')
    elevation = input('Did you hit high or low? ')
    yardDistanceInHundredths = round(yardDistance) / 100
    moaChangeElevation = float(elevationCorrection) / yardDistanceInHundredths
    elevationClicks = int(moaChangeElevation) * 4
    if elevation.lower() == 'high':
        print(f'{elevationClicks} "down" should have you on target. Send')
        onTargetElevation()
    elif elevation.lower() == 'low':
        print(f'{elevationClicks} "up" should have you on target. Send another.')
        onTargetElevation()
    else:
        print('Please answer "high" or "low".')
else:
    print('')

onTargetWindage()
while hitTargetWindage == False:
    windageCorrection = input('In inches, how far off target were you? ')
    windage = input('Did you hit left or right? ')
    moaChangeWindage = float(windageCorrection) / yardDistanceInHundredths
    windageClicks = int(moaChangeWindage) * 4
    if windage.lower() == 'left':
        print(f'{windageClicks} "left" should have you on target. Send another.')
        onTargetWindage()
    elif windage.lower() == 'right':
        print(f'{windageClicks} "right" should have you on target. Send another.')
        onTargetWindage()
    else:
        print('Please answer "left" or "right".')
else:
    print('Hell yeah, smacking center!')