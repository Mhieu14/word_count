* Mô tả:
- Demo Map Reduce, sử dụng Python và Hadoop Steam
- Thực hiện chạy Hadoop trên máy ảo Cloudera, sử dụng Docker

* Thực hiện:
Bước 1: Pull và run Image cloudera/quickstart từ Docker
- docker pull Cloudera/quickstart:latest 
- docker run --hostname=quickstart.cloudera --privileged=true -t -i -v /PATH/TO/MOUNT/FORDER: src -p 8888:8888 -p 80:80 -p 7180:7180 cloudera/quickstart /usr/bin/docker-quickstart
  Note: /PATH/TO/MOUNT/FORDER là đường dẫn tới thư mục chứ code và dữ liệu

Bước 2: Copy dữ liệu vào hdfs, cấp quyền truy cập vào mapper.py và reducer.py cho hadoop
- chmod 777 mapper.py reducer.py
- hdfs dfs -mkdir /word_count_in_python
- hdfs dfs -copyFromLocal /src/word_count_data.txt /word_count_in_python

Bước 3: Thực hiện Map Reduce, copy file kết quả về local
- hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /word_count_in_python/word_count_data_kmer.txt -output /word_count_in_python/output_kmer -file /src/mapper_k_mer.py -mapper "python /src/mapper_k_mer.py" -file /src/reducer.py -reducer "python /src/reducer.py"
- hdfs dfs -copyToLocal /word_count_in_python/output_kmer/part-00000 /src/output_kmer
  Note: File mapper của bài 1 là mapper.py, của bài 2 là mapper_k_mer.py, 2 bài sử dụng chung reducer

* Kết quả bài 1: Top 10 từ có tần suất lớn nhất (sort -k2,2n output/part-00000)

- he      17087
- my      17312
- a       23504
- in      24350
- that    24407
- i       30240
- to      33929
- of      53121
- and     79182
- the     93739

Kết quả bài 2: Top 10 9-mers xuất hình hiện nhiều nhất (sort -k2,2n output_kmer/part-00000) 

- CCGCCAGCA       199
- TGGCGCTGG       200
- GCCAGCGCC       207
- CGCCAGCGC       211
- CTGGCGCTG       212
- CGCTGGCGG       219
- CGCCAGCAG       220
- GCGCTGGCG       234
- CAGCGCCAG       247
- CCAGCGCCA       252