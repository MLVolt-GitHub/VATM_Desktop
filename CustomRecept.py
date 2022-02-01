from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

class CustomRecept:
	def __init__(self, TI, BD, AN, AM, TC):

		self.TI = TI
		self.BD = BD
		self.AN = AN
		self.AM = AM
		self.TC = TC

		self.pdf = canvas.Canvas('test.pdf', pagesize=(13 * cm, 6.5 * cm))

		self.pdf.drawImage('Assets/vatm_logo.jpeg', 10, 150, width=50, height=25)

		self.pdf.drawImage('Assets/ashok_stambh.jpg', 330, 130, width=25, height=40)

		self.pdf.drawImage('Assets/rupee_symbol.jpeg', 330, 25, width=20, height=35)

		self.pdf.setFont('Times-Bold', 8)
		self.pdf.drawString(10, 120, "TRANSACTION ID : "+self.TI)

		self.pdf.setFont('Times-Bold', 8)
		self.pdf.drawString(10, 110, "BANK DETAILS : "+self.BD)

		self.pdf.setFont('Times-Bold', 8)
		self.pdf.drawString(10, 100, "AADHAR NO : "+self.AN)

		self.pdf.setFont('Times-Bold', 8)
		self.pdf.drawString(10, 90, "AMOUNT : "+self.AM)

		self.pdf.setFont('Times-Bold', 8)
		self.pdf.drawString(10, 80, "TRANSFER CODE : "+self.TC)

		self.pdf.save()



#CustomRecept("12345", "SBI", "8953982411", "4000", "0011")

