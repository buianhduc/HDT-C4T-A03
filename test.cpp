#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

int flowersCost(std::vector<int> flowers, int l, int c)
{
    int NumberOfFlower=0;
    for(int i=0; i<=flowers.size(); i++){
        NumberOfFlower+=flowers[i];
    }
    int result;
    if(NumberOfFlower%2==0){
        result = NumberOfFlower*c;
    }
    else {
        result = NumberOfFlower*l;
    } 
    return NumberOfFlower;
}

int main(){
    vector<int> flowers;
    int l,c;
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        int temp;
        cin>>temp;
        flowers.push_back(temp);
    }
    cin>>l>>c;
    cout<<flowersCost(flowers,l,c);

}