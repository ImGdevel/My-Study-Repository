#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

const char* get_score(int N, int index){
     
    int rank = index / (N / 10);

    switch (rank)
    {
    case 9:
        return "A+";
    case 8:
        return "A0";
    case 7:
        return "A-";
    case 6:
        return "B+";
    case 5:
        return "B0";
    case 4:
        return "B-";
    case 3:
        return "C+";
    case 2:
        return "C0";
    case 1:
        return "C-";
    case 0:
        return "D0";
    default:
        break;
    }
}



int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);  cout.tie(NULL);

    int test_case;
	int T;

	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N, K, target;
        cin >> N >> K;

        int cutline = N/10;
        vector<int> vec (N);

        for(int i=0; i<N;i++){
            int m,l,a, score = 0;
            cin >> m >> l >> a;

            score = m*35 + l*45 + a*20;
            if( (K - 1) == i){
                target = score;
                //cout << "target" << target << " || ";
            }

            vec[i] = score;
        }


        sort(vec.begin(), vec.end());

        int index = 0;

        for(int i=0; i<N; i++){
           // cout << ">>" << vec[i] << "T:" << target;
            if(vec[i] == target){
                index = i;
                break;
            }
        }

        cout << "#" << test_case << " " << get_score(N, index) << "\n";
	}
	return 0;
}