# The small Newton indices of the terminal type-three sum

Research deduction, 5 November 2026. The exact type-three terminal
reduction has a uniformly negligible sector \(l/N\le1/200\), on the
full real target plateau and at all permitted target heights. This is
a bound on its positive double-sum majorant. The remaining Newton
indices are kept coherent. No root, parameter cover, or approximation
of the original outgoing polynomial is used.

## 1. Exact source, allocation, and real-row rate

Use the original conventions of the
[terminal Newton reduction](research_mixed_terminal_three_newton_reduction.md):
\[
\begin{split}
r=e^{-2\pi i/N},\qquad q=e^{\pi i/N},\qquad
P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,\\
\mathcal V_{0,N}(w,X)
 =N\sum_{l=0}^{N-1}\frac{(-q)^{-l}e_l(w)}{P_l}
       C_{1,N}(X,r^l),\\
C_{1,N}(X,r^l)
 =\sum_{i=0}^{N-1-l}
       \frac{X^{-i}p_i(X)p_i(r^l)}{P_i^3}.
\end{split}
\tag{1}
\]
The support \(i+l<N\) follows from the literal factor \(p_i(r^l)\),
independently of the ordinary color \(w\). The factor \(P_l^{-1}\),
all three factors \(P_i^{-1}\), the lift of \((-q)^{-l}\), and the
chirp \(X^{-i}\) remain present.

Let \(\mathcal V^{\rm low}_{0,N}\) denote (1) restricted to
\(l/N\le1/200\). Its positive majorant is the sum of the absolute
values of its original double summands, including the factor \(N\).
Put
\[
a=y+ih\in[.22,.45]+i[-.12,.12],\qquad X=e^{-2\pi ia},
\quad u=l/N,\quad t=i/N,
\tag{2}
\]
and write
\[
J(x)=\int_0^x\log(2\sin\pi s)\,ds,\qquad
L(x)=-J(x)\quad(0\le x\le1/2).
\tag{3}
\]
The original continuous endpoint values are used.
In particular \(J(1-x)=-J(x)\), \(J(1/2)=0\),
\(0\le L(x)<1/6\), and \(J(x)\ge0\) on \([1/2,1]\).

Here the strict scalar bound is elementary. Since
\(J'(x)=\log(2\sin\pi x)\), the maximum of \(L\) on
\([0,1/2]\) is \(L(1/6)\); reflection gives the same maximum
for \(|J|\) on \([0,1]\). Strict concavity of sine on
\([0,\pi/6]\) gives \(\sin\pi x>3x\) for \(0<x<1/6\).
Thus
\[
\max_{[0,1]}|J|=-J(1/6)
 <-\int_0^{1/6}\log(6x)\,dx=\frac16.
\]
This is the chord argument in
[the complex-index boundary theorem, equation (13)](research_complete_boundary_complex_index.md),
with its strictness made explicit. It also supplies the scalar
bound used in the physical type-three cap extension.

On the lower Newton half, the exact complete-color entropy is
\[
E(u)=-2J(1/2-u)-2J(u).
\]
The original product estimates, together with
\(p_i(r^l)=P_{i+l}/P_l\) on the support, give the double-row rate
\[
\begin{split}
R(u,t,a)={}&-2J(1/2-u)-4J(u)+J(u+t)-3J(t)\\
           &+I_a(t)-2\pi ht,\\
I_a(t)={}&\int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds,
\qquad 0\le t\le1-u .
\end{split}
\tag{4}
\]
This is an upper rate at zeros, not a relative asymptotic there.
The uniform ordinary-color and fixed-derivative estimate for \(e_l\)
is Lemma 1 of the
[upper Newton theorem](research_mixed_terminal_three_high_newton.md).
It applies to all \(l\), including \(l=0\) and odd-level zero rows.
The same theorem proves the uniform finite-product upper estimates
used in (4).

## 2. The entire zero-Newton row

**Lemma 1.** For every target (2) and every \(0\le t\le1\),
\[
R(0,t,a)=-2J(t)+I_a(t)-2\pi ht<\frac{913}{1200}.
\tag{5}
\]

*Proof.* Set \(R_*=\exp(6\pi/25)\) and \(\rho=e^{-2\pi h}\).
Then \(\rho\in[R_*^{-1},R_*]\), and
\[
I_a(t)-2\pi ht
 =\int_0^t\log|\rho-e^{-2\pi i(y+s)}|\,ds .
\tag{6}
\]
For a fixed angle \(\theta\), the squared modulus is a convex
quadratic in \(\rho\). Its maximum on this interval is at an
endpoint. The difference of its endpoint values is
\[
(R_*-R_*^{-1})(R_*+R_*^{-1}-2\cos\theta)>0 .
\]
Consequently
\[
|\rho-e^{-i\theta}|\le|R_*-e^{-i\theta}|
\quad\hbox{throughout the whole radius interval}.
\tag{7}
\]
This uses convexity and the endpoint comparison, not an assertion
that the modulus is increasing at every positive radius.

Put \(c=\log(1+R_*)<57/50\), using the rational scalar bound in
the upper Newton theorem. Thus (6) is at most \(ct\).
For \(0\le t\le3/8\), (3) gives
\[
R(0,t,a)<\frac13+\frac{57}{50}\frac38
                    =\frac{913}{1200}.
\]
For \(3/8\le t\le1/2\), use
\(L(t)=\int_t^{1/2}\log(2\sin\pi s)\,ds
\le(1/2-t)\log2\), with \(\log2<7/10\). Then
\[
R(0,t,a)\le(1-2t)\log2+ct
 <\frac7{10}-\frac{13}{50}t<\frac7{10}.
\tag{8}
\]

Finally \(R_*>2\): \(6\pi/25>18/25>7/10>\log2\).
Therefore the function
\(\log|R_*-e^{-2\pi i(y+s)}|\) is strictly positive at every
real \(s\). Its integral over one full period is \(\log R_*\),
by Jensen's identity. Equations (6)--(7) imply, for \(t\ge1/2\),
\[
I_a(t)-2\pi ht\le \log R_*=\frac{6\pi}{25}
 <\frac{132}{175}<\frac{913}{1200}.
\]
Since \(-2J(t)\le0\) there, this proves (5).
The integrated estimates hold at the possible zeros in (6) by
their continuous limiting values. \(\square\)

## 3. A fixed positive Newton interval

**Lemma 2.** On the complete triangular sector
\(0\le u\le1/200\), \(0\le t\le1-u\), and all targets (2),
\[
                         R(u,t,a)<\frac{1307}{1500}<\frac{109}{125}.
\tag{9}
\]

*Proof.* Since \(J'(x)\le\log2\) on \((0,1)\), with the
integrable endpoints retained,
\[
J(t+u)-J(t)\le u\log2,\qquad
-2J(1/2-u)\le2u\log2.
\]
Subtracting the \(u=0\) expression in (4) gives
\[
R(u,t,a)-R(0,t,a)\le3u\log2-4J(u).
\tag{10}
\]
For \(0\le x\le1/2\), concavity of sine gives
\(\sin\pi x\ge2x\). Hence
\[
-J(u)\le u(1-\log(4u)).
\]
The limiting value at zero is zero. The function
\(u(1-\log(4u))\) is increasing for \(0<u<1/4\), so for
\(u\le1/200\),
\[
-J(u)\le\frac{1+\log50}{200}<\frac1{40}.
\]
Here \(\log50<4\) follows already from
\(\sum_{j=0}^{7}4^j/j!>50\). Thus
\[
3u\log2-4J(u)<\frac{21}{2000}+\frac1{10}
                         =\frac{221}{2000}.
\]
Combining this with (5) proves (9), since
\(913/1200+221/2000=1307/1500\). \(\square\)

**Theorem 3.** There is a fixed ordinary-color disk about \(-2\)
such that, uniformly on (2), the positive double-sum majorant of
\(\mathcal V^{\rm low}_{0,N}\) is at most
\[
                            C N^A e^{879N/1000}.
\tag{11}
\]
Every fixed ordinary-color derivative has the same upper rate on a
smaller fixed disk, for both parities of \(N\). The estimate also
holds after restricting the sector to any subset of its inner indices.

*Proof.* Use the whole-color zero-safe Newton bound and the original
uniform product bounds cited after (4), spending less than \(1/200\)
in total upper-rate tolerance. By (9),
\[
1307/1500+1/200=2629/3000<879/1000.
\]
The factor \(N\) and at most \(N^2\) double summands alter only the
polynomial prefactor. Cauchy's formula on smaller ordinary-color disks
gives each fixed derivative. All denominator factorials have index
less than \(N\), and the exact support wall was kept throughout.
No division by a Newton or numerator-product value is used.
Restriction is valid because (11) bounds the positive majorant.
\(\square\)

## 4. The actual terminal supporting plane and the remaining source

Let \(a_*=A+ic_*\) be an actual external reference of a terminal
type-three block in an open word of length at least two. Let
\(\nu\in\{0,1\}\) be its external type minus three, \(a=y+ic_*\)
with \(y\in[.22,.45]\), \(d=y-A\), and \(\kappa=1/2500000\).
Write \(\mathcal P_0\) for its original optimized terminal action
and put \(\Pi_{0,\nu}=\mathcal P_0-\nu g/2\), with the original
primitive \(g=J+i\pi z(1-z)/2\).

The [terminal end-tail theorem](research_mixed_terminal_transform_tails.md),
equation (24), proves the uniform actual-reference floor
\[
\Re\mathcal P_0(a_*)+\Re\mathcal P_0'(a_*)d-\kappa d^2>89/100.
\tag{12}
\]
Consequently (11) gives, on a sufficiently small fixed color disk,
\[
\begin{split}
&|\partial_w^j\mathcal V^{\rm low}_{0,N}
   (w,e^{-2\pi i(y+ic_*)})|\,
   |d_N(e^{-2\pi i(y+ic_*)})|^{\nu/2}\\
&\quad\le C_jN^{A_j}
 \exp N\left\{\Re\Pi_{0,\nu}(a_*)
       +\Re\Pi_{0,\nu}'(a_*)d-\kappa d^2-\frac1{100}\right\}.
\end{split}
\tag{13}
\]
Indeed the unweighted reserve is greater than \(11/1000\).
For \(\nu=1\), the actual reference height is negative.
The original halfweight then has rate
\(-\Re g(y+ic_*)/2\); convexity of
\(y\mapsto\Re g(y+ic_*)\) bounds its negative by the negative
tangent at \(a_*\). This is exactly the allocation argument of
the end-tail theorem. It retains the actual unselected halfweight
at the new target; no selected-neighbor extension is asserted.

For a disjoint decomposition, first remove the already bounded
terminal end rows, then remove the high and low Newton sectors only
from the remaining middle rows. The high and low estimates bound
positive majorants and therefore permit these restrictions.
The exact remaining type-three source is
\[
\frac1{200}<\frac lN<\frac12,\qquad
\delta<\frac iN<1-\delta,\qquad i+l<N .
\tag{14}
\]
It is kept coherent, with its original \(+i\pi u\) lift, chirp,
ordinary polynomial and all finite factorials. Equation (13) proves
a genuine discarded-sector inequality. It does not establish the
central two-index contour estimate, its nonzero full contribution,
a type-four analogue, or ordinary-knot noncancellation.

