name="$1"
if [ "$name" == "name" ]; then
	echo -e "\033[35m 你好！\033[0m"
fi
parm=${name:-cxp}
echo -e "$parm"

str1=${name1:-cxp}
echo -e "$str1"

path="../python"
if [ ! -d "$path" ]; then
	mkdir "$path"
else
	echo -e "\033[35m Your folder has been existed!\033[0m"
fi

git diff --cached --name-only HEAD -> log.txt