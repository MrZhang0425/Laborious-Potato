import java.util.*;

public class AddFood {
	private ArrayList foodList=null;
	AddFood(){
		foodList=new ArrayList();
	}
	void addFood(int id,String name,double price) {
		Food food=new Food();
		food.setId(id);
		food.setName(name);
		food.setPrice(price);
		foodList.add(food);	
		System.out.println("食品添加成功");
	}
	void foodMessage(int id) {
		int i;
		for(i=0;i<foodList.size();i++) {
			Food food=(Food)foodList.get(i);
			if(food.getId()==(id)) {
				System.out.println("食品信息为:");
				System.out.println("编号\t"+"名字\t"+"价格");
				System.out.println(id+"\t"+food.getName()+"\t"+food.getPrice());
				System.out.println("食品信息查询完毕");
				break;
			}
		}
		if(i==foodList.size()) {
			System.out.println("没有找到指定编号的食品");

		}
	}
	void changePrice(int id,double price) {
		int i;
		for(i=0;i<foodList.size();i++) {
			Food food=(Food)foodList.get(i);
			if(food.getId()==(id)) {
				food.setPrice(price);
				System.out.println("编号为"+id+"的食品价格修改为"+price);

			}
		}
		if(i==foodList.size()) {
			System.out.println("没有找到指定编号的食品");
		}
		
		
	}
	void delFood(int id) {
		int i;
		for(i=0;i<foodList.size();i++) {
			Food food=(Food)foodList.get(i);
			if(food.getId()==(id)) {
				foodList.remove(i);
				System.out.println("移除成功");

			}
		}
		if(i==foodList.size()) {
			System.out.println("没有找到指定编号的食品");
		}
		
	}
	
}
