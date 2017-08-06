#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>


#define MOD 1000000007
#define ll long long
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pll pair<long long,long long>
#define PI 3.14159

using namespace std;

int main() {
	// your code goes here
	string s;
	ll x;
	cin>>s;
	cin>>x;
	string encrypt="";
	string decrypt="";
	for(ll i=0;i<s.size();i++){

	    int val=(((s[i]-65)+x)%26)+65;
	    char c=(char)val;
	    encrypt+=c;
	}
	cout<<"Encrypted String is "<<encrypt<<endl;
	for(ll i=0;i<encrypt.size();i++){
         decrypt+=(char)(((encrypt[i] -x-65+26)%26)+65);
	}
	cout<<"Decrypted String is "<<decrypt<<endl;
	return 0;
}
