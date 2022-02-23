using Printf

function valid_l(l,n)
   l >= 0 && l < n
end

function valid_m(m,l)
   m >= -l && m <= l
end

let
   Nmax = 20
   for n2 in 1:Nmax
      for n1 in 1:n2-1
         num = 0
         for l2 in 0:n2
            for m2 in -l2:l2
               # the l1 = l2-1 transition
               if valid_l(l2-1,n1)
                  l1 = l2-1
                  if valid_m(m2-1,l1)
                     num+=1
                  end
                  if valid_m(m2,l1)
                     num+=1
                  end
                  if valid_m(m2+1,l1)
                     num+=1
                  end
               end
               # the l1 = l2+1 transition
               if valid_l(l2+1,n1)
                  l1 = l2+1
                  if valid_m(m2-1,l1)
                     num+=1
                  end
                  if valid_m(m2,l1)
                     num+=1
                  end
                  if valid_m(m2+1,l1)
                     num+=1
                  end
               end
            end
         end
         dE = 13.6*(1.0/n1/n1 - 1.0/n2/n2)
         lam = 1240.0/dE
         if lam >= 380.0 && lam <= 750.0
            vflag="v"
         else
            vflag=" "
         end
         @printf("%2u -> %2u%1c  %8u %18.12g %18.12g\n",n2,n1,vflag,num,dE,lam)
      end
   end
end

