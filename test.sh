for i in $(seq 1 10);
do
  curl http://127.0.0.1:5000/
  sleep 0.25
done