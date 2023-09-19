import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import sys
import psutil
import time
import logging

class MemoryMonitorService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MemoryMonitorService"
    _svc_display_name_ = "Memory Monitor Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_running = True
        # Configurar el registro
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            filename='memory_monitor_service.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        interval = 1
        while self.is_running:
            memory_info = psutil.virtual_memory()
            usage_percent = memory_info.percent
            print(f"Uso de memoria RAM: {usage_percent}%")
            # Registra el uso de memoria en el archivo de registro
            logging.info(f"Uso de memoria RAM: {usage_percent}%")
            time.sleep(interval)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MemoryMonitorService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MemoryMonitorService)
