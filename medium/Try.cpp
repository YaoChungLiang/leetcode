#include  <iostream>
using namespace std;

#define NAME_SIZE 50

class Person{
    int id;
    char name[NAME_SIZE];

    public:
        void aboutMe(){
            cout << "I am a person.";
        }
};



int main(){
    Person * Ann = new Person();
    Ann->aboutMe();
    delete Ann;
    return 0;
}