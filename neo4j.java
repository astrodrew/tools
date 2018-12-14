package neo4jtest;

import org.neo4j.driver.v1.Statement;
import org.neo4j.driver.v1.*;
import java.io.*;

public class Test1 {
    public static void main(String args[]){

        String creatSql = null;
        Statement stmt = null; //采用预编译，和关系数据库不一样的是,参数需要使用{1},{2},而不是?
        File file = new File("E:/code/ml/xmly/data/yhtest.txt");
        BufferedReader reader = null;
        Driver driver = GraphDatabase.driver( "bolt://139.199.172.101:7687", AuthTokens.basic( "neo4j", "astro8023" ) );
        Session session = driver.session();
        try {
            reader = new BufferedReader(new FileReader(file));
            while ((creatSql = reader.readLine()) != null) {
                System.out.println(creatSql);
                session.run( creatSql);
            }
        } catch (FileNotFoundException e) {
                e.printStackTrace();
            }catch (IOException e) {
            e.printStackTrace();
        }
        session.close();
        driver.close();
    }
}
