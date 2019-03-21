#coding=utf-8

#��������� �������� �� AIP

import os
import errno
import shutil
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

source_path = "C:/AIP/"
destination_path = "C:/AIP01/"

#�������� �����, ���� � �� ����������
def make_dir_if_not_exists(path):
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

#����������� �����, ���� �� ���������� � ���������� �������� �����
def copy_pdf(path1, path2):
	if os.path.exists(path1):
		shutil.copy(path1,path2)
		#print path2
	else:
		print "����� "+path1+ "�� ����������"
		raise SystemExit(1)
			
#����������� ���� PDF ������ �� ����� � 1 ����			
def merge_pdf(dir,out_file):
	in_filenames = os.listdir(dir)
	if in_filenames:
		merger = PdfFileMerger()
		for filename in in_filenames:
#			f = open(dir+filename, 'rb+')
#			f.write("")
#			f.close()		
			if filename.find("eng") != -1: continue #����������� ����� �� ���������� ����� (� �������� ������� ���� eng)
			ext = filename.split('.')[-1]
			if ext == "pdf": #���������, ����� ���� ��� � ����������� PDF
				try:
					merger.append(PdfFileReader(file(dir+filename, 'rb')))
				except:
					print "Can't merge file "+filename
					continue
			else: continue
		merger.write(out_file)
	#print out_file

def airports(code):
	name=code
	return name
			
		
#���������, ����� � �������� ����� ���� 3 �������:
i=0
names = os.listdir(source_path) 
for name in names:
    i=i+1
if i != 3:
	print "�������� ����� �������� ������ ��� ������ 3 ��������"
	raise SystemExit(1)

#������ ������ ����� � �������� ���� pdf, �������������� ������ ��
make_dir_if_not_exists(destination_path)
book_dir = "����� 1/"
make_dir_if_not_exists(destination_path+book_dir)

merge_pdf(source_path+"1/aic/",destination_path+book_dir+"���������.pdf")
merge_pdf(source_path+"1/amdt/",destination_path+book_dir+"��������.pdf")
merge_pdf(source_path+"1/sup/",destination_path+book_dir+"����������.pdf")
copy_pdf(source_path+"1/notam/notam_rus.pdf",destination_path+book_dir+"�����.pdf")

part_dir = "����� 1. GEN/"
make_dir_if_not_exists(destination_path+book_dir+part_dir)
merge_pdf(source_path+"1/aip/gen/gen0/",destination_path+book_dir+part_dir+"GEN 0. ����� ��������.pdf")
merge_pdf(source_path+"1/aip/gen/gen1/",destination_path+book_dir+part_dir+"GEN 1. ������������ ������� � ����������.pdf")
merge_pdf(source_path+"1/aip/gen/gen2/",destination_path+book_dir+part_dir+"GEN 2. ������� � ����.pdf")
merge_pdf(source_path+"1/aip/gen/gen3/",destination_path+book_dir+part_dir+"GEN 3. ������������.pdf")
merge_pdf(source_path+"1/aip/gen/gen4/",destination_path+book_dir+part_dir+"GEN 4. ����������� ����� � ����� �� ����������������� ������������.pdf")

part_dir = "����� 2. ENR/"
make_dir_if_not_exists(destination_path+book_dir+part_dir)
copy_pdf(source_path+"1/aip/enr/enr0/1-enr0-6-rus.pdf",destination_path+book_dir+part_dir+"ENR 0. ���������� ����� 2.pdf")
merge_pdf(source_path+"1/aip/enr/enr1/",destination_path+book_dir+part_dir+"ENR 1. ����� ������� � ���������.pdf")
merge_pdf(source_path+"1/aip/enr/enr2/",destination_path+book_dir+part_dir+"ENR 2. ��������� ������������ ���.pdf")
merge_pdf(source_path+"1/aip/enr/enr3/",destination_path+book_dir+part_dir+"ENR 3. �������� ���.pdf")
merge_pdf(source_path+"1/aip/enr/enr4/",destination_path+book_dir+part_dir+"ENR 4. ������������������ ��������, �������.pdf")
merge_pdf(source_path+"1/aip/enr/enr5/",destination_path+book_dir+part_dir+"ENR 5. ������������� ��������������.pdf")
tmp_dir = "ENR 6. ���������� �����/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir)
copy_pdf(source_path+"1/aip/enr/enr6/1-enr6-1.pdf",destination_path+book_dir+part_dir+tmp_dir+"ENR 6. ������� ���� ��������� ����.pdf")

map_dir = "1/aip/enr/enr6/enr6-01/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	if i==13: i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+"�� "+str(i)+".pdf")


part_dir = "����� 3. AD/"
make_dir_if_not_exists(destination_path+book_dir+part_dir)
copy_pdf(source_path+"1/aip/ad/ad0/1-ad0-6-rus.pdf", destination_path+book_dir+part_dir+"AD 0. ���������� ����� 3.pdf")
merge_pdf(source_path+"1/aip/ad/ad1/",destination_path+book_dir+part_dir+"AD 1. �������� � ����������.pdf")
tmp_dir = "AD 2. ���������/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir)
tmp_dir1 = "AD 2.1. ������������� ��������� ���������� ���������/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)

map_dir = "1/aip/ad/ad2/rus/"
dirs = os.listdir(source_path+map_dir)
for dir in dirs:
	#print dir
	merge_pdf(source_path+map_dir+dir+"/", destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+airports(dir)+".pdf")

tmp_dir1 = "AD 2.3. ��������� ���/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)

tmp_dir2 = "AD 2.3.4. �����������/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+tmp_dir2)

map_dir = "1/aip/ad/ad2/tjk/"
dirs = os.listdir(source_path+map_dir)
for dir in dirs:
	#print dir
	merge_pdf(source_path+map_dir+dir+"/", destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+tmp_dir2+airports(dir)+".pdf")

tmp_dir2 = "AD 2.3.5. ������������/"	
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+tmp_dir2)

map_dir = "1/aip/ad/ad2/tkm/"
dirs = os.listdir(source_path+map_dir)
for dir in dirs:
	#print dir
	merge_pdf(source_path+map_dir+dir+"/", destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+tmp_dir2+airports(dir)+".pdf")

book_dir = "����� 2/"
make_dir_if_not_exists(destination_path+book_dir)

merge_pdf(source_path+"2/aic/",destination_path+book_dir+"���������.pdf")
merge_pdf(source_path+"2/amdt/",destination_path+book_dir+"��������.pdf")
merge_pdf(source_path+"2/sup/",destination_path+book_dir+"����������.pdf")
copy_pdf(source_path+"2/notam/2-notam_rus.pdf",destination_path+book_dir+"�����.pdf")

part_dir = "����� 1. GEN/"
make_dir_if_not_exists(destination_path+book_dir+part_dir)

merge_pdf(source_path+"2/aip/gen/gen0/",destination_path+book_dir+part_dir+"GEN 0. ����� ��������.pdf")
merge_pdf(source_path+"2/aip/gen/gen1/",destination_path+book_dir+part_dir+"GEN 1. ������������ ������� � ����������.pdf")
merge_pdf(source_path+"2/aip/gen/gen2/",destination_path+book_dir+part_dir+"GEN 2. ������� � ����.pdf")
merge_pdf(source_path+"2/aip/gen/gen3/",destination_path+book_dir+part_dir+"GEN 3. ������������.pdf")
merge_pdf(source_path+"2/aip/gen/gen4/",destination_path+book_dir+part_dir+"GEN 4. ����������� ����� � ����� �� ����������������� ������������.pdf")

part_dir = "����� 2. ENR/"
make_dir_if_not_exists(destination_path+book_dir+part_dir)
copy_pdf(source_path+"2/aip/enr/enr0/2-enr0-6-rus.pdf",destination_path+book_dir+part_dir+"ENR 0. ���������� ����� 2.pdf")
merge_pdf(source_path+"2/aip/enr/enr1/",destination_path+book_dir+part_dir+"ENR 1. ����� ������� � ���������.pdf")
merge_pdf(source_path+"2/aip/enr/enr2/",destination_path+book_dir+part_dir+"ENR 2. ��������� ������������ ���.pdf")
merge_pdf(source_path+"2/aip/enr/enr3/",destination_path+book_dir+part_dir+"ENR 3. �������� ���.pdf")
merge_pdf(source_path+"2/aip/enr/enr4/",destination_path+book_dir+part_dir+"ENR 4. ������������������ ��������, �������.pdf")
merge_pdf(source_path+"2/aip/enr/enr5/",destination_path+book_dir+part_dir+"ENR 5. ������������� ��������������.pdf")
tmp_dir = "ENR 6. ���������� �����/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir)
copy_pdf(source_path+"2/aip/enr/enr6/2-enr6-1.pdf",destination_path+book_dir+part_dir+tmp_dir+"ENR 6. ������� ���� ��������� ����.pdf")

map_dir = "2/aip/enr/enr6/enr6-01/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	if i==13: i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+"�� "+str(i)+".pdf")

part_dir = "����� 3. AD/"
make_dir_if_not_exists(destination_path+book_dir+part_dir)
copy_pdf(source_path+"2/aip/ad/ad0/2-ad0-6-rus.pdf", destination_path+book_dir+part_dir+"AD 0. ���������� ����� 3.pdf")
merge_pdf(source_path+"2/aip/ad/ad1/",destination_path+book_dir+part_dir+"AD 1. �������� � ����������.pdf")
tmp_dir = "AD 2. ���������/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir)
tmp_dir1 = "AD 2.1. ��������� ������ �, �, �/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)

map_dir = "2/aip/ad/ad2/"
dirs = os.listdir(source_path+map_dir)
for dir in dirs:
	#print dir
	merge_pdf(source_path+map_dir+dir+"/", destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+airports(dir)+".pdf")


book_dir = "����� 4/"
make_dir_if_not_exists(destination_path+book_dir)

merge_pdf(source_path+"4/aic/",destination_path+book_dir+"���������.pdf")
merge_pdf(source_path+"4/amdt/",destination_path+book_dir+"��������.pdf")
merge_pdf(source_path+"4/sup/",destination_path+book_dir+"����������.pdf")
copy_pdf(source_path+"4/notam/notam.pdf",destination_path+book_dir+"�����.pdf")
copy_pdf(source_path+"4/aip/4-aip-0.0-1.pdf",destination_path+book_dir+"����������.pdf")

part_dir = "����� 1. GEN/"
make_dir_if_not_exists(destination_path+book_dir+part_dir)

merge_pdf(source_path+"4/aip/gen/gen0/",destination_path+book_dir+part_dir+"GEN 0. ����� ��������.pdf")
merge_pdf(source_path+"4/aip/gen/gen1/",destination_path+book_dir+part_dir+"GEN 1. ������������ �������.pdf")
merge_pdf(source_path+"4/aip/gen/gen2/",destination_path+book_dir+part_dir+"GEN 2. ������� � ����.pdf")
merge_pdf(source_path+"4/aip/gen/gen3/",destination_path+book_dir+part_dir+"GEN 3. ������������.pdf")
merge_pdf(source_path+"4/aip/gen/gen4/",destination_path+book_dir+part_dir+"GEN 4. �����.pdf")

part_dir = "����� 2. ENR/"
make_dir_if_not_exists(destination_path+book_dir+part_dir)
copy_pdf(source_path+"4/aip/enr/enr0/4-enr-0.6.pdf",destination_path+book_dir+part_dir+"ENR 0. ���������� ����� 2.pdf")
merge_pdf(source_path+"4/aip/enr/enr1/",destination_path+book_dir+part_dir+"ENR 1. ����� ������� � ���������.pdf")
merge_pdf(source_path+"4/aip/enr/enr2/",destination_path+book_dir+part_dir+"ENR 2. ��������� ������������ ���.pdf")
merge_pdf(source_path+"4/aip/enr/enr3/",destination_path+book_dir+part_dir+"ENR 3. �������� ���.pdf")
merge_pdf(source_path+"4/aip/enr/enr4/",destination_path+book_dir+part_dir+"ENR 4. ������������������ ��������, �������.pdf")
merge_pdf(source_path+"4/aip/enr/enr5/",destination_path+book_dir+part_dir+"ENR 5. ������������� ��������������.pdf")
tmp_dir = "ENR 6. ���������� �����/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir)
copy_pdf(source_path+"4/aip/enr/enr6/4-enr-6-3.pdf",destination_path+book_dir+part_dir+tmp_dir+"ENR 6.3 ������� ����.pdf")
copy_pdf(source_path+"4/aip/enr/enr6/4-enr-6-1.pdf",destination_path+book_dir+part_dir+tmp_dir+"ENR 6.1 ��������.pdf")

tmp_dir1 = "�� �����-�������������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-SPB/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")

tmp_dir1 = "�� ����������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-MOS/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")	

tmp_dir1 = "�� ����������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-ROS/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")	

tmp_dir1 = "�� ���������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-SAM/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")	

tmp_dir1 = "�� ����������������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-EKB/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")

tmp_dir1 = "�� �������������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-NOW/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")	

tmp_dir1 = "�� ������������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-KRS/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")	

tmp_dir1 = "�� ���������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-IRK/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")	

tmp_dir1 = "�� ������������ ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-HAB/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")

tmp_dir1 = "�� ������������ ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-MAG/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")	

tmp_dir1 = "�� �������������-����������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-PTK/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")

tmp_dir1 = "�� ��������� ��/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir+tmp_dir1)
map_dir = "4/aip/enr/enr6/enr6-01/4-YAK/"
maps = os.listdir(source_path+map_dir)
i=0
for map in maps:
	i=i+1
	copy_pdf(source_path+map_dir+map, destination_path+book_dir+part_dir+tmp_dir+tmp_dir1+"���� "+str(i)+".pdf")
	

part_dir = "����� 3. AD/"

make_dir_if_not_exists(destination_path+book_dir+part_dir)
copy_pdf(source_path+"4/aip/ad/ad0/4-ad-0.6.pdf", destination_path+book_dir+part_dir+"AD 0. ���������� ����� 3.pdf")
merge_pdf(source_path+"4/aip/ad/ad1/",destination_path+book_dir+part_dir+"AD 1. ��������.pdf")
tmp_dir = "AD 2. ��������� �, �, �/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir)
map_dir = "4/aip/ad/ad2/"
dirs = os.listdir(source_path+map_dir)
for dir in dirs:
	#print dir
	merge_pdf(source_path+map_dir+dir+"/", destination_path+book_dir+part_dir+tmp_dir+airports(dir)+".pdf")

tmp_dir = "AD 3. ����������/"
make_dir_if_not_exists(destination_path+book_dir+part_dir+tmp_dir)
map_dir = "4/aip/ad/ad3/"
dirs = os.listdir(source_path+map_dir)
for dir in dirs:
	#print dir
	merge_pdf(source_path+map_dir+dir+"/", destination_path+book_dir+part_dir+tmp_dir+airports(dir)+".pdf")

copy_pdf(source_path+"4/aip/ad/ad4/4-ad-4.1.pdf", destination_path+book_dir+part_dir+"AD 4. ������ ���������.pdf")	
