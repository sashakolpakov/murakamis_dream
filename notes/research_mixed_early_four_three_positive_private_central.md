# The early first four/three central source at positive private height

Private written proof, 10 November 2026. The complete first-four cap
and the central part of its own-three neighbor have a strict joint
bound at the original fixed early heights, including when the
ordinary private critical height is positive. The main estimate uses
the joint cap/ordinary Hessian: discarding the cap's curvature before
estimating the ordinary factor would lose a useful positive term.
The two real cap cuts and the upper cap alias instead have a direct
joint transport inequality. The lower cap alias and the true cap
index ends are retained separately.

The finite conclusion includes the original ordinary left cut at
three twentieths, every central row up to half the level, both
zero-mode joins, all horizontal and vertical aliases, and both
parities. The high ordinary rows and a changing-height outer contour
are not included.

## 1. The original source, reference and allocation

Fix an actual positive three/four open word of length at least three
beginning with types four and three. Write its unchanged reference as
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad
 e_*=e_0+ih_e,\qquad s_*=s_0+ih_0.
\tag{1}
\]
The first private coordinate is \(e_*\), and the second vertex's
ordinary private coordinate is \(s_*\). Assume \(h_0\ge0\).
The endpoint rectangles, actual ordinary images, and the coupled
first-four height theorem give
\[
\begin{gathered}
 .246<a_0<.350,\quad -.070<c<-.020,\quad
 .333<e_0<.363,\quad -.051<h_e<-.019,\\
 .23\le s_0\le.45,\quad 0\le h_0\le17/250,
 \qquad -.065\le d\le.068.
\end{gathered}
\tag{2}
\]
These are necessary bounds on the same original coupled reference.
No arbitrary point of their containing product replaces it.
Keep all these heights fixed and take
\[
 a=x+ic,\quad b=z+id,\qquad
 x\in[1/10,11/50],\quad z\in P=[11/50,9/20].
\tag{3}
\]
With \(r_N=e^{-2\pi i/N}\), retain the literal definitions
\[
\begin{gathered}
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\quad
 P_j=(r_N;r_N)_j,\\
 R_{j,N}=X^{-j}
       \frac{(r_NX;r_N)_j(r_NY;r_N)_j}{P_j^2},\\
 J_L=\lfloor3N/20\rfloor,\quad J_R=\lceil N/2\rceil-1,
 \qquad C^{\rm mid}_{0,N}(X,Y)=\sum_{j=J_L+1}^{J_R}R_{j,N}.
\end{gathered}
\tag{4}
\]
The first factor is the complete cap polynomial \(U_{1,N}(w,X)\).
Its original first retained weight is the full unselected factor
\(d_N(X)\). There is no own-three outgoing halfweight at \(Y\).
No selected first monomial or factor \(1+X^{-N}\) is inserted.

Use the original primitives, complete-end action and logarithmic
lifts of the joint low-/half-row theorem. Thus
\[
 J'(v)=\Log(2\sin\pi v),\quad J(0)=0,\quad
 g(v)=J(v)+\tfrac{\pi i}{2}(v-v^2),
\]
and the allocated phases are exactly
\[
\begin{split}
 \Xi_1(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea-g(e)-\tfrac12g(a),\\
 F_{10}(s;a,b)&=g(s+a)+g(s+b)-2g(s)+2\pi ias
                                      -\tfrac32g(a)-g(b).
\end{split}
\tag{5}
\]
Write \(L_1=\operatorname{stat}_e\Xi_1\),
\(\phi_{10}=\operatorname{stat}_sF_{10}\), and
\(\kappa=1/2500000\). Retain the original joint plane
\[
\begin{split}
 \Gamma(z)={}&\Re L_1(a_*)+\Re\phi_{10}(a_*,b_*)
       +\Re\partial_b\phi_{10}(a_*,b_*)(z-b_0)
                                      -\kappa(z-b_0)^2.
\end{split}
\tag{6}
\]
The original critical equations give
\(L_1'(a_*)+\partial_a\phi_{10}(a_*,b_*)=0\).

**Theorem 1.** There is a uniform constant \(\nu>0\), obtained
from the compact strict Hessian estimate below, such that, with
\[
 \gamma_{43}=\min\{\kappa,\nu/4\}(a_0-11/50)^2>0,
\tag{7}
\]
every \(\tau>0\) admits
\[
 |U_{1,N}(w,X)|\,|d_N(X)|\,|C^{\rm mid}_{0,N}(X,Y)|
 \le C_\tau N^{A_\tau}
                 e^{N\{\Gamma(z)-\gamma_{43}+\tau\}}.
\tag{8}
\]
It holds uniformly on (3), for both level parities, on a sufficiently
small fixed ordinary-color neighborhood of \(w=-2\). Every fixed
ordinary-color derivative satisfies the same rate on a smaller
neighborhood. The gap is uniform over the actual reference family,
since \(a_0-.22>13/500\).

## 2. The cap contributes a full outgoing cotangent after elimination

Use the compact products
\[
\begin{gathered}
 .27\le\Re e\le.49,\quad -.051\le\Im e\le-.019,\\
 .1\le\Re a\le.35,\quad -.07\le\Im a\le-.02,\qquad
 .15\le\Re s\le.5,\quad 0\le\Im s\le.068.
\end{gathered}
\tag{9}
\]
The original early-cap curvature theorem gives, throughout its
larger private rectangle,
\[
 -\Re S''(e)/\pi>E+3/4,\qquad E=\Re\cot\pi e>0.
\tag{10}
\]
Set \(A=\Re\cot\pi a>0\), \(C_e=\Re\cot\pi(e+a)\).
The negative real cap Hessian divided by \(\pi\) is
\[
 \begin{pmatrix}K&-C_e\\-C_e&\tfrac32A-C_e\end{pmatrix},
             \qquad K>2E+3/4-C_e.
\tag{11}
\]

**Lemma 2.** Its Schur complement in the outgoing coordinate is
strictly greater than \(A\) on (9).

*Proof.* It is enough to prove
\[
                  K(\tfrac12A-C_e)-C_e^2>0.
\tag{12}
\]
For \(C_e\le0\), this follows directly from
\(K>-C_e\) and \(A>0\). If \(0<C_e\le1/4\), then
\(\Re(e+a)<1/2\), hence \(\Re a<.23\), and \(A>1\).
Therefore the left side of (12) is greater than
\[
 (3/4-C_e)(1/2-C_e)-C_e^2
                       =3/8-5C_e/4\ge1/16.
\tag{13}
\]
If \(C_e>1/4\), then \(\cot(.43\pi)<1/4\) implies
\(\Re(e+a)<.43\), so \(\Re e<.33\), \(\Re a<.16\).
Here \(E>1/2\), \(A>4/3\), and \(C_e<9/20\).
The left side of (12) now exceeds
\[
 (7/4-C_e)(2/3-C_e)-C_e^2
                =7/6-29C_e/12>19/240.
\tag{14}
\]

Here are elementary witnesses for all guards just used. The
positive hyperbolic series gives \(\cosh(.14\pi)<11/10\):
use \(.14\pi<11/25\) in
\(\cosh t\le1+t^2/[2(1-t^2/12)]\), whose added term is
then at most \(726/7379<1/10\).
For \(.1\le x\le.23\),
\(\sin(2\pi x)+\cos(2\pi x)>11/10\), which implies
\(A>1\). The sum is concave on this interval; its first endpoint
is greater than \(7/12+4/5\). At its second endpoint use
\(\cos(.04\pi)>97/98\) and
\(\sin(.04\pi)>3/25-1/2058\); their sum exceeds \(11/10\).
For \(x\le.16\), the real cotangent part decreases in \(x\)
on this range, and
\(\sin(.32\pi)>5/6\), \(\cos(.32\pi)>1/2\) give
\(A>25/18>4/3\). The sine bound follows by evaluating its
increasing Taylor lower polynomial at \(t=1\), since
\(.32\pi>1\); the cosine bound uses \(.32\pi<\pi/3\).
For \(.27\le\Re e<.33\), its sine numerator exceeds
\(\sqrt3/2>4/5\), while its denominator is below
\(16/15+1/2<8/5\), giving \(E>1/2\).
Finally, \(\tan(.07\pi)<1/4\) follows from
\(.07\pi<11/50\) and \(\tan t\le t/(1-t^2/2)\).
The same bound at \(.13\pi<41/100\) gives
\(\cot(.37\pi)<8200/18319<9/20\).
All these domains lie in the original regular sine strips.
\(\square\)

## 3. Joint main concavity on the whole old central interval

Put \(V(s,a)=g(s+a)-g(s)-g(a)\),
\(U=\Re\cot\pi s\), \(C=\Re\cot\pi(s+a)\).
After eliminating the cap private direction, Lemma 2 shows that
the negative real Hessian of
\(\Xi_1+V(s,a)-g(a)/2+2\pi ias\), divided by \(\pi\),
strictly dominates in \((s,a)\) the matrix
\[
                  \begin{pmatrix}U-C&-C\\-C&\tfrac52A-C\end{pmatrix}.
\tag{15}
\]
The chirp has purely imaginary Hessian. If \(C\le0\), (15)
is positive definite; at \(\Re s=1/2\), where \(U=0\),
one has \(C<0\), so this endpoint is also strict.

For \(C>0\), put \(u_0=\cot(\pi\Re s)\),
\(p_0=\cot(\pi\Re a)\). Then
\[
 U>\tfrac45u_0,\qquad A>\tfrac{13}{20}p_0,\qquad
 C\le C_0=\frac{u_0p_0-1}{u_0+p_0},\qquad p_0<10/3.
\tag{16}
\]
For the first two inequalities use
\[
 \frac{\Re\cot\pi(v+iy)}{\cot\pi v}
 =\frac1{1+\sinh^2(\pi y)/\sin^2(\pi v)}.
\]
The written bounds
\(\sinh(.068\pi)<2/9\), \(\sin(.15\pi)>4/9\),
\(\sinh(.07\pi)<2/9\), \(\sin(.1\pi)>4/13\)
give respectively \(4/5\) and \(324/493>13/20\).
For example, \(.07\pi<11/50\) and
\(\sinh t\le t+t^3/[6(1-t^2/20)]\) give the hyperbolic
bound; \(\sin t\ge t-t^3/6\) and \(157/50<\pi<22/7\)
give both sine bounds. Also \(p_0<1/(\pi/10)<10/3\).

The determinant of (15) is positive if
\(1/U+1/((5/2)A)<1/C_0\). Equations (16) reduce this to
\[
 \frac5{4u_0}+\frac8{13p_0}
                   <\frac{u_0+p_0}{u_0p_0-1}.
\tag{17}
\]
After multiplication by positive denominators its difference has
numerator
\[
 p_0\left(\frac5{13}u_0^2-\frac{p_0}4u_0+\frac54\right)
                              +\frac8{13}u_0>0.
\tag{18}
\]
Indeed the bracket exceeds
\((5/13)u_0^2-(5/6)u_0+5/4\), whose discriminant is
\(25/36-25/13<0\). This proves strict positivity on (9).

Compactness now supplies \(\nu>0\) such that
\[
 -\Re\{\Xi_1+V(s,a)-g(a)/2+2\pi ias\}''
                              \succeq\nu I_{e,s,a}.
\tag{19}
\]
The half-index theorem retains the original independent estimate
\(-\Re V(s,b)''\succeq2\kappa I_{s,b}\) on
\([.15,.5]+i[-.108,.068]\) and
\(P+i[-.12,.12]\). Adding it proves
\[
 -\Re(\Xi_1+F_{10})''
                 \succeq\nu I_{e,s,a}+2\kappa I_{s,b}.
\tag{20}
\]
The horizontal segment from the actual reference to every main
target stays in these products. Its two private marginals vanish,
and its first retained marginals cancel. Integrating (20) therefore
gives, for every \(u\in[.27,.49]\), \(v\in[.15,.5]\),
\[
 \Re\{\Xi_1(u+ih_e,a)+F_{10}(v+ih_0;a,b)\}
                       \le\Gamma(z)-2\gamma_{43}.
\tag{21}
\]
Only positive compactness is used to choose \(\nu\); no numerical
value for an eigenvalue or critical point is evaluated.

## 4. The real cap cuts and the upper cap alias

For \(s=v+i\eta\), \(.15\le v\le.5\), \(0\le\eta\le h_0\),
set \(r=e^{2\pi c}\), \(q=e^{-2\pi\eta}\). The actual bounds give
\[
                  3/5<r<9/10,\qquad 13/20<q\le1.
\tag{22}
\]
The first inequality follows from \(.14\pi<1/2<\log(5/3)\);
the upper follows from \(c<-.02\) and
\(e^{\pi/25}>1+3/25>10/9\). The positive atanh series gives
\(\log(20/13)>14/33+686/107811>3/7>17\pi/125\), proving
the bound on \(q\).

For any cap point \(e=u+i\xi\) with \(.27\le u\le.49\)
and \(\xi\ge0\), put \(R=e^{2\pi\xi}\ge1\). Exact
differentiation, including the ordinary chirp, gives
\[
 \partial_x\Re(\Xi_1+F_{10})=
 \log\frac{N_eN_s}{D^3},\qquad
 \begin{cases}
 N_e=|1-rR e^{-2\pi i(u+x)}|,\\
 N_s=|q-r e^{-2\pi i(v+x)}|,\\
 D=|1-r e^{-2\pi ix}|.
 \end{cases}
\tag{23}
\]
The factor \(q\), rather than one, is essential.

**Lemma 3.** The derivative (23) is strictly positive throughout
(3), (22) and the displayed private intervals.

*Proof.* If \(x\le4/25\), the squared moduli satisfy
\[
 N_e^2>1+r^2+r,\qquad N_s^2>169/400+r^2,
                    D^2< B=1+r^2-r<1.
\]
Here \(u+x\in[.37,.65]\), \(v+x\in[.25,.66]\).
The second lower bound exceeds \(B\), since
\(r>3/5>231/400\); the first does also. Hence
\(N_e^2N_s^2>B^2>B^3\).

For \(4/25\le x\le11/50\), use the sharper angular bounds
\[
 \cos2\pi(u+x)<-31/125,\quad
 \cos2\pi(v+x)<-14/75,\quad \cos2\pi x>14/75.
\tag{24}
\]
They follow from \(\sin(.08\pi)>31/125\) and
\(\sin(.06\pi)>14/75\). For written witnesses,
\(.08\pi>157/625\), \(.08\pi<13/50\), and
\(2197<2400\) pay the cubic sine remainder in the first
inequality. For the second use \(.06\pi>471/2500\),
\(.06\pi<19/100\), and \(6859<10400\).
The squared moduli are bounded by
\[
\begin{split}
 N_e^2&>A=1+r^2+62r/125,\\
 N_s^2&>C=r^2+91r/375+169/400,\\
 D^2&<B=1+r^2-28r/75.
\end{split}
\tag{25}
\]
We show \(P(r)=AC-B^3>0\) on \([3/5,9/10]\).
Write \(a=62/125\), \(b=28/75\), \(c_1=91/375\),
\(d_1=169/400\). Multiplication gives
\[
\begin{split}
 P(r)={}&-r^6+3br^5-(2+3b^2)r^4
 +(a+c_1+6b+b^3)r^3\\
 &+(d_1-2+ac_1-3b^2)r^2
 +(c_1+ad_1+3b)r+d_1-1.
\end{split}
\tag{26}
\]
Its second derivative satisfies
\[
\begin{split}
 P''(r)&<-30r^4+\frac{112}{5}r^3-29r^2
                                      +\frac{91}{5}r-\frac{15}{4}\\
       &\le-\frac{626}{25}r^2+\frac{91}{5}r-\frac{15}{4}<0.
\end{split}
\tag{27}
\]
For the coefficient comparisons in the first line,
\(28224>28125\), \(38357310<38390625\), and
\(5583200>5578125\) suffice. In the second line use
\(r\ge3/5\), \(r\le9/10\); the final quadratic has
discriminant \((8281-9390)/25<0\).
The two exact endpoint values are
\[
 P(3/5)=\frac{2262972}{31250000}>0,\qquad
 P(9/10)=\frac{8910792}{125000000}>0.
\tag{28}
\]
Concavity proves the required positivity throughout the interval.
Equations (25) then imply \(N_eN_s>D^3\).
\(\square\)

The lemma includes both real cap cuts \(e=.27,.49\) and the
whole upper cap alias at \(\xi=.04\). Its penalty \(.08\pi\)
is independent of \(x\). At \(x=.22\), their completed cap
plane and the original ordinary main plane add to
\(\Gamma(z)-2\kappa(a_0-.22)^2\). Lemma 3 transports this
bound to every early target, for every ordinary main-line point.

## 5. The lower cap alias and true index ends

The original complete-end critical branch on the full cap rectangle
has \(.17<\Re u_c(e)<.28\) and
\(.01<\Re(e-u_c(e))<.32\). Its exact differentiated phase is
\[
 \Xi_{0,e}=-J'(e-u_c(e))+J'(e+a)+i\pi(u_c(e)-a),
                    \qquad \Xi_{1,e}=\Xi_{0,e}-g'(e).
\tag{29}
\]
Both sine arguments in the first identity have real part in
\((0,1)\). Their original logarithms have arguments between
\(-\pi/2\) and \(\pi/2\), so
\(\Im\Xi_{0,e}<59\pi/50\). For \(.27\le\Re e\le.49\),
the original \(\arg(1-e^{-2\pi ie})\) is positive. Hence
\[
                         \Im\Xi_{1,e}<59\pi/50.
\tag{30}
\]
Integrate from the lower alias height \(-.055\) to the actual
main height \(h_e<-.019\). Its length is less than \(9/250\).
The full Fourier penalty therefore gives the pointwise comparison
\[
 \Re\Xi_1(u-.055i,a)-.11\pi
 <\Re\Xi_1(u+ih_e,a)-\frac{211\pi}{3125}.
\tag{31}
\]
Adding any ordinary phase preserves this inequality. Thus (21),
rather than an uncalibrated real-height cap, pays the whole lower
alias.

The true cap ends have the separate allocated profile
\[
 E_{\rm end}-\tfrac12\Re g(a),\qquad
 E_{\rm end}=3/5+\log4/100<123/200.
\tag{32}
\]
Its derivative after adding \(F_{10}\) is
\(\log(N_s/D^2)\). On the whole positive-height private interval,
\(\cos2\pi(v+x)\le0\), so
\[
 N_s^2>169/400+9/25=313/400>49/64,
                         \qquad D^2<3/2.
\]
The latter follows from the bounds on \(B\) above. Consequently
\[
 \log(N_s/D^2)>\log(7/12)>-3/5,
\tag{33}
\]
where \(e^{3/5}>1+3/5+9/50>12/7\).
Its entire unfavorable early transport costs less than \(9/125\).
At \(x=.22\), the original bare cap plane exceeds \(79/100\),
leaving a reserve greater than \(7/40\) against (32).
The outgoing halfweight comparison is favorable by convexity of
\(\Re g\). The reserve after transport still exceeds
\[
                           7/40-9/125=103/1000.
\tag{34}
\]
Every true cap endpoint is therefore retained. Own four has no
additional physical upper-row allowance in the complete cap theorem.

## 6. Upward joins and every ordinary Fourier correction

At the early real cuts \(s=.15,.5\), the complete cap/row theorem
already bounds every cap profile and its true ends by
\(\Gamma(z)-1/2000\), with the original full first weight.
For the cap main profile, (20) implies \(\Re F_{10,ss}<0\)
throughout \(0\le\Im s\le h_0\). Thus its restriction to
either ordinary vertical zero-mode join is convex in height.
Its two endpoints are bounded by that real-cut comparison and (21).
The lower cap alias follows pointwise from (31).

For the real cap cuts and upper alias, at \(x=.22\) the old
half-index Hessian gives the same vertical convexity, so the entire
upward join is bounded by its original real-cut or main-line plane.
Lemma 3 transports it pointwise for \(0\le\eta\le h_0\).
Equation (33), with the reserve (34), handles the true cap ends
on those joins as well. Therefore both complete zero-mode joins
have the same joint bound as the main line, with room to leave
\(\gamma_{43}\).

The ordinary alias estimates do not depend on the first-type flag.
For \(Q_0=g(s+a)+g(s+b)-2g(s)+2\pi ias\), the original
argument proof in the complete early central source gives
\[
 -11\pi/5<\Im Q_{0,s}<53\pi/50\quad(y\in\mathbb R),
 \qquad \Im Q_{0,s}>-77\pi/40\quad(y\ge0).
\tag{35}
\]
Its only additional first-height hypothesis, \(c>-.078\),
holds by (2). The lower and upper ordinary heights remain
\(-1/5\) and \(4\). Exactly as in the positive-height own-three
source, for all \(.15\le v\le.5\),
\[
\begin{split}
 \Re F_{10}(v-i/5)-2\pi/5
       &<\Re F_{10}(v+ih_0)-1449\pi/12500,\\
 \Re F_{10}(v+4i)-8\pi
       &<\Re F_{10}(v+ih_0)-3\pi/10.
\end{split}
\tag{36}
\]
On the two upper vertical alias halves,
\(\partial_y(\Re F_{10}-2\pi y)<-3\pi/40\); on the two
lower halves,
\(\partial_y(\Re F_{10}+2\pi y)>47\pi/50\).
They are bounded by their own real-cut rates. These comparisons
hold after multiplication by every unchanged cap contribution.

## 7. The literal finite assembly and scope

Take the half-grid cuts
\(\ell_N=(J_L+1/2)/N\), \(r_N'=(J_R+1/2)/N\).
The exact marked factorial interpolant is
\[
 A_N(s;a,b)=e^{2\pi iNas}
 \frac{\widehat P_N(N(s+a))\widehat P_N(N(s+b))}
      {\widehat P_N(Na)\widehat P_N(Nb)\widehat P_N(Ns)^2}.
\tag{37}
\]
Its original functional equation gives \(A_N(j/N)=R_{j,N}\).
The residue formula is exactly
\[
 C^{\rm mid}_{0,N}=
       \frac{N}{2i}\oint_{\partial\mathcal R_N}^{\rm CCW}
                        \cot(\pi Ns)A_N(s;a,b)\,ds,
\tag{38}
\]
where \(\mathcal R_N\) has horizontal heights \(-1/5,4\).
Every real factorial argument stays in a fixed compact part of
\((0,1)\); the maximal shifted real part tends to \(.95\).
The original interpolation theorem allows this fixed finite height.

The constant cotangent pieces combine to \(+N\) times the real
central integral. Moving it upward gives exactly
\[
 N\left\{
 \int_{\ell_N+ih_0}^{r_N'+ih_0}A_N(s)\,ds
 +\int_{\ell_N}^{\ell_N+ih_0}A_N(s)\,ds
 -\int_{r_N'}^{r_N'+ih_0}A_N(s)\,ds\right\}.
\tag{39}
\]
Sections 3--6 pay all three terms after multiplication by the
complete cap. The nonconstant pieces retain exactly two horizontal
aliases and four vertical half-sides, paid by (35)--(36) and the
real-cut comparisons. The cap's own finite decomposition retains
its main line, both cuts, both aliases, both zero-mode joins,
four vertical alias halves, all real rows and both true index ends.
No finite row or parity correction is removed before estimating.

All symbols, contour lengths and half-grid displacements have
polynomial costs or fit in the prescribed rate tolerance. Strict
compact inequalities persist on neighborhoods needed for those
displacements. The unselected Fourier theorem supplies precisely
the two halves of \(d_N(X)\) allocated in (5), since \(c<0\).
No finite Fourier value is divided out. Equations (21), (23)--(36)
then prove (8), since \(2\gamma_{43}<1/2000\).

The complete cap input is valid on every real ordinary color; its
favorable angular loss in regular profiles can be discarded, and
its true-end bound is uniform there. The proof consequently first
gives the same product bound for that whole real interval. Its
degree in the ordinary color is less than \(N\). Bernstein--Walsh
continuation gives a fixed neighborhood of \(-2\) at arbitrarily
small additional rate cost; Cauchy's formula gives fixed derivatives
on a smaller neighborhood. This applies to the polynomial product
directly and divides by no possibly vanishing multiplier.

Together with the nonpositive-height theorem, this pays the full
central block of every actual first four/three pair at unchanged
early heights. The low block is already paid. This note does not
pay the remaining high own-three rows, selected first weights,
moving-height outer joins, or a whole open word or closed knot.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_cap_joint_early_horizontal_concavity.md | 1b623741d70402af77287b287aa1e2636b0b8d1abcb7275d5347f14ac75dbb20 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_three_positive_private_central.md | d7f54fc0a20c5ccce15b028d16dbcaee2ef0eefbea70795089da097c9730635e |
| research_mixed_half_index_contour.md | ed8d13779e734803090f778d01ddc334469cbfb7a35154ba48d6eb462c28c57e |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_first_cap_plateau_phase.md | 159a1b89eebcb72fa9ac3395435086f066b3e648c389e2417e0b61fb490ff612 |
| research_mixed_first_four_attached_height_bound.md | 42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |

The full proof and directly used source implications were read back.
The new Schur argument incorporates the parent's written derivation;
the complementary-profile transport and finite assembly are proved
here. No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test or frozen-source edit was performed.
