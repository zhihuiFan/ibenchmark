export PSQL=/u01/yizhi/bin/xora/bin/psql
export DBNAME=imdb
export PGPORT=9967

mkdir -p logs
mkdir -p png
for fn in `ls sql/[0-9]*.sql`
do
echo "Working on $fn"
$PSQL $DBNAME -p $PGPORT -q -X <<EOF >logs/`basename $fn`.analyze.log
    load 'aqo';
    set aqo.mode = learn ;
    \i $fn
    \i $fn
    \i $fn
    \i $fn
    \i $fn
    \i $fn
    \i $fn
    \i $fn
    \i $fn
    \i $fn
EOF
done




	   
	   
