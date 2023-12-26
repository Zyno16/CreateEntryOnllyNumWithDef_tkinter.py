
from tools import *


frm = form()

Label(frm,text="Enter your name: ").pack(pady=10)

EntryOnlyNumber(frm).pack(pady=5)
EntryOnlyNumber(frm,True).pack(pady=5)
frm.mainloop()
