# Replace old mob_drop_item for better view

This script is for developers of private metin2 servers. 
Script simply replace strange group names related to incorrect encoding with new ones by searching the mob id trough **mob_names** file 
and past it to the group name in **mob_drop_item** file.

- In my case mob_drop_item is in .cpp format, but you can also use any other text format. 

- In script I used [unidecode](https://github.com/avian2/unidecode) - to make generated file more universal

- Tested on [Python 3.11.8 64-bit](https://www.python.org/downloads/release/python-3118/)

## Expected file structure:
*mob_drop_item.cpp*
```
Group	���ֹ���_Ǫ���θ����
{
	Type	kill
	Mob	134
	kill_drop	400
	1	5110	1	25	10
	2	290	1	15	10
}

Group	���ֹ���_���������
{
	Type	kill
	Mob	138
 [...]
```

## Result:
*mob_drop_item_generated.cpp*
```
Group	Przekl_Nieb_Alfa_Wilk
{
	Type	kill
	Mob	134
	kill_drop	400
	1	5110	1	25	10
	2	290	1	15	10
}


Group	Przeklety_Czerw_Dzik
{
	Type	kill
	Mob	138
[...]
```

## required mobs data generated from database

Scripts requires following structure of mob_names.txt file:

```
VNUM	LOCALE_NAME
101	Dziki Pies
102	Wilk
103	Alfa Wilk
104	Nieb. Wilk
[...]
```
I generated example mob_names.txt from my database.

## Additional arguments

You can set your own file paths by following:

*python generate.py --mob_names_file "your path" --input_file "your path"*

- when running script with no additional arguments, it use files from "/example" directory.

- for my testing purposes I created argument "--test_time", to test execution time of script.
