first_argument=$1

if [ $first_argument == 'dev' ]
then
  uvicorn main:app --reload
fi

if [ $first_argument == 'test' ]
then
  pytest
fi
