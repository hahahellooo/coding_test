f = open('readme1.txt', 'w+')
f.write("Gooooood Evening")
f.close()

f = open('readme2.txt', 'w+')
f.write("Gooooood Night")
f.close()

# # zip
# import zipfile

# comp_file = zipfile.ZipFile('com.zip','w')
# comp_file.write('readme1.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('readme2.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()

# # unzip
# zip_obj = zipfile.ZipFile('com.zip','r')
# zip_obj.extractall('extracted')

# 하위 디렉토리 파일 zip/unzip
import shutil
dir_to_zip = '/Users/jeongmieun/zip'
output = "folder_zip"
shutil.make_archive(output, 'zip', dir_to_zip)
shutil.unpack_archive(f"{output}.zip", "exxtarcted2", "zip")