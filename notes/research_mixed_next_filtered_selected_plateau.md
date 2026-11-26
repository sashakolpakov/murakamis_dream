# The cardinal correction on the full selected plateau

Research deduction, 7 November 2026. The polynomial representing the
remaining physical rectangle can replace the full \(34\) prefix on the
whole selected second plateau with exponentially small
error. The estimate uses the original ordinary-next reference and its
affine marginal. It holds for both next types and for all real ordinary
colors. It does not estimate either complete Fourier coefficient.

## 1. The exact correction and reference

Let \(D=N-1\), \(r=e^{-2\pi i/N}\), and use precisely the filtered
polynomial of
[the low physical interval theorem](research_mixed_next_low_physical_interval.md),
Section 4:
\[
 F_N^{\mathrm{mid}}=(I-\Pi)(F_{34,N}-R_N^a),\qquad
 E_N=F_{34,N}-F_N^{\mathrm{mid}}
       =R_N^a+\Pi F_{34,N}-\Pi R_N^a.                    \tag{1}
\]
Here \(R_N^a\) is the complete first-coordinate deletion,
\(\Pi\) projects onto the physical second indices
\[
 b\le\lfloor\delta N\rfloor
 \quad\hbox{or}\quad b\ge\lceil11N/12\rceil ,
 \qquad
 \mathfrak l_b(Y)=N^{-1}\sum_{\nu=0}^{D}(Yr^{-b})^\nu.
                                                               \tag{2}
\]
The symbol \(b\) in (2) is a physical integer index. Below \(z\)
denotes the continuous third retained coordinate; these are different
variables. Every polynomial in (1) has degree at most \(D\) in \(Y\).

Fix the ordinary-next canonical family of
[the second-selected plateau theorem](research_mixed_second_selected_first_three_plateau_completion.md):
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),
 \qquad(\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),
 \quad \beta\in\{0,1\}.                                    \tag{3}
\]
Its external parameter is \(c=s_4^*\in K_3\cup K_4\). Both
\(s_*,t_*\) are ordinary indices, also at word length four.
In particular \(s_*,y_*\in O_4\), and
\[
 .24<\Re s_*,\Re y_*<.36,\qquad
 -.102<\Im s_*,\Im y_*<-.001.                               \tag{4}
\]
The theorem includes all canonical references in those two parameter
sets. It makes no substitution of a terminal third-vertex graph.

Write \(P=[.22,.45]\), \(H=1/100\), and use the fixed selected segment
\[
 y=x+iH,\quad x\in P,\quad Y=e^{-2\pi iy},\qquad
 z=v+i\Im z_*,\quad v\in P,\quad Z=e^{-2\pi iz}.              \tag{5}
\]
The exact error density is
\[
 \mathscr E_{\beta,N}(w;y,z)
       =E_N(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z).                \tag{6}
\]
No root sum replaces this open contour, and no conditional row is
deleted from \(C_{\beta,N}\).

Let \(Q_\beta\) have its original bare normalization
\[
 Q_\beta(t;y,z)=g(t+y)+g(t+z)-(2+\beta)g(t)
                  -g(y)-g(z)+2\pi iyt.
                                                               \tag{7}
\]
The full prefix action \(\mathcal P_{34}\) is the pre-Gram action of
[the complete following-prefix theorem](research_mixed_three_four_following_complete_prefix.md).
Set
\[
 \begin{split}
 A_*&=\Re\{\mathcal P_{34}(-2,y_*)-\tfrac12 g(y_*)\},\\
 p&=\Re\{g'(s_*+y_*)-\tfrac32g'(y_*)\},\\
 p_R&=g'(t_*+z_*)-(1+\beta/2)g'(z_*),\\
 \Lambda_{123}(z)&=
   \Re\{\mathcal P_{34}(-2,y_*)+Q_\beta(t_*;y_*,z_*)
                         -g(y_*)-\tfrac\beta2g(z_*)\}
                  +\Re\{p_R(z-z_*)\}.
 \end{split}                                                 \tag{8}
\]
These are the original absolute action and outgoing marginal.
In particular, no new additive action constant is introduced.

**Theorem.** For every sufficiently small prescribed tolerance
\(\tau>0\),
\[
 |\mathscr E_{\beta,N}(w;y,z)|\,|d_N(Z)|^{\beta/2}
 \le C_\tau N^{A_\tau}
       e^{N\{\Lambda_{123}(z)-1/500+\tau\}}                 \tag{9}
\]
uniformly on (3)--(5), for all real ordinary colors
\(w\in[-2,2]\) and both level parities. For \(\beta=0\), no
outgoing factor is inserted.
Thus a finite loss \(1/1000\) remains after the common tolerance
and polynomial prefactors. The same conclusion holds on sufficiently
small fixed complete-color neighborhoods, with fixed local mixed
derivatives as specified in Section 5.

## 2. A sharper bound for the entire correction polynomial

The proof of (17)--(21) in the low physical interval theorem gives
more than its displayed rate \(8/5\). Its low-node bound has rate
\[
 M_{\mathrm{pend}}+\epsilon(\delta)+\tau,\qquad
 M_{\mathrm{pend}}<769/500,\qquad
 \epsilon(\delta)<\Delta/8,\quad \Delta=59/440000.
                                                               \tag{10}
\]
The allowed finite and complex-color tolerances can be chosen so
that this is less than \(77/50\), since
\(77/50-769/500=1/500\). Its high-node rate is bounded by
\[
 \frac{433}{500}+\frac{85}{288}+\frac{17}{60}+\frac7{120}
                 =\frac{54101}{36000}<\frac{77}{50}.         \tag{11}
\]
The first-coordinate polynomial and its cardinal projection have
rate \(371/720\). All these bounds retain the complete prefix at
the physical nodes; the high-node estimate is not an absolute
bound on its internal first-coordinate sum.

Since \(|\mathfrak l_b(Y)|\le1\) on the unit disk, (1),
(10), and (11) imply
\[
 \sup_{|Y|\le1}|E_N(w,Y)|\le C N^A e^{77N/50}.               \tag{12}
\]
The strict reserves permit the same bound on a sufficiently small
fixed disk about \(w=-2\). The original all-real coefficient estimates
give (12) for every real ordinary color.

For a polynomial of degree at most \(D\), the maximum principle
applied outside the unit disk gives
\[
 \sup_{|Y|=R}|E_N(w,Y)|
       \le R^D\sup_{|Y|\le1}|E_N(w,Y)|,\qquad R\ge1.
                                                               \tag{13}
\]
Thus on (5) the complete correction has rate
\(77/50+2\pi H\). This includes the rows revived away from the
physical nodes.

## 3. The selected halfweight with its forcing term

Put \(\nu(y)=-\Re g(y)\). On \(x\in P\), \(0\le h\le H\),
write \(R=e^{2\pi h}<2\). The original logarithm satisfies
\[
 \Re(1-Re^{-2\pi ix})>3/5,\qquad
 \Im(1-Re^{-2\pi ix})>0.
                                                               \tag{14}
\]
Indeed \(\cos(2\pi x)\le\sin(.06\pi)<1/5\); the last
inequality follows from \(\pi<22/7\). The elementary exponential
series gives \(e^{\pi/50}<2\). Therefore the original argument
lies in \((0,\pi/2)\), without changing its lift, and
\[
 \partial_h\nu(x+ih)
     =\arg(1-Re^{-2\pi ix})<\pi/2,\qquad
 \nu(x+ih)\le-J(x)+\pi h/2.                                 \tag{15}
\]

Define the angle-dependent bound
\[
             H_0(x)=\max\{-J(x)/2-3\pi/400,0\}.
                                                               \tag{16a}
\]
The complete polynomial estimate in
[the Fourier weight continuation](research_mixed_fourier_weight_continuation.md)
has the two rates \(\nu(y)\) and \(2\pi h\). After the exact
selected multiplier \(Y^{-N}\) and a square root, it gives
\[
 \begin{split}
 |d_N(Y)Y^{-N}|^{1/2}
 &\le C_\tau N^{A_\tau}
    e^{N\{\frac12\max(\nu(y)-2\pi H,0)+\tau\}}\\
 &\le C_\tau N^{A_\tau}e^{N\{H_0(x)+\tau\}},\qquad
          H_0(x)\le1/12-3\pi/400.
 \end{split}                                                 \tag{16}
\]
Here \(\max_{[0,1]}(-J)<1/6\), as used in
[the boundary strip bounds](research_mixed_boundary_strip_bounds.md),
and \(1/12-3\pi/400>0\). Both the factorial branch and the
polynomial forcing branch remain in the maximum in (16).
There is no division by \(d_N\).

## 4. The original plane and a strict comparison

Let \(B_3(x,v)\) be the complete ordinary third-factor supporting
plane, including its original quadratic losses. The full-plateau
height theorem, equation (22) in
[the first-collar full-target proof](research_mixed_first_collar_full_plateau_second_target.md),
gives
\[
 |C_{\beta,N}(Y,Z)|
 |d_N(Y)Y^{-N}|^{1/2}|d_N(Z)|^{\beta/2}
 \le C_\tau N^{A_\tau}
                  e^{N\{B_3(x,v)+7/250+\tau\}}.             \tag{17}
\]
Its incoming reference is the ordinary type-four output \(y_*\);
its own index \(t_*\) and outgoing target belong to the original
ordinary next map. Thus (3)--(5) satisfy its source hypotheses
for both values of \(\beta\). Equation (17) contains the whole
conditional polynomial, all physical tails and all alias currents,
and bounds both Fourier alternatives. The selected height \(H=.01\)
is inside its original permitted interval \([0,7/500]\).

The actual stationarity in the second retained coordinate cancels
the two real incoming marginals. Consequently the original allocation
gives
\[
 A_*+p(x-\Re y_*)+B_3(x,v)\le\Lambda_{123}(z).
                                                               \tag{18}
\]
To check the halfweight in this identity, the first term is
\(\mathcal P_{34}-g(y)/2\); the third term has
\(Q_\beta-g(y)/2-\beta g(z)/2\). Their sum is exactly
the reference expression in (8).

There are elementary uniform bounds for the two quantities on the
left of (18). The actual following-prefix theorem gives
\(\Re\mathcal P_{34}(-2,y_*)>7/4\). The negative-height
four-domain estimate in the Fourier weight theorem gives
\[
 \nu(y_*)>\chi=\frac{117}{800\pi}>\frac{819}{17600},
 \qquad A_*>\frac74+\frac{819}{35200}.                        \tag{19}
\]
For the real marginal, both original moduli obey
\[
 1<|1-e^{-2\pi i(s_*+y_*)}|<2,\qquad
 1<|1-e^{-2\pi iy_*}|<2.                                   \tag{20}
\]
The first follows from \(\Re(s_*+y_*)\in(.48,.72)\), whose
cosine is negative, and its strictly negative height. For the second,
the radius is greater than \(1/2\), since
\(.204\pi<(51/250)(22/7)<693/1000<\log2\).
Also \(\cos(2\pi\Re y_*)\le\sin(.02\pi)<1/4\), so that
the radius exceeds twice this cosine. This proves the lower modulus
bound; the upper bound follows from a radius below one.
The witnesses \(\log2>693/1000\) and \(\log2<7/10\) are
the same elementary inequalities used in
[the low-index kernel margin](research_mixed_next_low_index_kernel_margin.md)
and [the binomial end bound](research_mixed_three_four_next_binomial_end_bound.md).

The envelope derivative of the original pre-Gram action is
\(\mathcal P_{34}'=g'(s_*+y_*)-g'(y_*)\).
Taking real parts in (20) therefore gives
\[
 -\tfrac32\log2<p<\log2,\qquad |p|<21/20.                   \tag{21}
\]
Combining (12)--(13), (16), and (17), and writing
\(a=\Re y_*\), the correction rate minus the first-pair tangent
is at most
\[
 \frac{196}{125}+\frac{\pi}{50}
                   +H_0(x)-p(x-a)-A_*+\tau.                \tag{22}
\]
The sign of the actual marginal controls the entire interval.

First suppose \(p\le0\). The own radius in (20) is in
\((1/2,1)\), and its cosine is less than \(1/4\); its modulus
is therefore at most its unit-radius value \(2\sin\pi a\).
The other modulus exceeds one. Consequently
\[
        -p\le k(a):=\tfrac32\log(2\sin\pi a).
                                                               \tag{23}
\]
Moreover \(k(a)>\frac12\log2\). For example,
\(\pi>25/8\) gives
\(\sin(.24\pi)>\sin(3/4)>87/128>2/3\), and
\((4/3)^3>2\). Wherever \(H_0\) is positive its derivative
is \(-\frac12\log(2\sin\pi x)\ge-\frac12\log2\);
where it vanishes its derivative is zero. Thus
\(H_0(x)+k(a)(x-a)\) is increasing on \([a,.45]\).
Also
\[
 -J(.45)/2
   =\tfrac12\int_{.45}^{.5}\log(2\sin\pi u)\,du
       <\log2/40<3\pi/400 ,
 \qquad H_0(.45)=0.
                                                               \tag{24}
\]
For \(x<a\), \(H_0(x)-p(x-a)\le H_0(x)\le1/12\).
For \(x\ge a\), its maximum is at most \(k(a)(.45-a)\).
Concavity of \(\log(2\sin\pi a)\) and its tangent at \(a=1/4\)
give, with \(u=a-1/4\),
\[
 \begin{split}
 k(a)(.45-a)
 &\le\tfrac32\left\{\tfrac1{10}\log2+
        (\pi/5-\tfrac12\log2)u-\pi u^2\right\}\\
 &<\tfrac32\left\{\frac7{100}
                  +\frac{(31/105)^2}{12}\right\}<\frac3{25}.
 \end{split}                                                 \tag{25}
\]
Here \(\log2>2/3\), \(\pi<22/7\), and \(\pi>3\)
bound the positive linear coefficient by \(31/105\) and the
quadratic maximum by its square divided by \(12\).
The last rational comparison reduces to \(96100<132300\).
Therefore the positive rate before subtracting \(A_*\) in (22)
is less than
\[
        \frac{196}{125}+\frac{11}{175}+\frac3{25}
                                     <\frac{1751}{1000}.
                                                               \tag{26}
\]
By (19), \(A_*>177/100\), so this case has more than the
claimed gap \(1/500\).

Now suppose \(p\ge0\). Since \(x>1/6\), \(H_0\) is
nonincreasing on \(P\), so \(H_0(x)-p(x-a)\) is largest at
\(x=.22\). A sharper upper bound on \(p\) suffices there.
Writing \(r_*=e^{2\pi\Im y_*}>1/2\), its own squared modulus
increases with \(r_*\) and obeys
\[
 |1-r_*e^{-2\pi ia}|^2
      >\frac54-\cos(2\pi a)
      >\frac54-\frac{11}{175}=\frac{831}{700}.
                                                               \tag{27}
\]
The elementary inequality \(\log t\ge2(t-1)/(t+1)\) gives
\[
 \log|1-r_*e^{-2\pi ia}|>\frac{131}{1531},\qquad
 p<\frac7{10}-\frac32\frac{131}{1531}.
                                                               \tag{28}
\]
Since \(a-.22<7/50\), this yields
\[
 p(a-.22)<\frac7{50}
                \left(\frac7{10}-\frac{393}{3062}\right)
                             <\frac{801}{10000}.            \tag{29}
\]
For the last comparison,
\(2751\cdot10000-179\cdot153100=105100>0\).
Using \(H_0(x)\le1/12-3\pi/400\), the complete positive cost
in (22) is therefore less than
\[
          \frac{196}{125}+\frac1{12}
                    +\frac{\pi}{80}+\frac{801}{10000}.
                                                               \tag{30}
\]
Finally,
\[
 \frac74+\frac{819}{35200}
  -\left(\frac{196}{125}+\frac1{12}
                    +\frac{11}{280}+\frac{801}{10000}\right)
                         >\frac1{500}.                    \tag{31}
\]
After subtracting \(1/500\), the difference in (31) is
\(10127/18480000>0\). This uses \(\pi/80<11/280\).
Together with (18), the two sign cases prove (9) on all of \(P\).

## 5. Finite contour meaning and derivatives

Orient the selected segment (5) from left to right. The exact
difference between the two selected integrals on this segment is
\[
 N\int_{P+iH}
  \{F_{34,N}(w,Y)-F_N^{\mathrm{mid}}(w,Y)\}
       d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)\,dy
       =N\int_{P+iH}\mathscr E_{\beta,N}(w;y,z)\,dy .
                                                               \tag{32}
\]
Its length and the factor \(N\) cost only a polynomial prefactor.
The entire conditional source and the exact original scalar \(N\)
are retained. Thus (9) also bounds (32), with the same outgoing
halfweight. The estimate uses no identity between the segment and
a subset of physical roots.

For fixed ordinary-color derivatives, apply Markov's inequality to
the full coefficient polynomials in the proof of (12), before the
positive bounds and the cardinal sum. Their degrees are \(O(N)\).
This costs a fixed power of \(N\). For complex parameters, fix a
reference (3) and keep the segment in (32) fixed. The strict
inequalities above persist on smaller fixed neighborhoods.
The exact integrand is holomorphic there. Near the actual outgoing
\(z_*\), the outgoing type-four weight, when present, has its
original nonzero factorial asymptotic; a local square-root branch
may be chosen. Cauchy's formula then gives every fixed mixed
normalized derivative of (32) with an exponential loss, for example
\(1/2000\) after shrinking the neighborhoods and allowing polynomial
factors. The normalization is the original next conditional action;
its outgoing halfweight is precisely the one already displayed
in (8)--(9). At arbitrary real targets \(v\in P\), (9) is a
weighted absolute estimate and asserts no division through a zero
of \(d_N(Z)\).

The theorem permits replacement of the prefix by its filtered
polynomial on the whole selected plateau. It does not by itself bound
the original full-prefix integral on that plateau, the remaining
selected contour, or the unselected coefficient. The physical
middle rectangle and the local unwrapped geometric contribution
retain exactly the scope of the low physical interval theorem.
