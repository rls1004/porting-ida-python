# porting-ida-python

porting IDA python script 6.x-7.3 to 7.4

## Usage
```bash
$ python porting-ida-python.py [file]
```

## Example
```bash
$ python porting-ida-python.py test.py
.startEA -> .start_ea
.SETPROC_ALL -> .SETPROC_LOADER_NON_FATAL
.autoWait -> .auto_wait
.AnalyzeArea -> .plan_and_wait
.MakeName(func.start_ea, "_panic") -> .set_name(func.start_ea,  "_panic",  idc.SN_CHECK)
.MakeName(func.start_ea, "_do_printf") -> .set_name(func.start_ea,  "_do_printf",  idc.SN_CHECK)
.GetSegmentAttr -> .get_segm_attr
.GetMnem -> .print_insn_mnem
.MakeFunction -> .add_func
.GetFlags -> .get_full_flags
.GetOpnd -> .print_operand
.FindBinary -> .find_binary
[+] create: ida7_test.py
```
