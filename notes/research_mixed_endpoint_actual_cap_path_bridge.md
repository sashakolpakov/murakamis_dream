# Complete endpoint packet on the continued real incoming cap path

Research deduction, 7 November 2026. The complete original endpoint
coefficient has its nonzero asymptotic on a fixed neighborhood of the
actual cap critical path for real incoming parameter \(1/2\le a\le7/10\).
This supplies the missing bridge below private real part \(27/100\).
The path enclosure and the new real-cut comparisons are analytic; no
root evaluation, certificate replay or numerical test is used.

This is an endpoint-coefficient theorem. It does not pay all currents
of the outer cap integral or assert a complete outer-cap packet along
the incoming arc. Earlier frozen notes are unchanged.

## 1. Original source and selected path

Keep exactly
\[
 \begin{split}
 C_N(e,w)&=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\qquad
 S_l=\prod_{j=1}^l2\sin(\pi j/N),\\
 F(e,z)&=-2J(1/2-z)-3J(z)-J(e-z)+i\pi ez,\qquad
 S(e)=F(e,u_c(e)).
 \end{split}                                                     \tag{1}
\]
The Newton polynomials, canonical factorial, reciprocal zeros,
ordinary color, primitive constants and logarithmic lifts are the
original ones. No off-grid row in (1) is deleted.

Let \(e=e(a)\) be the original selected cap critical point from
[general incoming transport](research_mixed_half_face_general_incoming_transport.md),
at complete ordinary color \(-2\). Put
\[
 \begin{gathered}
 X=e^{-2\pi ia},\quad p=e^{2\pi ie},\quad
 \omega=e^{2\pi iu_c(e)},\quad k=\frac{1-\omega}{1+\omega},\\
 k=r-i\tau,\quad \tau>0,\quad U=|k|^2,\quad D=1-2r+U.
 \end{gathered}                                                    \tag{2}
\]
Here \(U\) is a real modulus variable, not the auxiliary coordinate.
The cited theorem proves simple selected branches, original zero
lifts, and
\[
 \Im p>0,\quad\Im\omega>0,\quad
                  0<\Re u_c<\Re e<1-a\le1/2.                  \tag{3}
\]
The exact relations are
\[
 p=1-2k+2k^2,\qquad
 X=4k^2+3-\frac2{1-k}=1-\frac{2kp}{1-k}.                       \tag{4}
\]
All divisors are nonzero on the selected path.

[Global phase decrease](research_mixed_half_face_global_phase_decrease.md)
already establishes \(r<1/5\), and \(|p|^2>2U\) when \(r>0\).
Its unit-locus calculation gives
\[
 \begin{split}
 \mathfrak f(r,U)
   &:=4U^3-(8r+2)U^2+12r^2U-8r^3+4r^2-r=0,\\
 |p|^2&=1-4r+8r^2-8rU+4U^2,\\
 \Re X&=8r^2-4U+3-\frac{2(1-r)}{1-2r+U},\\
 \Re p&=1-2r+4r^2-2U,\qquad
 \Im p=2\tau(1-2r).
 \end{split}                                                     \tag{5}
\]
Throughout the incoming arc,
\[
             \Re X\le\frac{1-\sqrt5}{4}<-\frac3{10}.           \tag{6}
\]
At the initial half face the proved algebraic enclosure gives
\[
 0<r<1/5,\qquad U>17/23>1/2,\qquad
                         1<|p|^2<1444/777<21/10.             \tag{7}
\]
For \(U\), use \(U=(1-2\sigma+s)/(1+2\sigma+s)\),
\(\sigma<1/8\), \(s>2/3\), from Section 2 of
[the complete half-cap theorem](research_mixed_half_face_complete_cap_packet.md).

## 2. Global enclosure of the actual private path

**Lemma 1.** On the selected path,
\[
 -1/100<r<1/5,\qquad U>2/5,\qquad 1<|p|^2<21/10.              \tag{8}
\]
Consequently
\[
 \boxed{\quad
 6/25<\Re e(a)<9/20,\qquad -3/50<\Im e(a)<0 .
 \quad}                                                        \tag{9}
\]

*Proof.* At \(U=2/5\),
\[
 \mathfrak f(r,2/5)
 =-8/125-(57/25)r+(44/5)r^2-8r^3.                             \tag{10}
\]
This is strictly convex on \([-1/100,1/5]\); its endpoint values
are \(-5039/125000\) and \(-29/125\), hence it is negative
throughout. Before a first crossing of \(r=-1/100\), the initial
branch cannot cross \(U=2/5\). At that hypothetical crossing,
\[
 \mathfrak f(-1/100,U)
  =4U^3-(48/25)U^2+(3/2500)U+1301/125000.                     \tag{11}
\]
It increases strictly for \(U\ge2/5\), and its value at \(47/100\)
is \(267/125000>0\). Thus \(U<47/100\).
At fixed \(r=-1/100\), the expression for \(\Re X\) decreases
for \(U\ge2/5\), so
\[
       \Re X+3/10>888/625-202/149>0.                           \tag{12}
\]
The last cross-product difference is \(6062\). This contradicts
(6), proving \(r>-1/100\); (10) then gives \(U>2/5\) globally.

For \(-1/100<r\le0\), \(\mathfrak f(r,U)\) increases on
\(U\ge2/5\), and
\[
                  \mathfrak f(r,1/2)=r(-3+10r-8r^2).          \tag{13}
\]
Therefore \(U<1/2\) when \(r<0\), and \(U=1/2\) at \(r=0\).
For \(0<r<1/5\), the polynomial is strictly convex for
\(U\ge2/5\), negative at \(2/5\) and \(1/2\), and has exactly
one zero above \(2/5\). Thus \(U>1/2\) there.
When \(r\le0\), one also has \(U>12/25\). Indeed \(\Re X\)
decreases with \(U\), whereas at \(U=12/25\), writing \(r=-s\),
\[
 \Re X=8s^2+\frac{27}{25}-\frac{2(1+s)}{37/25+2s}
 \ge\frac{27}{25}-\frac{50}{37}
 =-\frac{251}{925}>-\frac3{10}.                              \tag{14}
\]
The quotient decreases for \(0\le s\le1/100\), so (6) proves
the claim.

For \(r<0\), (5) and \(U<1/2\) give
\[
 |p|^2<1+1/25+1/1250+1/25+1
                 =2601/1250<21/10.                          \tag{15}
\]
For \(r\ge0\), put \(d=1-2r\), \(w_0=U-r>0\). Then
\[
 \begin{split}
 4w_0^3-2dw_0^2-2d(1-d)w_0-d(1-d)/2&=0,\\
                       |p|^2&=d^2+4w_0^2,\qquad 3/5<d\le1.
 \end{split}                                                   \tag{16}
\]
At a hypothetical \(|p|^2=q=21/10\), these imply
\[
 \sqrt{q-d^2}\,(q+d^2-2d)=d(q+1-d-d^2).                       \tag{17}
\]
Squaring and setting \(z=1-d=2r\in[0,2/5)\) yields
\[
 0=(80z-11)^2+
 z^3(17400-20900z+10000z^2-2000z^3).                          \tag{18}
\]
The parenthesis is at least \(8912>0\); at \(z=0\) the
square is positive. Thus the initial bound (7) cannot be crossed.
The lower bound \(|p|^2>1\) follows from the already proved
\(|p|^2>2U\) for \(r>0\), directly from (5) for \(r<0\),
and from \(|p|^2=2\) at \(r=0\).
The depth in (9) follows from
\[
 e^{6\pi/25}>e^{3/4}>
 1+3/4+(3/4)^2/2+(3/4)^3/6=269/128>21/10,                    \tag{19}
\]
using \(\pi>25/8\).

If \(r\ge0\), then \(\Re p\le0\), so \(\Re e\ge1/4\).
If \(r<0\), (14) gives
\[
          \Re p<151/2500,\qquad \Im p>69/50.                 \tag{20}
\]
Here \(\tau^2>12/25-1/10000>(69/100)^2\).
When \(\Re p>0\), its ratio to \(\Im p\) is less than
\(151/3450<3/50<\tan(\pi/50)\); hence
\(\arg p>\pi/2-\pi/50\), giving \(\Re e>6/25\).
The other case is stronger. Finally \(\tau>3/5\),
\(1-2r>3/5\), and \(|p|<3/2\) imply
\(\sin(\arg p)>12/25\). This rules out \(\Re e\ge9/20\),
since then \(\sin(\arg p)\le\sin(\pi/10)<1/3\).
\(\square\)

## 3. Auxiliary enclosure on the missing subpath

Only \(E:=\Re e\le27/100\) requires a new endpoint proof.
Write \(e=E-i\eta\), \(u_c=\xi+ih_c\).

**Lemma 2.** On this subpath,
\[
 \begin{gathered}
 -1/100<r<7/200,\qquad 12/25<U<591/1000,\\
 1/20<\eta<3/50,\qquad
 1/6<\xi<21/100,\qquad -1/400<h_c<1/120,
 \end{gathered}                                                  \tag{21}
\]
and
\[
 E-\xi>1/25\ (h_c\ge0),\qquad E-\xi>1/30\ (h_c<0).            \tag{22}
\]

*Proof.* For \(r>0\), (16) gives
\[
              4w_0^2(2w_0-d)=d(1-d)(4w_0+1).                 \tag{23}
\]
As \(w_0^2<87/200<4/9\), the decreasing function
\((4w_0+1)/(8w_0^2)\) exceeds \(33/32>1\). Therefore
\[
         w_0>d/2+d(1-d),\qquad
         \Re p=d^2-2w_0<-3d(1-d).                            \tag{24}
\]
If \(r\ge7/200\), then \(3/5<d\le93/100\), so
\(\Re p<-1953/10000\), and
\[
 \cos(\arg p)<-651/5000<-22/175<-\sin(\pi/25).                \tag{25}
\]
This would give \(E>27/100\), a contradiction.
Thus \(d>93/100\), and
\[
 w_0^2<12351/40000<(139/250)^2,\qquad
 U<139/250+7/200=591/1000.                                   \tag{26}
\]
The lower bound follows from (13)--(14).

The exact formula
\[
                 \omega=\frac{1-U+2i\tau}{1+2r+U}            \tag{27}
\]
has positive real part, and
\[
       69/26<\frac{2\tau}{1-U}<1540/409<19/5.                 \tag{28}
\]
Use \(\tau>69/100\), \(\tau<77/100\) and (26).
The lower bound exceeds \(\sqrt3\). Also
\[
        \cot(2\pi/25)>175/44-22/175>19/5,                    \tag{29}
\]
using \(\cos x\ge1-x^2/2\), \(\sin x\le x\) and
\(2\pi/25<44/175\).
Thus \(1/6<\xi<21/100\).
Moreover
\[
          h_c=\frac1{4\pi}
                \log\frac{1+2r+U}{1-2r+U}.                  \tag{30}
\]
For \(r\ge0\), \(U\ge1/2\) gives
\[
          0\le h_c<7/(286\pi)<1/120.                         \tag{31}
\]
For \(r<0\), \(U>12/25\) gives instead
\[
                         |h_c|<1/(146\pi)<1/400.             \tag{32}
\]
These follow from \(\log(1+x)<x\).

If \(r<0\), (5) gives \(|p|^2>1+4(12/25)^2>19/10\).
If \(r>0\), (24) gives
\[
 |p|^2>d^2\{1+4(3/2-d)^2\}
       \ge198892404/100000000>19/10.                          \tag{33}
\]
The expression on the left of the second inequality increases
on \(93/100\le d<1\), with derivative
\(4d(1-d)(5-4d)>0\); the rational value is its value at
\(93/100\). At \(r=0\), \(|p|^2=2\).
Finally
\[
 \log(19/10)=2\operatorname{artanh}(9/29)>
 18/29+\tfrac23(9/29)^3
       =15624/24389>22/35>\pi/5,                             \tag{34}
\]
proving \(\eta>1/20\).

For (22), put \(d_*=E-\xi>0\).
When \(h_c\ge0\), the original zero lift \(F_z(e,u_c)=0\)
gives the exact imaginary equation
\[
 \begin{split}
 \arctan\{\cot(\pi d_*)\tanh\pi(\eta+h_c)\}
   ={}&\pi E-2\arctan\{\tan(\pi\xi)\tanh(\pi h_c)\}\\
      &-3\arctan\{\cot(\pi\xi)\tanh(\pi h_c)\}
   \le\pi E .
 \end{split}                                                   \tag{35}
\]
All primitive arguments have their original signs.
The elementary inequalities
\[
 \tan(27\pi/100)<6/5,\quad \tanh(\pi/20)>31/200,\quad
               \tan(\pi/25)<9/70<31/240                      \tag{36}
\]
imply \(\tan(\pi d_*)>31/240\), hence \(d_*>1/25\).
Here are explicit witnesses: \(27\pi/100<17/20\),
\(\sin x\le x-3x^3/20\) for \(0\le x\le1\) gives
\(\sin(17/20)<19/25\), and
\(\cos(17/20)\ge511/800>19/30\).
Use \(\tanh x\ge x-x^3/3\) at \(x=157/1000<\pi/20\)
for the second inequality, and
\[
 \tan(\pi/25)<
 (22/175)/(1-(22/175)^2/2)=3850/30383<9/70
\]
for the third.

When \(h_c<0\), (13) gives \(U<1/2\); then \(\Re p>0\),
so \(E<1/4\). The same imaginary equation has right side
less than
\[
 \pi/4+\pi|h_c|\{2\tan(\pi\xi)+3\cot(\pi\xi)\}
 <\pi/4+29\pi/1600=429\pi/1600<17/20.                         \tag{37}
\]
Use \(\xi<1/4\), \(\xi>1/6\), \(\sqrt3<7/4\), and (32).
Now \(\eta+h_c>19/400\) and
\(\tanh(19\pi/400)>7/50\). Taking tangents in (35)
therefore gives \(\tan(\pi d_*)>7/60\).
But \(\tan(\pi/30)<1/9<7/60\), proving \(d_*>1/30\).
The last witnesses follow from \(\tanh x\ge x-x^3/3\)
at \(x=57/400\), and \(\tan x\le x/(1-x^2/2)\)
at \(x=11/105\). \(\square\)

## 4. Both real cuts lie strictly below the own critical action

Keep the exact bridge-tail cuts
\[
                     a_L=1/20,\qquad b(E)=E-1/100.            \tag{38}
\]
Lemma 2 places the critical point strictly between them.
Along either straight segment from \(u_c\) to its real cut,
\[
 -F_{zz}(e,z)/\pi
       =2\tan\pi z+3\cot\pi z+\cot\pi(e-z).                   \tag{39}
\]
Every term has positive real part. Write the first two
terms as \(A_0+iB_0\). For \(z=x+ih\),
\[
 \begin{split}
 \frac{|\Im\tan\pi z|}{\Re\tan\pi z}
  =\frac{|\Im\cot\pi z|}{\Re\cot\pi z}
  &=\frac{\sinh(2\pi|h|)}{\sin(2\pi x)},\\
 \Re\tan\pi z\,\Re\cot\pi z
  &=\frac1{1+\{\sinh(2\pi h)/\sin(2\pi x)\}^2}.
 \end{split}                                                   \tag{40}
\]
All segment heights have \(|h|<1/120\), and
\(\sinh(\pi/60)<1/18\). For this last inequality use
\(\pi/60<1/19\), \(\sinh t\le t/(1-t^2/6)\).

On the left segment \(1/20\le x\le21/100\), so
\(\sin(2\pi x)>3/10\). Weighted arithmetic-geometric mean
in (40) gives
\[
                         A_0>4,\qquad |B_0|<A_0/5.           \tag{41}
\]
On the right segment \(1/6\le x\le26/100\), so
\(\sin(2\pi x)\ge\sqrt3/2>6/7\). Thus
\[
                         A_0>24/5,\qquad |B_0|<A_0/15.       \tag{42}
\]
The squared lower bounds for \(A_0\) are respectively
\(24/(1+1/25)>16\) and \(24/(1+1/225)>576/25\).

Throughout both segments, \(0<\Re(e-z)<1/2\) and
\(-\Im(e-z)>19/400\). The third term has positive real part and
\[
       0<\Im\cot\pi(e-z)\le\coth(19\pi/400)<7.                \tag{43}
\]
Use \(\pi>25/8\) and
\(19/128-(19/128)^3/3>1/7\) for the last inequality.
Writing \(F_{zz}=-A+iB\), \(A>0\), (41)--(43) imply
\[
 |B|<2A\quad\hbox{on the left segment},\qquad
 |B|<(8/5)A\quad\hbox{on the right segment}.                  \tag{44}
\]
Indeed the two ratios are at most
\(1/5+7/4=39/20<2\) and \(1/15+35/24=61/40<8/5\).

The left displacement from the critical point has
\[
             |\Delta\Im z|/|\Delta\Re z|<1/14.                \tag{45}
\]
For the right cut, (22) gives the common upper bound
\[
             |\Delta\Im z|/|\Delta\Re z|<5/18.                \tag{46}
\]
When \(h_c\ge0\), use \(h_c<1/120\) and
\(b(E)-\xi>3/100\). When \(h_c<0\), the stronger ratio
\((1/400)/(7/300)=3/28\) follows.

Because the original \(F_z(e,u_c)=0\), the exact second-order
integral along either segment gives
\[
 \Re\{F(e,c)-S(e)\}
 \le-\int_0^1(1-s)A(s)\,ds\,
       \{\Delta x^2-\Delta h^2-2M|\Delta x\Delta h|\}<0,       \tag{47}
\]
where \(M=2\) or \(8/5\). The bracket divided by \(\Delta x^2\)
is at least, respectively,
\[
       1-1/196-4/14=139/196>0,\qquad
       1-25/324-8/9=11/324>0.                               \tag{48}
\]
Both real cuts therefore have strict own-action gaps on this
entire compact subpath. Their minimum is positive; it is not
numerically evaluated.

## 5. Complete finite-source conclusion

**Theorem.** There is a fixed open complex neighborhood of
\[
              \mathcal K=\{(e(a),-2):1/2\le a\le7/10\}        \tag{49}
\]
on which the entire original function (1) satisfies
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                  (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0.  \tag{50}
\]
The phase, symbol and accretive square-root branch are the
original ones. Both level parities and all fixed mixed
ordinary-color/index derivatives are included on smaller
neighborhoods.

*Proof.* Lemma 1 puts the full path in the domain of
[the bridge real tails](research_mixed_endpoint_bridge_real_tails.md)
and [the bridge phase floor](research_mixed_endpoint_bridge_phase_floor.md).
For \(E\ge27/100\), the packet is already proved by
[the deeper rectangle](research_mixed_endpoint_cap_rectangle_deeper_extension.md).
For \(E\le27/100\), use (38) and (47). The tail theorem reduces
every row below the left cut and from the right cut through
one half to those same cut values. Every row above one half
has rate less than \(67/105\), whereas the original action
exceeds \(1511/2000\), leaving a gap greater than \(1/10\).
Thus every omitted physical and revived row is paid, including
true endpoints, both parities and all reciprocal zeros.

The retained contour uses the signed-height construction of
Section 4 of the deeper-rectangle proof. Its hypotheses are
now established independently by (3), (39) and (47).
Horizontal strict concavity through \(u_c\) gives its unique
nondegenerate maximum \(\Re S\). For symmetric heights
\(\pm H\), the original exact reflection gives
\[
 \begin{split}
 \Re F(e,x-iH)-\Re F(e,x+iH)
   &=2\pi EH+\int_{-H}^H\Im J'(e-x+it)\,dt,\\
 \left|\int_{-H}^H\Im J'(e-x+it)\,dt\right|&\le\pi H .
 \end{split}                                                   \tag{51}
\]
When \(h_c=H>0\), the opposite lower alias loses at least
\(\pi(1-2E)H\); when \(h_c=-H<0\), the opposite upper alias
loses at least \(\pi(1+2E)H\). The alias on the main side
loses \(2\pi H\). Weighted vertical profiles are convex on
each height-sign half, so their paid real and horizontal
endpoints pay the entire sides. The unweighted joins are
also convex between the paid real cut and the paid endpoint
on the main line.

If \(h_c=0\), the original identity
\[
       \Im F_z(e,x)=\Arg\sin\pi(e-x)+\pi E\in(-\pi/2,\pi/2)    \tag{52}
\]
on the retained real segment permits a fixed small finite
rectangle with outer heights \(\pm\epsilon\),
\(|\Im F_z|<\pi\), and both cut gaps retained.
Each horizontal alias then loses at least \(\pi\epsilon\).
When \(h_c\ne0\), slightly enlarge the outer heights beyond
\(\pm|h_c|\) after allocating part of their strict gaps.
These constructions persist on fixed base neighborhoods.
A finite cover includes every change of sign of \(h_c\).

At a fixed base point use exactly
\[
 \begin{gathered}
 L_N=\lceil N/20\rceil,\quad M_N=\lceil N(E-1/100)\rceil,\\
 a_N=(L_N-1/2)/N,\qquad b_N=(M_N-1/2)/N.
 \end{gathered}                                                  \tag{53}
\]
The retained rows are \(L_N\le l<M_N\). The original finite
cotangent identity has constant-mode coefficient \(+N\),
both horizontal aliases, four sign-half vertical aliases
and two unweighted joining currents. Every reciprocal
factorial argument is regular on the retained rectangles;
other rows remain the literal finite source already bounded.
The half-grid shifts preserve the strict gaps by the original
zero-safe uniform factorial estimates. No current is discarded.

The exact regular row symbol has its original nonzero power
\(N^{-2}\). The Gaussian normalization is consequently
\(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\), with the original
accretive branch of \(\sqrt{-F_{zz}}\). The first odd Gaussian
correction vanishes. Every other source group has a common
fixed positive gap. The original Newton bounds preserve those
gaps on a small fixed complex ordinary-color neighborhood.
Keep each base contour and its integer row sets fixed while
parameters vary; no ceiling is differentiated.
On overlaps the exact function, critical branch and symbol
agree with their original continuations. Compactness gives
(50) near (49), and Cauchy's formula gives all fixed mixed
derivatives. \(\square\)

This theorem supplies the complete endpoint factor near every
point of the actual real-incoming cap critical path. A full
outer cap deformation must additionally pay its private
horizontal bridge, outer cuts, aliases and unweighted joins
relative to the outer critical action. Those conclusions do
not follow from (50) and are not asserted here.
