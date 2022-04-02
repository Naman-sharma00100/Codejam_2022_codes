#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,total=0;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        // cout<<endl;
        sort(arr,arr+n);
        // for(int i=0;i<n;i++)
        // {
        //     cout<<arr[i];
        // }
        // cout<<endl;
        // if( n=> (arr[n-1]) )
        // {
        int a=1,i=0,g=1;
        // }
        // for(int i=0;i<n;i++)
        while(a<=n)
        {
            // cout<<"run--"<<" "<<a<<" "<<i<<endl;
            if( arr[i] >= a ){
                a++;
                i++;
                total++;
                // cout<<"--iteration--"<<" "<<total;
            }
            else
            {
                a++;
                i++;
                // cout<<total<<endl;
                // goto str;
            }
        }
        cout<<"Case #"<<g<<": ";
        cout<<total<<endl;
        g++;
        // str: {};
    }
    return 0;
}