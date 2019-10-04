import java.util.*;
public class FoodStockManage {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		AddFood af=new AddFood();
		while(true) {
			System.out.println("-----按提示选择一下功能-----");
			System.out.println("-----添加食品请按1");
			System.out.println("----查询食品信息按2");
			System.out.println("----修改食品价格按3");
			System.out.println("-------删除食品按4");
			System.out.println("----------退出按0\n\n");
			System.out.println(">>>>>>>请选择<<<<<<<");
			
			int a=input.nextInt();
			if(a==1) {
				// 添加食品
				System.out.println("-----输入食品编号:");
				int id=input.nextInt();
				System.out.println("-----输入食品价格:");
				double price=input.nextDouble();
				System.out.println("-----输入食品名称:");
				String name=input.next();
	
				af.addFood(id, name, price);
			}
			else if(a==2) {
				System.out.println("-----输入食品编号:");
				int id=input.nextInt();
				af.foodMessage(id);
			}
			else if(a==3) {
				System.out.println("-----输入食品编号:");
				int id=input.nextInt();
				System.out.println("-----输入食品价格:");
				double price=input.nextDouble();
				af.changePrice(id, price);
			}
			else if(a==4) {
				System.out.println("-----输入食品编号:");
				int id=input.nextInt();
				af.delFood(id);
			}
			else if(a==0) {
				break;
			}
			else {
				System.out.println("输入有误重新输入");
				
			}
		}
	}
}
