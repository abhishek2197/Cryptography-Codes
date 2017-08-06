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
	ll n;
	getline(cin,s);
	cin>>n;
	map<ll,ll>m_p;
	vector<ll>v(n);
	for(ll i=0;i<n;i++){
	    cin>>v[i];
	    m_p[v[i]-1]=i;
	}
	s.erase(std::remove(s.begin(), s.end(), ' '), s.end());
	vector< vector<char> >v1(n);
	ll k=0;
	while(k<=s.size()){
      for(ll i=0;i<n;i++){
        if(k>s.size())
        break;
        v1[i].pb(s[k++]);
      }
	}    

    ll maxi=0;
    for(ll i=0;i<n;i++){
        maxi=max(maxi,(ll)v1[i].size());
       
    }
    
    for(ll i=0;i<n;i++){
        for(ll j=0;j<v1[i].size();j++){
           if(v1[i][j]=='\0'){
               v1[i][j]='z';
           }
        }
    }

    
    vector<vector<char> >v2(n);
    for(ll i=0;i<n;i++){
        ll cmn=v[i]-1;
        for(ll j=0;j<v1[cmn].size();j++){
            v2[i].pb(v1[cmn][j]);
        }
    }
    cout<<"Encrypted string is "; 
    for(ll i=0;i<n;i++){
        for(ll j=0;j<v2[i].size();j++){
            cout<<v2[i][j];
        }
  
    }
    cout<<endl;
    vector<vector<char> >v3(n);
    for(ll i=0;i<n;i++){
        ll x=m_p[i];
        for(ll j=0;j<v2[x].size();j++){
            v3[i].pb(v2[x][j]);
        }
    }
    for(ll i=0;i<n;i++){
        for(ll j=0;j<v3[i].size();j++){
            cout<<v3[i][j]<<" ";
        }
      cout<<endl;
    }
    cout<<"Decrypted string is "; 
    for(ll i=0;i<v3[0].size();i++){
        for(ll j=0;j<n;j++){
            cout<<v3[j][i];
        }
      
    }
	return 0;
}
