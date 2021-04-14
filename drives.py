import json

class Error(Exception):
   """Base class for other exceptions"""
   pass

class EmptyDrivesArray(Error):
   """Fethcing info from empty drives array"""
   pass



class Drive:

    def __init__(self, data):
        self.drive_data = {}
        if type(data) is dict:
            self.drive_data = data
        else:
            data_list = data.split(',')
            for item in data_list:
                tmp_data = item.split()
                if tmp_data[0] == 'disks':
                    self.drive_data[tmp_data[0]] = tmp_data[1:]
                else:
                    self.drive_data[tmp_data[0]] = ' '.join(tmp_data[1:])

    def __oldinit(self, id, data):
        self.id = id
        self.drive_data = {}
        data_list = data.split(',')
        for item in data_list:
            tmp_data = item.split()
            self.drive_data[tmp_data[0]] = ' '.join(tmp_data[1:])

    def dprint(self):
       return self.drive_data

    def drive_offline(self):
        if self.drive_data['status'] == 'Offline':
            return True
        else:
            return False
       

class DrivesArray:
    
    def __init__(self, data=None):
        self.drives = []
        if data is None:
            # Read data from the file
            try:
                self.__read_drives()
            except EmptyDrivesArray:
                raise
        else:
            # disks = json.loads(data)
            for key in data.keys():
                self.add_drive(data[key])
            self.__save_drives()
    
    def add_drive(self, data):
        drive = Drive(data)
        self.drives.append(drive)
        
    def show_drives(self, status=None):

        outdrive = []
        for drive in self.drives:
            if status == 'Offline':
                if drive.drive_offline():
                    outdrive.append(drive.dprint())
            else:
                outdrive.append(drive.dprint())
                
        return outdrive
            
    def __save_drives(self):

        f = open('/tmp/drives_data.json', 'w')
        data = self.show_drives()
        j = json.dumps(data, indent = 4)
        f.write(j)
        f.close()

    def __read_drives(self):

        try:
            with open('/tmp/drives_data.json') as f:
                content = f.read()
            f.close()
            d = json.loads(content)
            for disk in d:
                self.add_drive(disk)
        except FileNotFoundError:
            raise EmptyDrivesArray()
    
            

    
    
