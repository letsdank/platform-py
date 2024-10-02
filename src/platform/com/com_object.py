
import win32com.client
import pythoncom

class COMObject:
    def __init__(self, name):
        self.name = name
        com_obj = win32com.client.Dispatch(name, pythoncom.CoInitialize())
        good_ones = []

        for key in dir(com_obj):
            method = getattr(com_obj, key)
            if "<COMObject" in str(method) and not "CDispatch." in str(method) and str(type(method)) == "<class 'method'>":
                # print(type(method), method)
                good_ones.append(key)
                setattr(self, key, method)

        # TODO: Make debug logging
        print(f"Imported {len(good_ones)} methods from COM Object {name}:\n * " + "\n * ".join(good_ones))
