#include <iostream>
using std::cout;
using std::endl;

#include <iomanip>
using std::setw;

bool valid_l(int l, int n) { return l >= 0 and l < n; }
bool valid_m(int m, int l) { return m >= -l and m <= l; }

int main()
{
   const int Nmax = 20;
   for (int n2 = 1; n2 <= Nmax; ++n2)
      for (int n1 = 1; n1 < n2; ++n1)
      {
         int num = 0;
         for (int l2 = 0; l2 < n2; ++l2)
            for (int m2 = -l2; m2 <= l2; ++m2)
            {
               // the l1 = l2-1 transition
               if (valid_l(l2-1,n1))
               {
                  const int l1 = l2-1;
                  if (valid_m(m2-1,l1)) ++num;
                  if (valid_m(m2,l1)) ++num;
                  if (valid_m(m2+1,l1)) ++num;
               }
               // the l1 = l2+1 transition
               if (valid_l(l2+1,n1))
               {
                  const int l1 = l2+1;
                  if (valid_m(m2-1,l1)) ++num;
                  if (valid_m(m2,l1)) ++num;
                  if (valid_m(m2+1,l1)) ++num;
               }
            }
         const double dE = 13.6*(1.0/n1/n1 - 1.0/n2/n2);
         const double lambda = 1240.0/dE;
         cout << setw(2) << n2 << "->" << n1 << (lambda >= 380.0 and lambda <= 750.0 ? 'v' : ' ')
         << setw(10) << num << setw(16) << dE << setw(16) << lambda << endl;
      }
   return 0;
}

