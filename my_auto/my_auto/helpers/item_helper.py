from my_auto.items import MyAutoItem

class ItemHelper:

    def make_item(  self,
                    carid = None,
                    time = None,
                    customs=None,
                    location = None,
                    manufacturer = None,
                    model = None,
                    year = None,
                    category = None,
                    fuel_type = None,
                    engine_volume = None,
                    mileage = None,
                    cylinders = None,
                    gear_type = None,
                    drive_wheels = None,
                    doors = None,
                    wheel = None,
                    color = None,
                    interior_color = None,
                    airbags = None,
                    abs = None,
                    el_windows = None,
                    air_condintioner = None,
                    climate_system = None,
                    leather_interior = None,
                    disks = None,
                    navigation_system = None,
                    central_lock = None,
                    hatch = None,
                    alarm = None,
                    board_computer = None,
                    hydraulics = None,
                    anti_skid = None,
                    chair_warming = None,
                    parking_control = None,
                    rear_view_camera = None,
                    price = None,
                    description = None):
        item = MyAutoItem()
        item['customs'] = customs
        item['location'] = location
        item['manufacturer'] = manufacturer
        item['model'] = model
        item['year'] =year
        item['category'] = category
        item['fuel_type'] = fuel_type
        item['engine_volume'] =engine_volume
        item['mileage'] =mileage
        item['cylinders'] =cylinders
        item['gear_type'] =gear_type
        item['drive_wheels'] =drive_wheels
        item['doors'] =doors
        item['wheel'] =wheel
        item['color'] =color
        item['interior_color'] =interior_color
        item['airbags'] = airbags
        item['abs'] =abs
        item['el_windows'] =el_windows
        item['air_condintioner'] = air_condintioner
        item['climate_system'] =climate_system
        item['leather_interior'] =leather_interior
        item['disks'] =disks
        item['navigation_system'] =navigation_system
        item['central_lock'] =central_lock
        item['hatch'] =hatch
        item['alarm'] =alarm
        item['board_computer'] =board_computer
        item['hydraulics'] =hydraulics
        item['anti_skid'] =anti_skid
        item['chair_warming'] =chair_warming
        item['parking_control'] =parking_control
        item['rear_view_camera'] =rear_view_camera
        item['price'] =price
        item['description'] =description
        return item








