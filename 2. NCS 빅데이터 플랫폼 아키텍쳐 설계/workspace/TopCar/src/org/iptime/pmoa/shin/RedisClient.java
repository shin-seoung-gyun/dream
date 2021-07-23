package org.iptime.pmoa.shin;

import java.util.Set;
import java.util.concurrent.TimeUnit;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.Tuple;

public class RedisClient {

	public static void main(String[] args) throws Exception {
		JedisPoolConfig jedisPoolConfig = new JedisPoolConfig();
		JedisPool jPool = new JedisPool(jedisPoolConfig, "server02.hadoop.com", 6379);
		Jedis jedis = jPool.getResource();
		
//		Set<String> list = jedis.smembers("abc");
//		for(String temp : list) {
//			System.out.println(temp);
//		}
		long count = 1;
		while(true) {
			
			Set<Tuple> list = jedis.zrevrangeWithScores("TopCar", 0, -1);
			int i =1;
			System.out.println("");
			System.out.println(count + "번째 확인");
			for(Tuple rank : list) {
				System.out.println(i++ +"등"+ rank.getElement()+ ","+ (int)rank.getScore());
			}
			count++;
			//delay
			TimeUnit.SECONDS.sleep(5);
		}
		
	}

}
