fn valid_l(l:i64, n:i64) -> bool { l >= 0 && l < n }
fn valid_m(m:i64, l:i64) -> bool { m >= -l && m <= l }

fn main() {
   let nmax = 20;
   for n2 in 1..=nmax {
      for n1 in 1..n2 {
         let mut num = 0;
         for l2 in 0..n2 {
            for m2 in -l2..=l2 {
               // the l1 = l2-1 transition
               if valid_l(l2-1,n1) {
                  let l1 = l2-1;
                  if valid_m(m2-1,l1) { num+=1; }
                  if valid_m(m2,l1) { num+=1; }
                  if valid_m(m2+1,l1) { num+=1; }
               }
               // the l1 = l2+1 transition
               if valid_l(l2+1,n1) {
                  let l1 = l2+1;
                  if valid_m(m2-1,l1) { num+=1; }
                  if valid_m(m2,l1) { num+=1; }
                  if valid_m(m2+1,l1) { num+=1; }
               }
            }
         }
         let term1 = 1.0/(n1 as f64)/(n1 as f64);
         let term2 = 1.0/(n2 as f64)/(n2 as f64);
         let de = 13.6*(term1 - term2);
         let lambda = 1240.0/de;
         println!("{:2} -> {:2}{:1} {:10}{:20.10e}{:20.10e}", n2, n1,
                  if lambda >= 380.0 && lambda <= 750.0 
                  { 'v' } else {' '}, num, de, lambda);
      }
   }
}

