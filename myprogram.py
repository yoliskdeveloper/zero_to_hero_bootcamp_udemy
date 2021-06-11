from mymodule import my_func
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import my_sub_script

# my_func()     # call module from single file
some_main_script.report_main()  # call module "report_main" from file some_main_script inside directory "MyMainPackage"

my_sub_script.sub_report() # call module 'sub_report' from file "my_sub_script" inside directory "SubPackage" inside
# directory "MyMainPackage"
