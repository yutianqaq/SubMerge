# 子域名去重、合并工具

## 帮助
```bash
python SubMerge.py -h                                 
usage: SubMerge.py [-h] [-D FILENAME] [-m FILE1 FILE2] [-d DIRECTORY] [-o OUTPUT_FILE]

Subdomain Deduplication and File Merge

options:
  -h, --help            show this help message and exit
  -D FILENAME, --deduplicate FILENAME
                        perform subdomain deduplication on the specified file
  -m FILE1 FILE2, --merge FILE1 FILE2
                        merge the contents of two files
  -d DIRECTORY, --directory DIRECTORY
                        perform subdomain deduplication on the files in the specified directory
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        output file for the results
```

## 使用方法
### 合并
#### 两个文件合并

```bash
┌──(kali㉿kali)-[~/SubMerge]
└─$ cat domain1.txt domain2.txt
example.com
www.example.com
example.com
test.example.com    

┌──(kali㉿kali)-[~/SubMerge]
└─$ python SubMerge.py -m domain1.txt domain2.txt         
Please provide an output file using the -o/--output option.

┌──(kali㉿kali)-[~/SubMerge]
└─$ python SubMerge.py -m domain1.txt domain2.txt -o output.txt
Merged domain1.txt and domain2.txt into output.txt.

┌──(kali㉿kali)-[~/SubMerge]
└─$ cat output.txt             
example.com
www.example.com
example.com
test.example.com 
```
#### 多个文件见合并
将多个文件放入目录，然后合并到一个文件中
```bash
┌──(kali㉿kali)-[~/SubMerge]
└─$ ls domains 
doamin3.txt  domain1.txt  domain2.txt
                                     
┌──(kali㉿kali)-[~/SubMerge]
└─$ python SubMerge.py -d domains -o merge_example_com.txt     
Read 5 subdomains from files in directory domains.
Total domains: 5
Merged subdomains from files in directory domains into merge_example_com.txt.

┌──(kali㉿kali)-[~/SubMerge]
└─$ cat merge_example_com.txt 
email.example.com
example.com
login.example.com
test.example.com
www.example.com
```

### 去重
读入一个文件，将去重结果输出
```
┌──(kali㉿kali)-[~/SubMerge]
└─$ cat doamin.txt 
test.com
test.com
home.test.com 
                                                                   
┌──(kali㉿kali)-[~/SubMerge]
└─$ python SubMerge.py -D doamin.txt -o doamin_output.txt
Read 2 subdomains from doamin.txt.
Total domains: 2

┌──(kali㉿kali)-[~/SubMerge]
└─$ cat doamin_output.txt 
home.test.com
test.com

```



