#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    vector<int> a = {4,5,1,8,9,10,5,6,4,3};
    for(int i=0; i<3; i++){
        cout<<a[i]<<' ';
    }
    cout<<endl;
    for(int i=0; i<3; i++){
        cout<<a[a.size()-1]<<' ';
    }
    cout<<endl;

    sort(a.begin(),a.end());
    for(int i=0; i<a.size(); i++){
        cout<<a[i]<<' ';
    }
    for(int i=a.size()-1; i>-1; i--){
        cout<<a[i]<<' ';
    }
}