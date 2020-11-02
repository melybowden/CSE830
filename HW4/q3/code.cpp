#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
#include <ctime>
// std::clock_t start_time = std::clock();
// the_function_you_want_to_time();
// std::clock_t tot_time = std::clock() - start_time;
// std::cout << "Time: "
//           << ((double) tot_time) / (double) CLOCKS_PER_SEC
//           << " seconds" << std::endl;  

void print_times(const std::vector<double> &times)
{
    for (size_t i = 0; i < times.size(); i++)
    {
        std::cout << times[i] << " ";
    }
}

int main()
{
    
    std::vector<double> times;
    std::vector<double> dtimes;
    //int N = 1000000;
    int N = 10000000;
    int N2 = 1000000;
    std::multimap<int, int> mmap; // Balance binary tree
    // Could try using different input types
    for (int i = 0; i < N; i += N2)
    {
        std::clock_t t1 = std::clock();
        for (int j = 0; j < i; j++)
        {
            mmap.insert({(i+j)*j,i*(i+1)});
        }
        times.push_back(((double) (std::clock() - t1)) / (double) CLOCKS_PER_SEC);
        
        t1 = std::clock();
        // for (int j = 0; j < i; j++)
        // {
        //     mmap.erase((i+j)*j);
        // }
        mmap.clear();
        dtimes.push_back(((double) (std::clock() - t1)) / (double) CLOCKS_PER_SEC);
        
    }
    

    std::unordered_multimap<int, int> map; //Hash table
    for (int i = 0; i < N; i += N2)
    {
        std::clock_t t1 = std::clock();
        for (int j = 0; j < i; j++)
        {
            map.insert({(i+j)*j,i*(i+1)});
        }
        times.push_back(((double) (std::clock() - t1)) / (double) CLOCKS_PER_SEC);
        // t1 = std::clock();
        // for (int j = 0; j < i; j++)
        // {
        //     map.erase((i+j)*j);
        // }
        // dtimes.push_back(((double) (std::clock() - t1)) / (double) CLOCKS_PER_SEC);
        t1 = std::clock();
        map.clear();
        dtimes.push_back(((double) (std::clock() - t1)) / (double) CLOCKS_PER_SEC);
    }
    
    print_times(times);
    std::cout << std::endl;
    print_times(dtimes);
    std::cout << std::endl;

    return 0;
}