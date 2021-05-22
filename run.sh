#!/bin/bash
for ((i=1; i <= $1; i++));
do
  yarn jar "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming-3.1.4.jar \
        -files $(pwd)/mapper_authority.py,$(pwd)/reducer_authority.py \
        -input HITS/1_"$i" \
        -output HITS/2_"$i" \
        -mapper "python3 mapper_authority.py" \
        -reducer "python3 reducer_authority.py"
  yarn jar "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming-3.1.4.jar \
        -files $(pwd)/mapper_hub_counting.py,$(pwd)/reducer_hub_counting.py \
        -input HITS/2_"$i" \
        -output HITS/1_$((i+1)) \
        -mapper "python3 mapper_hub_counting.py" \
        -reducer "python3 reducer_hub_counting.py"
done
