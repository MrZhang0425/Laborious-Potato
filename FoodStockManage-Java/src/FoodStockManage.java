import java.util.*;
public class FoodStockManage {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		AddFood af=new AddFood();
		while(true) {
			System.out.println("-----����ʾѡ��һ�¹���-----");
			System.out.println("-----���ʳƷ�밴1");
			System.out.println("----��ѯʳƷ��Ϣ��2");
			System.out.println("----�޸�ʳƷ�۸�3");
			System.out.println("-------ɾ��ʳƷ��4");
			System.out.println("----------�˳���0\n\n");
			System.out.println(">>>>>>>��ѡ��<<<<<<<");
			
			int a=input.nextInt();
			if(a==1) {
				// ���ʳƷ
				System.out.println("-----����ʳƷ���:");
				int id=input.nextInt();
				System.out.println("-----����ʳƷ�۸�:");
				double price=input.nextDouble();
				System.out.println("-----����ʳƷ����:");
				String name=input.next();
	
				af.addFood(id, name, price);
			}
			else if(a==2) {
				System.out.println("-----����ʳƷ���:");
				int id=input.nextInt();
				af.foodMessage(id);
			}
			else if(a==3) {
				System.out.println("-----����ʳƷ���:");
				int id=input.nextInt();
				System.out.println("-----����ʳƷ�۸�:");
				double price=input.nextDouble();
				af.changePrice(id, price);
			}
			else if(a==4) {
				System.out.println("-----����ʳƷ���:");
				int id=input.nextInt();
				af.delFood(id);
			}
			else if(a==0) {
				break;
			}
			else {
				System.out.println("����������������");
				
			}
		}
	}
}
