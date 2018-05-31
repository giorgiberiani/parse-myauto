import re

class MyAutoHelper:
    helper_respnse = None
 
    def get_customs(self):
        return self.helper_respnse.xpath('//*[@class="levy"]//text()').extract_first()
        

    def get_location(self):
        location = self.helper_respnse.xpath('//div[1]/ul/li[2]/span/text()').extract_first()
        return re.sub(' +',' ',location)

    def get_description(self):
        description = self.helper_respnse.xpath('//div[1]/div[5]/div[1]/div[2]/div/text()').extract_first()
        return re.sub(' +',' ',str(description))
    
    def get_price(self):
        return self.helper_respnse.xpath('//*[@class="car-price " or @class="car-price resized" or @class="no-fixed-price"]/text()').extract_first()
            
    def get_manufacturer(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[1]/th[1]/div[2]//text()').extract_first()

    def get_model(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[2]/th[1]/div[2]//text()').extract_first()

    def get_year(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[3]/th[1]/div[2]//text()').extract_first()
        
    def get_category(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[4]/th[1]/div[2]//text()').extract_first()

    def get_fuel_type(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[5]/th[1]/div[2]//text()').extract_first()

    def get_engine_volume(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[6]/th[1]/div[2]//text()').extract_first()

    def get_mileage(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[7]/th[1]/div[2]//text()').extract_first()

    def get_cylinders(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[8]/th[1]/div[2]//text()').extract_first()

    def get_gear_type(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[9]/th[1]/div[2]//text()').extract_first()
       
    def get_drive_wheels(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[10]/th[1]/div[2]//text()').extract_first()

    def get_doors(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[11]/th[1]/div[2]//text()').extract_first()
     
    def get_wheel(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[12]/th[1]/div[2]//text()').extract_first()

    def get_color(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[13]/th[1]/div[2]//text()').extract_first()

    def get_interior_color(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[14]/th[1]/div[2]//text()').extract_first()

    def get_airbags(self):
        return self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[15]/th[1]/div[2]//text()').extract_first()

    def get_abs(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[1]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_el_windows(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[2]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_air_condintioner(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[3]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_climate_system(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[4]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_leather_interior(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[5]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_disks(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[6]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_navigation_system(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[7]/th[2]/div[2]/i[@class="fa fa-check"]'):
             return 1
        else:
            return 0 

    def get_central_lock(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[8]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_hatch(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[9]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_alarm(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[10]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_board_computer(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[11]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_hydraulics(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[12]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_anti_skid(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[13]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_chair_warming(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[14]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_parking_control(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[15]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_rear_view_camera(self):
        if self.helper_respnse.xpath('//*[@class="detail-car-table"]//tr[16]/th[2]/div[2]/i[@class="fa fa-check"]'):
            return 1
        else:
            return 0

    def get_id(self):
        return self.helper_respnse.xpath('//*[@class="number"]/text()').extract_first()

    def get_time(self):
        return self.helper_respnse.xpath('//*[@class="number"]/text()').extract()[1]
        

