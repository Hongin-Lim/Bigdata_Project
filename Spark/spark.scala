// shell 실행
spark-shell --master local[4] --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1,org.apache.kafka:kafka_2.13:3.1.0 --jars kafka-clients-3.1.0.jar,commons-pool2-2.11.1.jar,spark-token-provider-kafka-0-10_2.12-3.2.1.jar

// import
import org.apache.spark._
import org.apache.spark.sql.Row
import org.apache.spark.sql.Column
import org.apache.spark.streaming._
import spark.implicits._
import org.apache.spark.sql.functions.get_json_object
import org.apache.spark.sql.types._

// read kafka topic data
val df = spark.read.format("kafka").
    option("subscribe", "final_logdata").
    option("kafka.bootstrap.servers", "192.168.182.19:9092").
    load()
df.show(false)

//tostring
val toStr = udf((payload: Array[Byte]) => new String(payload))
val parsing = df.withColumn("value", toStr(df("value")))
val df2 = parsing.drop("key", "topic", "partition", "timestampType", "offset", "timestamp")
df2.printSchema
df2.show(false)

// structType
import org.apache.spark.sql.types.{StringType, StructType}
val schema = new StructType().add("time", StringType, true).add("order_num", StringType, true).add("user_num", StringType, true).add("item", StringType, true).add("item_ea", StringType, true)

val df3 = df2.withColumn("value",from_json(col("value"),schema))
df3.printSchema()
df3.show(false)

val df4=df3.select(col("value.*"))
df4.printSchema()
df4.show(false)

// window function
import org.apache.spark.sql.functions._
import org.apache.spark.sql.expressions.Window

val windowitem  = Window.partitionBy("item").orderBy("item_ea")
val df5 = df4.withColumn("row_number",row_number.over(windowitem))
df5.show

val windowitemAgg  = Window.partitionBy("item")

val df6 = df5.withColumn("row",row_number.over(windowitem)).withColumn("sum", sum(col("item_ea")).over(windowitemAgg)).withColumn("min", min(col("item_ea")).over(windowitemAgg)).withColumn("max", max(col("item_ea")).over(windowitemAgg)).where(col("row")===1).select("item","sum","min","max").orderBy(desc("sum"))
df6.show
