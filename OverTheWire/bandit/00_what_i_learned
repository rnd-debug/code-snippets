
Find files of size 1000 bytes, output the results using "ls", then filter.
```
find / -1000c -ls | grep groupName
```

`uniq` will not detect duplicated lines if they are not adjacent : need to sort before.
```
cat file.txt | grep wordOnSameLine 
cat file.txt | uniq --count
cat data.txt | sort | uniq -u
```

Find specific TEXT pattern in a BINARY file : `cat data.txt | grep -a "====" `

To decode from b64 : ` base64 -d toto.txt `

Transform chars:
```
echo "a" | tr [:lower:] [:upper:]
cat data.txt | tr 'a-z' 'n-za-m' | tr 'A-Z' 'N-ZA-M'
```

Create temporary file or dir
```
mktemp 
mktemp -d 
```

Convert hexdump to binary: ` xxd -r -p  hexdump.hex`

Decompress/Extract files from archive:
```
  tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
  
  tar -tvf archive.tar         # List all files in archive.tar verbosely.
  tar -xf archive.tar          # Extract all files from archive.tar.

  bzip2 -d toto.bz2
  gzip -dc toto.gz
```