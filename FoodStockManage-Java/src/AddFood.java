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
		System.out.println("ʳƷ��ӳɹ�");
	}
	void foodMessage(int id) {
		int i;
		for(i=0;i<foodList.size();i++) {
			Food food=(Food)foodList.get(i);
			if(food.getId()==(id)) {
				System.out.println("ʳƷ��ϢΪ:");
				System.out.println("���\t"+"����\t"+"�۸�");
				System.out.println(id+"\t"+food.getName()+"\t"+food.getPrice());
				System.out.println("ʳƷ��Ϣ��ѯ���");
				break;
			}
		}
		if(i==foodList.size()) {
			System.out.println("û���ҵ�ָ����ŵ�ʳƷ");

		}
	}
	void changePrice(int id,double price) {
		int i;
		for(i=0;i<foodList.size();i++) {
			Food food=(Food)foodList.get(i);
			if(food.getId()==(id)) {
				food.setPrice(price);
				System.out.println("���Ϊ"+id+"��ʳƷ�۸��޸�Ϊ"+price);

			}
		}
		if(i==foodList.size()) {
			System.out.println("û���ҵ�ָ����ŵ�ʳƷ");
		}
		
		
	}
	void delFood(int id) {
		int i;
		for(i=0;i<foodList.size();i++) {
			Food food=(Food)foodList.get(i);
			if(food.getId()==(id)) {
				foodList.remove(i);
				System.out.println("�Ƴ��ɹ�");

			}
		}
		if(i==foodList.size()) {
			System.out.println("û���ҵ�ָ����ŵ�ʳƷ");
		}
		
	}
	
}
