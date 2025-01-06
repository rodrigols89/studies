#include <iostream>
#include <list>

void showlist(std::list<int> mylist)
{
    std::cout << "List values:";
    std::list<int>::iterator it;
    for (it = mylist.begin(); it != mylist.end(); ++it)
        std::cout << ' ' << *it;
    std::cout << '\n';
}

int main()
{
    std::list<int> mylist;

    std::cout << "---- ( push_front() examples ) -----\n";
    mylist.push_front(5); // [5]
    mylist.push_front(3); // [3]->5
    mylist.push_front(1); // [1]->3->5
    showlist(mylist);

    mylist.push_back(10); // 1->3->5->[10]
    mylist.push_back(15); // 1->3->5->10->[15]
    mylist.push_back(20); // 1->3->5->10->15->[20]
    showlist(mylist);

    std::cout << "---- ( Useful Functions examples ) -----\n";
    std::cout << "List is empty(1) or not(0): " << mylist.empty() << "\n";
    std::cout << "List size(): " << mylist.size() << "\n";
    std::cout << "front(): " << mylist.front() << "\n";
    std::cout << "back(): " << mylist.back() << "\n";
    mylist.reverse();
    std::cout << "reverse() ";
    showlist(mylist);

    std::cout << "---- ( merge() + sort() examples ) -----\n";
    std::list<int> mylist_one = {5, 1, 0, 50, 2, 10};
    std::list<int> mylist_two = {3, 7, 8, 20, 4, 15};
    std::cout << "List 1 = ";
    showlist(mylist_one);
    std::cout << "List 2 = ";
    showlist(mylist_two);
    mylist_one.merge(mylist_two);
    std::cout << "List 1 merged with List 2 = ";
    showlist(mylist_one);
    std::cout << "List 1 before apply sort() function = ";
    showlist(mylist_one);
    mylist_one.sort();
    std::cout << "List 1 after apply sort() function = ";
    showlist(mylist_one);

    return 0;
}
