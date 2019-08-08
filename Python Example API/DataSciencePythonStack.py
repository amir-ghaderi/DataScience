import win32service  
import win32serviceutil  
import win32event
import subprocess
  
class StellaWindowsService(win32serviceutil.ServiceFramework):  
    # this is the service name to NET START/STOP
    _svc_name_ = "ApplicationImpactModel"  
    # this is the service name in the Service Control Manager(SCM)  
    _svc_display_name_ = "API for Impact Model"  
    # this text shows up as the description in the SCM  
    _svc_description_ = "This service runs the Impact Model API"  
      
    def __init__(self, args):  
        win32serviceutil.ServiceFramework.__init__(self,args)  
        # create an event to listen for stop requests on  
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
      
    # core logic of the service     
    def SvcDoRun(self):    
        p=subprocess.Popen(["python","F:\\Flask Stack\\ImpactModel\\app.py"]) 
        closeCmd = None  
          
        # if the stop event hasn't been fired keep looping  
        while closeCmd != win32event.WAIT_OBJECT_0:  
            # block for 5 seconds and listen for a stop event  
            closeCmd = win32event.WaitForSingleObject(self.hWaitStop, 5000)  
              
        p.kill()

    # called when we're being shut down      
    def SvcStop(self):  
        # tell the SCM we're shutting down  
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)  
        # fire the stop event  
        win32event.SetEvent(self.hWaitStop)  
          
if __name__ == '__main__':  
    win32serviceutil.HandleCommandLine(StellaWindowsService)  
