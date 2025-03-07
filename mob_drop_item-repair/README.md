Script for replacing wrong encoded group names in mob_drop_item.txt file into human-readable format.
Script replace names by searching the mob id trough **mob_names** file and past it to the group name in **mob_drop_item** file.

Tested on [Python 3.11.8 64-bit](https://www.python.org/downloads/release/python-3118/)

## Expected file structure:
*mob_drop_item.txt*
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
*mob_drop_item_generated.txt*
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

I added the ability to set your own file paths by following:

*python generate.py --mob_names_file "your path" --input_file "your path"*

- when running script with no additional arguments, it use files from "/example" directory.

- for my testing purposes I created argument "--test_time", to test execution time of script.
