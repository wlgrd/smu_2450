from smu.SMU2450 import API as smuAPI

smu = smuAPI()

if smu.discover_and_connect() is False:
    print('Test failed, no device found')

print("Connected!")

smu.write('SENS:FUNC "VOLT"')
smu.output_disable()
smu.set_source_current()
smu.set_current_drain_microamp(0)
smu.output_enable()

smu.set_current_drain_microamp(10)
time.sleep(0.5)

smu.output_disable()