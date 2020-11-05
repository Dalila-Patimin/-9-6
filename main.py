#include <stdio.h>
int MinIn4(int w,int x,int y,int z){
	int min[4] = {w,x,y,z};
	int result = min[0];
	for(int i = 1; i < 4 ; i++){
		if(result > min[i]){
			result = min[i];
		}
	}
	return(result);
}
int main()
{
  int a,b,c,d;
  printf("Enter 1st number : ");
  scanf("%d",&a);
  printf("Enter 2nd number : ");
  scanf("%d",&b);
  printf("Enter 3rd number : ");
  scanf("%d",&c);
  printf("Enter 4th number : ");
  scanf("%d",&d);
  printf("Minimum is %d\n",MinIn4(a,b,c,d));
  return 0;
}
