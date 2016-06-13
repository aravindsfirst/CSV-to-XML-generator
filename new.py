from lxml import etree
import csv
import string
import sys
import pprint
import os
import subprocess

#with open(sys.argv[1],'r') as csvfile:

with open(sys.argv[1],'r') as csvfile:
	kek = csv.reader(csvfile, delimiter=',')
	Configuration = etree.Element('Configuration')
	csvDict = {}
	current = 0
	chapters = []
	lel = 0

	for line in kek:
		number = line[0]
		title = line[1]
		subtitle = ''.join(line[2:])
		if number:
			current = int(number)
			loltitle = title
			csvDict[title] = [subtitle]
		elif subtitle:
			csvDict[loltitle].append(subtitle)

		if title:
			chapters.append(title)


	


def slugify(stringy):
	return stringy.lower().replace(" ", "_").translate(None, ".,-'?!").replace("__", "_")

def mainblock(lol):
	Configuration = etree.Element('Configuration')
	Head = etree.Element('Head')
	ID = etree.Element('ID')
	ID.text=(slugify(lol))
	Description = etree.Element('Description', type="C")
	cdata = etree.CDATA('')
	Description.text = cdata
	Version = etree.Element('Version')
	Version.text=('')
	name = etree.Element('name')
	name.text = lol
	Icon = etree.Element('Icon', type="C")
	Icon.text=cdata
	Partner = etree.Element('Partner')
	Partner.text=('Specadel Technologies Private Limited')
	OptionalConfiguration = etree.Element('OptionalConfiguration')
	QP_Version = etree.Element('QP_Version')
	QP_Version.text=('2.0')
	MenuPosition = etree.Element('MenuPosition')
	MenuPosition.text = str(chapters.index(lol) + 1)

	Configuration.append(Head)
	Head.append(ID)
	Head.append(Description)
	Head.append(Version)
	Head.append(name)
	Head.append(Icon)
	Head.append(Partner)
	Head.append(OptionalConfiguration)
	OptionalConfiguration.append(QP_Version)
	OptionalConfiguration.append(MenuPosition)

	for i in range(0, len(csvDict[lol])):
		
		SubMenu = etree.Element('SubMenu')
		cdata = etree.CDATA('')
		ID2 = etree.Element('ID')
		ID2.text = slugify(lol) + str(i + 1)
		name2 = etree.Element('name')
		name2.text = csvDict[lol][i].rstrip()
		Icon2 = etree.Element('Icon', type='C')
		Icon2.text = cdata
		Description2 = etree.Element('Description', type='C')
		Description2.text = cdata
		Timer = etree.Element('Timer', type='N')
		Timer.text='60'
		path = etree.Element('path')
		path.text = ''
		Instruction = etree.Element('Instruction', type='C')
		Instruction.text = cdata
		OptionalConfiguration2 = etree.Element('OptionalConfiguration')
		FileType = etree.Element('FileType')
		FileType.text = 'VIDEO'

		Configuration.append(SubMenu)
		SubMenu.append(ID2)
		SubMenu.append(name2)
		SubMenu.append(Icon2)
		SubMenu.append(Description2)
		SubMenu.append(Timer)
		SubMenu.append(path)
		SubMenu.append(Instruction)
		SubMenu.append(OptionalConfiguration2)
		OptionalConfiguration2.append(FileType)

	doc = etree.ElementTree(Configuration)
	with open('settings_'+slugify(lol)+'.xml', 'w') as outfile:
		doc.write(outfile, pretty_print=True, encoding="UTF-8", xml_declaration=True)
	os.mkdir("module_"+slugify(lol))


#def subblock(lol, i):
	

	##Writing to XML file
	
	#doc = etree.ElementTree(Configuration)
	#outfile = open('filename.xml', 'w')
	#doc.write(outfile, pretty_print=True, encoding="UTF-8", xml_declaration=True)
def main():

	for Num in range(0, len(csvDict)):

		mainblock(chapters[Num])
			#print len(csvDict[chapters[Num]])
			##Writing to XML file
#pprint.pprint(csvDict)
main()
subprocess.call(['java', '-Dfile.encoding=UTF8 -jar', '/home/pisa/Downloads/Work/EncryptionTool/encryptdecrypt15042015.jar'])
#print csvDict['Heat']
#main()
#print len(csvDict['Heat'])