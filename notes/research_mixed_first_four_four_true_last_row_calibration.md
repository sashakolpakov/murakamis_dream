# The complete first-four cap with the last row of its four neighbor

Research proof, 10 November 2026. At the actual fixed heights of a
word beginning with two fours, the complete first cap and the true
last-row rate of the next ordinary factor lie below their original
joint supporting plane throughout the early first interval. The
proof retains the cap's coherent main contour, both real cuts,
both aliases, and its true index ends. It does not replace the cap
by the sum of its absolute private rows.

There are two height regimes. In the deeper regime the main and
real-cut products transport to the old plateau; the original alias
and endpoint reserves pay their possible transport costs. In the
shallower regime the ordinary last row is below its half row.
The conclusion also bounds every sufficiently late physical row,
including the literal final index, at both level parities.
The adopted own-four high-row principle and complete low/central
sources then give a bound for the literal full first \(4,4\) pair.

## 1. The unchanged source and joint plane

Fix an actual positive three/four open word of length \(m\ge3\)
whose first two types are four. The original coupled reference is

\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad e_*=u_*+ih_*.
\tag{1}
\]

Here \(a_*=t_1^*\), \(b_*=t_2^*\), and \(e_*\) is the first
private cap coordinate. The
[attached-height theorem](research_mixed_first_four_attached_height_bound.md),
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md),
and actual ordinary-image scope retained in the
[joint low-row theorem](research_mixed_early_joint_low_tail.md) give

\[
\begin{gathered}
 \frac{123}{500}<a_0<\frac7{20},\qquad
 -\frac{39}{500}<c<-\frac1{50},\qquad
 -\frac{51}{500}<d<0,\\
 \frac{333}{1000}<u_*<\frac{363}{1000},\qquad
 -\frac{51}{1000}<h_*<-\frac{19}{1000}.
\end{gathered}
\tag{2}
\]

No independent box point is substituted for this reference. Keep
the target heights fixed and put

\[
 a=x+ic,\quad b=z+id,\qquad
 \frac1{10}\le x\le\frac{11}{50},\quad
 z\in P=[11/50,9/20].
\tag{3}
\]

All primitives and logarithmic lifts below are those of the exact
open source. With \(J'(v)=\log(2\sin\pi v)\) and

\[
 g(v)=J(v)+\frac{\pi i}{2}(v-v^2),\qquad J(0)=0,
\]

define the allocated cap phase and ordinary phase by

\[
\begin{split}
 \Xi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea-g(e)-\tfrac12g(a),\\
 F(s;a,b)&=g(s+a)+g(s+b)-3g(s)+2\pi ias
                            -\tfrac32g(a)-\tfrac32g(b).
\end{split}
\tag{4}
\]

The critical actions are \(L=\operatorname{stat}_e\Xi\) and
\(\phi=\operatorname{stat}_s F\), on their original branches.
Their first-coordinate marginals cancel:

\[
 L'(a_*)+\phi_a(a_*,b_*)=0.
\tag{5}
\]

Set \(\kappa_*=1/2500000\) and retain exactly the plane from
equation (9) of the joint low-row theorem:

\[
\begin{split}
 \Gamma(z)={}&\Re L(a_*)+\Re\phi(a_*,b_*)
       +\Re\phi_b(a_*,b_*)(z-b_0)-\kappa_*(z-b_0)^2,\\
 \gamma_{44}&=\kappa_*(a_0-11/50)^2
             >\kappa_*(13/500)^2>0.
\end{split}
\tag{6}
\]

For \(r_N=e^{-2\pi i/N}\), put \(P_j=(r_N;r_N)_j\),

\[
 p_j(X)=(r_NX;r_N)_j,\quad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},
 \qquad R_{j,N}(a,b)=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^3}.
\tag{7}
\]

The complete first cap is \(U_{1,N}(w,X)\). Its complete unselected
first Fourier weight is \(d_N(X)\); the ordinary outgoing
halfweight is \(|d_N(Y)|^{1/2}\). No selected monomial or
\(1+X^{-N}\) is inserted in the quantity considered here.

The allocated ordinary row rate is

\[
\begin{split}
 \mathcal R(s;a,b)={}&\int_0^s\log|1-e^{-2\pi i(a+t)}|\,dt
            +\int_0^s\log|1-e^{-2\pi i(b+t)}|\,dt\\
 &-3J(s)-2\pi cs-\tfrac12\Re g(a)-\tfrac12\Re g(b).
\end{split}
\tag{8}
\]

In particular, because \(c,d<0\), its exact endpoint is

\[
 \mathcal R(1;a,b)=-2\pi c-\tfrac12\Re g(a)-\tfrac12\Re g(b).
\tag{9}
\]

This is the endpoint of the full product-integral rate, not a
replacement of the literal row \(j=N-1\) by a different finite
coefficient.

Let \(\mathcal A(a)\) be the maximum of the five allocated cap
profiles in the
[complete fixed-height source](research_mixed_cap_early_fixed_height_full_source.md),
using main height \(h_*\), and its true-end profile. Thus its
regular profiles are \(\Re\Xi(e,a)-\mathfrak p_e\), where

\[
\begin{array}{c|c|c}
 \text{profile}&e&\mathfrak p_e\\ \hline
 \text{main}&u+ih_*,\quad .27\le u\le.49&0\\
 \text{real cuts}&.27,\ .49&0\\
 \text{lower alias}&u-.055i,\quad .27\le u\le.49&.11\pi\\
 \text{upper alias}&u+.04i,\quad .27\le u\le.49&.08\pi .
\end{array}
\tag{10}
\]

The true-end profile is

\[
 E_{\rm end}-\tfrac12\Re g(a),\qquad
 E_{\rm end}=\frac35+\frac{\log4}{100}<\frac{123}{200}.
\tag{11}
\]

For own four there is no additional upper-row allowance. These
profiles already include both unweighted joins, all four vertical
alias halves, the full physical tails, and both parity stops.

## 2. A radial half-row comparison

Write \(r=e^{2\pi c}\) and \(t=e^{2\pi d}\). By (2),

\[
                  0<r<9/10,\qquad 1/2<t<1.
\tag{12}
\]

For the second assertion, \(2\pi(51/500)<2/3\), while the
positive-series bound

\[
 e^v\le1+v+\frac{v^2}{2(1-v/3)}\qquad(0\le v<3)
\tag{13}
\]

gives \(e^{2/3}\le41/21<2\). The bound \(r<9/10\) also
follows from \(c<-1/50\) and \(e^{\pi/25}>1+3/25>10/9\).

For \(0<\rho<1\), let

\[
 G_\rho(v)=\Re g\left(v+\frac{i\log\rho}{2\pi}\right),
 \qquad \mathcal S_\rho(v)=-G_\rho(v)-G_\rho(1/2-v).
\tag{14}
\]

The original radial primitive, also used in the
[right-tail reflection theorem](research_mixed_right_tail_reflection.md),
gives

\[
 \mathcal S_\rho(v)=\frac1\pi
       \sum_{\substack{n\ge1\\n\ {\rm odd}}}
                       \frac{\rho^n\sin(2\pi nv)}{n^2}.
\tag{15}
\]

This function is symmetric under \(v\mapsto1/2-v\) and
strictly increases for \(0<v<1/4\). Indeed its derivative is

\[
 \log|1-\rho e^{-2\pi i(1/2-v)}|
       -\log|1-\rho e^{-2\pi iv}|>0.
\]

It also strictly increases in \(\rho\) for \(0<v<1/2\):
differentiating the absolutely convergent series gives

\[
 \partial_\rho\mathcal S_\rho(v)
 =\frac1{\pi\rho}\Im\operatorname{artanh}(\rho e^{2\pi iv})>0.
\tag{16}
\]

Here the quotient
\((1+\rho e^{2\pi iv})/(1-\rho e^{2\pi iv})\) has
positive real and imaginary parts. Thus the logarithm defining
the last imaginary part is its continuation from \(\rho=0\),
and has positive argument.

**Lemma 1.** If \(r\ge2/3\) and \(4/25\le x\le11/50\),
then, throughout (3),

\[
          \mathcal R(1/2;a,b)-\mathcal R(1;a,b)>\frac1{72}.
\tag{17}
\]

*Proof.* The exact reflection identity gives

\[
 \mathcal R(1/2;a,b)-\mathcal R(1;a,b)
       =\mathcal S_r(x)+\mathcal S_t(z)+\tfrac12\log r.
\tag{18}
\]

All halfweights cancel in this difference. Equations (12),
(15)--(16) imply

\[
 \mathcal S_r(x)\ge\mathcal S_{2/3}(4/25),\qquad
 \mathcal S_t(z)>\mathcal S_{1/2}(1/20).
\tag{19}
\]

At each of these two angles the \(n=3\) sine is positive.
Also

\[
 \sin(8\pi/25)>5/6,\qquad \sin(\pi/10)>3/10,
 \qquad\sum_{\substack{n\ge5\\n\ {\rm odd}}}\frac1{n^2}<\frac18.
\tag{20}
\]

For the first sine inequality, \(8\pi/25>1\) and
\(\sin1>1-1/6\). For the second use
\(\pi/10>5/16\) and
\(\sin(5/16)>5/16-(5/16)^3/6>3/10\).
The final bound follows from convexity of \(v^{-2}\): each
odd summand is smaller than one half of its integral over the
interval of length two centered there. The integrals telescope
to \(\tfrac12\int_4^\infty v^{-2}dv=1/8\).
Consequently

\[
 \mathcal S_{2/3}(4/25)>\frac{131}{243\pi},\qquad
 \mathcal S_{1/2}(1/20)>\frac{187}{1280\pi}.
\tag{21}
\]

The sum in (21) exceeds \(13/60\): replacing \(\pi\) by
\(22/7\) reduces this to
\(89510820>88957440\). Finally the positive atanh series gives

\[
 \log(3/2)
   <\frac25+\frac{2}{3}\sum_{j\ge1}(1/5)^{2j+1}
   =\frac{73}{180}.
\tag{22}
\]

Combining (18)--(22) yields
\(13/60-73/360=1/72\), proving the lemma. \(\square\)

## 3. The deeper regime: main contour and real cuts

For a regular cap point \(e=u+ih\) let

\[
 N_e=|1-r e^{2\pi h}e^{-2\pi i(u+x)}|,
 \qquad D=|1-r e^{-2\pi ix}|.
\tag{23}
\]

Adding (9) to the original allocated cap phase, with its alias
penalty unchanged, gives the exact fixed-height derivative

\[
 \partial_x\{\Re\Xi(e,a)+\mathcal R(1;a,b)-\mathfrak p_e\}
                         =\log(N_e/D^2).
\tag{24}
\]

For the true-end cap profile it is instead \(-\log D\).
The denominator exponent two in (24) uses both original halves
of the first Fourier weight. No argument or chirp is deleted.

Suppose \(r\le2/3\). On the original main line,
\(e^{2\pi h_*}>18/25\). In fact \(2\pi|h_*|<13/40\),
and (13) gives
\(e^{13/40}\le11849/8560<25/18\).
The real cuts have the larger private radius one. On all the
early interval the original angular bounds give

\[
 N_e^2>1+\frac{324}{625}r^2+\frac{216}{625}r,
 \qquad D^2<1+r^2-\frac9{25}r.
\tag{25}
\]

Here \(u+x\in[.37,.71]\), so
\(\cos2\pi(u+x)<-6/25\), while
\(\cos2\pi x>9/50\). These are the same elementary
sine bounds retained in the joint low-row proof.
Subtracting the square of the second bound from the first gives

\[
 N_e^2-D^4>rP(r),\qquad
 P(r)=\frac{666}{625}-\frac{1007}{625}r
                              +\frac{18}{25}r^2-r^3>0.
\tag{26}
\]

Indeed \(P'(r)<0\) for every real \(r\): the discriminant of
\(-1007/625+36r/25-3r^2\) is negative and its leading
coefficient is negative. At the present right endpoint,
\(P(2/3)=256/16875>0\). Thus (24) is positive for the
whole main line and both real cuts.

Transport these three profiles to \(x=11/50\). There the
[completed cap plane](research_mixed_first_cap_plateau_completion.md)
and [completed ordinary last-row plane](research_mixed_typed_last_row_support_completion.md)
apply at the same correlated reference. Their slopes cancel by
(5); each supplies its first-coordinate quadratic term. Hence
every transported profile is at most

\[
                         \Gamma(z)-2\gamma_{44}.
\tag{27}
\]

The maximum over the private main coordinate is taken only after
this pointwise comparison. It does not require differentiability
or uniqueness of a moving maximizing coordinate.

## 4. The deeper regime: both complete aliases and true ends

For an alias, \(e^{2\pi h}\) is its prescribed radius, which
need not obey the main-line lower bound used in (25). We keep
its entire original penalty and anchor it instead at \(x=a_0\).
Lemma 3 of the
[original complete-current cap proof](research_mixed_cap_outer_contour_reduction.md)
gives an upper-alias deficit greater than \(3/20\), and a
lower-alias deficit greater than \(6/25\), relative to the
actual cap critical value at \(a_*\). Adding the ordinary last
row at \((a_*,z+id)\), whose plateau plane is already proved,
therefore bounds each joint alias by

\[
                             \Gamma(z)-3/20.
\tag{28}
\]

This application is at the original attached point \(a_*\).
It does not enlarge the old alias-curvature certificate to the
early target rectangle.

We now bound its possible transport loss from \(a_0<7/20\)
to any \(x\ge1/10\), still assuming \(r\le2/3\).
For \(x\le11/50\), \(u+x\in[.37,.71]\) makes \(N_e>1\),
at either alias radius. Moreover \(D^2<271/225\). Thus

\[
                    \log(N_e/D^2)>-46/225.
\tag{29}
\]

For \(11/50\le x\le7/20\), the sum \(u+x\) lies in
\([.49,.84]\). Its cosine is less than \(11/20\): at the
largest possible cosine use
\(\cos(8\pi/25)<\cos1<13/24<11/20\).
For every positive alias radius \(\rho\), it follows that

\[
 N_e^2\ge1+\rho^2-\frac{11}{10}\rho
             \ge\frac{279}{400}>\frac{25}{36}.
\tag{30}
\]

On \(x\le3/10\), \(\cos2\pi x>-1/3\), so
\(D^2<17/9\) and

\[
             \log(N_e/D^2)>\log(15/34)>-5/6.
\tag{31}
\]

For the last inequality,
\(e^{5/6}>1+5/6+25/72+125/1296=2951/1296>34/15\).
On the remaining \(x\le7/20\), the elementary bound
\(\sin(\pi/5)<3/5\) gives \(D^2<101/45\), whence

\[
             \log(N_e/D^2)>\log(75/202)>-1.
\tag{32}
\]

Here \(e>65/24>202/75\). The sine bound follows by squaring
\(\sin(\pi/5)=\sqrt{10-2\sqrt5}/4\); for example
\(\sqrt5>53/25\) suffices. The bound
\(\cos(3\pi/5)>-1/3\) in (31) similarly follows from
\(\sqrt5<7/3\).

Integrate (29)--(32) over the complete containing intervals,
even if the actual path is shorter. Its total possible loss is
less than

\[
 \frac3{25}\frac{46}{225}
 +\frac2{25}\frac56+\frac1{20}
       =\frac{46}{1875}+\frac1{15}+\frac1{20}.
\tag{33}
\]

Subtracting this from (28) leaves

\[
 \Re\Xi(e,a)+\mathcal R(1;a,b)-\mathfrak p_e
                         <\Gamma(z)-\frac{11}{1250}.
\tag{34}
\]

Every private alias coordinate is included before taking its
maximum. Both original alias penalties are unchanged.

For the true-end cap profile, anchor at \(x=11/50\).
The original bare cap plane exceeds \(79/100\), whereas
(11) is less than \(123/200\). Its reserve exceeds \(7/40\),
also after allocating the halfweight, as proved in Section 3 of
the joint low-row theorem. The ordinary last row has its old
plateau plane. On the early interval its combined derivative is
\(-\log D>-23/225\), by the same bound used in (29).
Its entire possible transport loss is less than \(23/1875\).
The reserve remains greater than \(1/10\). This treats every
true cap endpoint row rather than discarding an unfavorable
endpoint profile.

## 5. The shallower regime and the complete rate conclusion

Suppose \(r\ge2/3\). On \(4/25\le x\le11/50\),
Lemma 1 and the complete cap-times-half-row comparison, equation
(23) of the joint low-row theorem, give

\[
 \mathcal A(a)+\mathcal R(1;a,b)
            <\Gamma(z)-\frac1{2000}-\frac1{72}.
\tag{35}
\]

This uses a comparison of the complete profile rates, not an
inference about rates from a finite upper bound at one half row.
That source's proof establishes the cap-profile comparison
individually, including its true-end alternative.

For \(x\le4/25\), each regular cap point in (10) has \(N_e>1\),
and \(D^2<1+r^2-r<1\), since \(r<1\). Thus (24) is
positive for every main, cut and alias point. The true-end
derivative \(-\log D\) is positive as well. Transport all these
profiles to \(x=4/25\), keeping their exact penalties. Inequality
(35) consequently holds throughout the early interval in this
regime.

Together with (27), (34) and the true-end estimate, this proves
the source-rate statement

\[
 \boxed{\quad
       \mathcal A(a)+\mathcal R(1;a,b)
                         \le\Gamma(z)-\gamma_{44}.
       \quad}
\tag{36}
\]

Indeed \(\gamma_{44}<\kappa_*\), which is smaller than each
fixed reserve in Sections 4--5; Section 3 retains \(2\gamma_{44}\).
The reference ranges in (2) give a positive uniform lower bound
in (6). All cases preserve the original first-coordinate marginal
cancellation and the remaining outgoing marginal.

## 6. Literal late rows, colors and exact scope

Let

\[
 j_0(x,z,N)=\left\lceil N\{1-\min(x,z)\}\right\rceil.
\tag{37}
\]

The reflection proof's Lemma 1 uses only
\(0<x,z<1/2\) and \(0\le v\le\min(x,z)\), although
its original statement placed both angles on the plateau.
The same integral proof therefore applies here: with the exact
drift \(-2\pi c>0\) retained, it gives

\[
 \mathcal R(s;a,b)\le\mathcal R(1;a,b),
                  \qquad 1-\min(x,z)\le s\le1.
\tag{38}
\]

There is no endpoint-only assertion for the preceding high rows
in this deduction.

The original zero-safe product estimate, stated explicitly in
Section 5 of the
[adjoining contour source](research_mixed_first_attached_complete_contour_envelope.md),
bounds every literal row (7) by (8), with an arbitrarily small
uniform rate tolerance and polynomial cost. This particular
row argument needs only compact outer targets: numerator
logarithms can be regularized positively, their integral errors
converge uniformly, and the unchanged denominator factorial has
its \(O(\log N)\) endpoint error. It does not use a taper relation,
an index root, or a central-contour cotangent guard.
Both \(a,b\) have negative height and real part in \((0,1/2)\),
so the original
[Fourier-weight theorem](research_mixed_fourier_weight_continuation.md)
supplies precisely the allocations in (4), (8). No finite
Fourier polynomial is divided out.

**Theorem 2.** For every \(\tau>0\), both parities satisfy

\[
\begin{split}
 &|U_{1,N}(w,X)|\,|d_N(X)|\,|d_N(Y)|^{1/2}
       \sum_{j=j_0(x,z,N)}^{N-1}|R_{j,N}(a,b)|\\
 &\hspace{15mm}\le C_\tau N^{A_\tau}
             \exp N\{\Gamma(z)-\gamma_{44}+\tau\}.
\end{split}
\tag{39}
\]

It is uniform in (3) and every real ordinary color \(w\in[-2,2]\).
It holds on a sufficiently small fixed ordinary-color neighborhood
of \(-2\), and for every fixed derivative of the cap in that color
on a smaller neighborhood, with polynomial cost. In particular
the literal final row \(j=N-1\) has this bound for all sufficiently
large \(N\).

*Proof.* The complete cap source gives (10)--(11) at every real
ordinary color. Its regular term has a favorable angular loss,
which may be discarded; its true-end term is uniform on the full
real color interval. All unweighted joins, aliases, compact and
true endpoint rows are already included. Multiply by each
ordinary row bound, use (36), (38), and sum at most \(N\) rows.
Choose the finitely many source tolerances within the prescribed
\(\tau\). This proves the real-color statement without deleting
any row or odd-level zero.

The product is a polynomial of degree less than \(N\) in \(w\)
times color-independent factors. The interval Bernstein--Walsh
bound extends its absolute estimate to a fixed neighborhood with
an arbitrarily small additional rate cost. Cauchy's formula on
a smaller fixed neighborhood gives the color derivatives.
At a zero of a color-independent multiplier the asserted bound
is immediate; this argument requires no division there.
\(\square\)

## 7. The complete early first-four/four pair

The [adopted own-four high-row theorem](research_mixed_early_own_four_high_rows.md),
Theorem 1 and Corollary 2, applies to either first type under the
actual height conditions in (2). It bounds every high row by the
maximum of the continuous half-row and last-row rates, and then
proves the full finite sum bound with both endpoint groups retained.
The third own factorial pays the reflected drift; no sign or
nondegeneracy of a high-row stationary point is required.

The half-rate branch, after multiplication by the complete cap,
is below \(\Gamma-1/2000\) by the joint low-/half-row theorem.
The last-rate branch is (36). Consequently

\[
\begin{split}
 &|U_{1,N}(w,X)|\,|d_N(X)|\,|d_N(Y)|^{1/2}
        \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,b)|\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
                  e^{N\{\Gamma(z)-\gamma_{44}+\tau\}}.
\end{split}
\tag{40}
\]

This conclusion uses the continuous profile comparisons before
taking finite bounds. It does not divide by, or assume a lower
bound for, a physical half-row value.

**Corollary 3.** With the hypotheses and exact weights above, the
complete original ordinary factor
\(C_{1,N}(X,Y)=\sum_{j=0}^{N-1}R_{j,N}(a,b)\) satisfies

\[
 \boxed{\quad
 |U_{1,N}(w,X)C_{1,N}(X,Y)|\,|d_N(X)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_{44}+\tau\}}.
 \quad}
\tag{41}
\]

Its scope in real ordinary colors, fixed ordinary-color
neighborhoods, derivatives, and parities is the same as Theorem 2.

*Proof.* Split the literal index set into the disjoint blocks

\[
\begin{array}{ll}
 0\le j\le\lfloor N/8\rfloor,&\text{low},\\
 \lfloor N/8\rfloor+1\le j\le\lceil N/2\rceil-1,
                                      &\text{central},\\
 \lceil N/2\rceil\le j\le N-1,&\text{high}.
\end{array}
\tag{42}
\]

The first block, multiplied by the complete cap and exactly the
weights in (41), has deficit \(1/2000\) by the joint low-row
theorem. For the second block use Theorem 1 of the
[complete joint central source](research_mixed_early_joint_central_source.md).
Its private-height condition is automatic here: the actual
ordinary vertex has own type four, so \(\Im s_*<0\).
It gives the same deficit \(\gamma_{44}\) as (6), with the
original left cut \(1/8\), the full interval through \(1/2\),
both downward zero-mode joins, both horizontal Fourier corrections,
and all four vertical alias halves. Its exact residue coefficient
and all original source scalars remain unchanged. The high block
is (40). Adding these three bounds proves (41), since
\(\gamma_{44}<1/2000\).

All three statements first hold uniformly on the whole real
ordinary-color interval, with the cap summed completely. Apply
the same degree continuation and Cauchy argument as in Theorem 2
to obtain the common fixed color neighborhood and derivatives.
Allocate all source tolerances within the single prescribed
\(\tau\). This completes the exact finite index partition at
both level parities. \(\square\)

The corollary is a complete first-pair upper bound at unchanged
actual heights, with the second target on its horizontal plateau.
It does not move the heights or include the selected first
Fourier monomial. The original external scalar and every later
cut halfweight remain exactly those of the open-source identity.
Further outer contour pieces and whole-word propagation keep
their separate hypotheses. No signed lower bound, whole-word,
closed-knot, or finite-exception conclusion is asserted.

## Frozen direct sources

All required statements and source domains were read directly.

| Source | SHA-256 |
|---|---|
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_cap_outer_contour_reduction.md | 52bd01353c084aa8bb8d74a1abd015c0cfebdbe6a796c8958bb8796aaba0f9b4 |
| research_mixed_first_four_attached_height_bound.md | 42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
| research_mixed_typed_last_row_support_completion.md | 70e842fee569d7429cec8fe38441012dd5775c5fb248bba6656a2ea7cc1b24aa |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_first_attached_complete_contour_envelope.md | faa0afee38a1b18c2694e7bd2ad44c069d3880116352d66c3b11ac8d3dad1302 |
| research_mixed_early_own_four_high_rows.md | 62c3d5070d15c093ae8ab10cb373e9624a497d29743d6cd909bc5d7a33daebb6 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |

Only written inequalities were used. No mathematical numerical
evaluation, saved-value arithmetic, import, compilation, test,
or frozen-source edit was performed.
