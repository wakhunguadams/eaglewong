#include<iostream>
using namespace std;
void printarray (int arg[], int
length) { for (int n=0; n<length; n++)
cout << arg[n] << " ";
cout << "\n";
}
int main ()
{
int firstarray[] = {5, 10, 15};
printarray(firstarray,3);
return 0;
}
