# The first physical node of the next-three sum

Research deduction, 7 November 2026. The term at the first physical
incoming node of the next-three sum has an exponential gap below the
actual geometric action. Its estimate uses the complete boundary
polynomial of the already studied adjacent three-crossing pendant.
An exact identity turns the remaining kernel into the original
reciprocal-factorial interpolation polynomial.

This removes one term of a finite sum. It does not estimate a fixed
interval of physical indices or an arc of a coefficient contour.
No numerical evaluation or certificate replay is used.

## 1. The original term

Put
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad r=q^{-2},\qquad
 P_j=(r;r)_j,\qquad \kappa=q^{D^2/2}.
 \tag{1}
\]
Let \(d_N\) be the polynomial of degree at most \(D\) satisfying
\(d_N(r^j)=P_j^{-1}\). Use the original matrices \(A_n=JM^n\)
and the Newton evaluation column \(v(w)\). The
[exact coefficient identity](research_mixed_next_lowered_word_dual_observation.md),
equations (17)--(18), gives
\[
 F_{34,N}(w,1)=\frac{F_N^{\mathrm{pend}}(w)}{\kappa^2N},
 \qquad
 F_N^{\mathrm{pend}}(w)=v(w)^TA_3^2e_0.
 \tag{2}
\]
Here \(e_0\) on the right denotes the coordinate vector of the
unit. It equals \(v(c_0)\), where \(c_0=q+q^{-1}\).
The polynomial in (2) is exactly the source of
[the adjacent three-crossing boundary theorem](research_three_crossing_full_boundary_asymptotic.md),
not the ordinary \(33\) source evaluated at its complete second color.

For a next three, the complete finite sum is
\[
 \mathcal F_{0,N}(w,Z)
   =\sum_{b=0}^{D}\frac{F_{34,N}(w,r^b)}{P_b}
                         C_{0,N}(r^b,Z),\qquad
 C_{0,N}(X,Z)=\sum_{j=0}^{D}
           \frac{X^{-j}p_j(X)p_j(Z)}{P_j^2},
 \quad p_j(Z)=(rZ;r)_j .
 \tag{3}
\]
The identity combines both original Fourier coefficients before
selecting a physical index.

**Lemma 1.** At every integer level and for every complex \(Z\),
\[
 C_{0,N}(1,Z)=N d_N(Z).
 \tag{4}
\]
Consequently the \(b=0\) term of (3) is exactly
\[
 B_N(w,Z)=\kappa^{-2}F_N^{\mathrm{pend}}(w)d_N(Z).
 \tag{5}
\]

*Proof.* At the ordinary color \(c_0\), every positive-index Newton
polynomial vanishes. Thus the original endpoint polynomial satisfies
\(H_N(c_0,W)=1\), and
\[
 C_{0,N}(1,Z)=\sum_{j=0}^{D}p_j(Z)/P_j=U_{0,N}(c_0,Z).
 \tag{6}
\]
Apply the exact one-letter coefficient identity, Proposition 1 of
the coefficient note, to the cap \(U_0\). It gives
\[
 U_{0,N}(c_0,r^b)=(-q)^b(M^2)_{D,b}.
 \tag{7}
\]
For clarity the entry in (7) can be calculated entirely in the
original full algebra. Write \(Q=q^2\), \(F_j=(Q;Q)_j\),
and \(\nu_j=(-1)^jq^{j(j+1)}\), so \(F_j=\nu_jP_j\).
The [paired crossing formula](research_terminal_powers_qbinomial.md),
Proposition 1, is
\[
 M^2=\kappa^2\Delta B\Delta^{-1},\qquad
 \Delta_{jj}=(-q)^jF_j,\qquad
 B_{jb}=Q^{b(b+1)}\frac{F_j}{F_bF_{j-b}} .
 \tag{8}
\]
Use \(F_D=N\), \(F_{D-b}=N\nu_b/F_b\), and
\(\kappa^2(-q)^D=1\). The last row is
\[
 (M^2)_{D,b}
  =\frac{\kappa^2(-q)^{D-b}N^2Q^{b(b+1)}}
             {F_b^2F_{D-b}}
  =\frac{Nq^{b^2}}{F_b}.
 \tag{9}
\]
Equations (7)--(9) give \(U_{0,N}(c_0,r^b)=N/P_b\).
Both sides of (4) have degree at most \(D\) and agree at
the \(N\) distinct roots, which proves (4). Finally \(P_0=1\)
and (2) prove (5). No repeated-root data in the original
matrices were removed. \(\square\)

## 2. A bound for the actual output coordinates

Write \(Z=e^{-2\pi iz}\), \(z=x+ih\), and retain the original
primitive
\[
 g(z)=J(z)+\frac{i\pi}{2}(z-z^2),\qquad
 J'(z)=\log(2\sin\pi z),\quad J(0)=0 .
 \tag{10}
\]
On every compact set in \(0<\Re z<1\), the complete
[Fourier-weight estimate](research_mixed_fourier_weight_continuation.md),
Section 5, gives, for arbitrary \(\epsilon>0\),
\[
 |d_N(e^{-2\pi iz})|
 \le C_\epsilon N^A
  \exp N\{\max(-\Re g(z),\,2\pi h_+)+\epsilon\}.
 \tag{11}
\]
The second term is the actual polynomial forcing. It is retained
even where the reciprocal-factorial approximation is not relatively
accurate.

**Lemma 2.** On every compact subset of
\[
       \frac14\le x<\frac12,\qquad h\le\frac{17}{250},
 \tag{12}
\]
the rate in (11), before \(\epsilon\), is at most
\(17\pi/125\).

*Proof.* Set \(W=e^{-2\pi iz}\). With the continuation in (10),
\[
 g(z)=\frac{\operatorname{Li}_2(W)-\pi^2/6}{2\pi i}.
 \tag{13}
\]
For \(h\le0\), the convergent dilogarithm series, including its
continuous boundary values, gives
\(\lvert\operatorname{Li}_2(W)\rvert\le\sum_{k\ge1}k^{-2}
=\pi^2/6\). Hence \(-\Re g(z)\le\pi/12\).

For \(h>0\), \(W\) lies below the real axis, and the inversion
identity on this branch is
\[
 \operatorname{Li}_2(W)+\operatorname{Li}_2(W^{-1})
       =-\pi^2/6-\tfrac12\log(-W)^2,\qquad
 \log(-W)=2\pi h+i\pi(1-2x).
 \tag{14}
\]
One can verify the identity by differentiating both sides and
fixing its constant at \(W=-1\); it extends continuously there.
Since \(|W^{-1}|<1\), the same series bound and the imaginary
part of (14) give
\[
 -\Re g(z)\le\frac{\pi}{12}+\pi h(1-2x)
      \le\frac{\pi}{12}+\frac{17\pi}{500}
      =\frac{44\pi}{375}<\frac{17\pi}{125}.
 \tag{15}
\]
Also \(2\pi h_+\le17\pi/125\). This proves the lemma.
\(\square\)

All ordinary next-three outputs lie in the actual enclosure
\[
 O_3\subset[.267,.433]+i[-.065,.068].
 \tag{16}
\]
The [terminal endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
place the private next-three output in
\([.376,.438]+i[-.019,.037]\). Thus both actual reference
families satisfy (12). The ordinary height upper bound here is
\(.068\), not \(.065\).

## 3. The complete boundary term is exponentially smaller

The [whole-period pendant theorem](research_three_crossing_whole_period_source.md)
and its local holomorphic theorem give
\[
 |F_N^{\mathrm{pend}}(w)|\le C N^A e^{NM_{\mathrm{pend}}},
                  \qquad -2\le w\le2,
 \tag{17}
\]
and the same bound with an arbitrarily small rate allowance on
a sufficiently small fixed disk about \(w=-2\). The already saved
action enclosure quoted in
[action calibration, Section 6](research_three_crossing_action_volume_calibration.md)
gives
\[
                  M_{\mathrm{pend}}<77/50.
 \tag{18}
\]
This uses its recorded upper enclosure; no certificate is rerun.

**Theorem 3.** On the actual ordinary and terminal next-three
reference families, for all sufficiently large levels of either
parity,
\[
 |B_N(w,e^{-2\pi iz})|\le C N^A e^{197N/100}.
 \tag{19}
\]
The assertion holds for every real ordinary color \(w\), and on
sufficiently small fixed complex neighborhoods of the complete
ordinary-color reference. Every fixed derivative in the ordinary
color and the outgoing coordinate obeys the same exponent with
a polynomial cost.

*Proof.* From (5), (11), (15), and (17)--(18), the rate before
allowances is less than
\[
 \frac{77}{50}+\frac{17\pi}{125}
 <\frac{77}{50}+\frac{374}{875}
 =\frac{3443}{1750}
 <\frac{197}{100}.
 \tag{20}
\]
The last strict reserve is \(9/3500\). Choose the total color
and interpolation allowances smaller than that reserve. Compactness
and continuity preserve a strict reserve on slightly larger fixed
output neighborhoods. Cauchy's formula there proves the output
derivative assertion. For real ordinary colors, the polynomial
degree is at most \(N-1\), so Markov's inequality applied to
the uniform bound (17) costs only a polynomial for each fixed
derivative. On complex ordinary-color disks use Cauchy's formula.
All identities and estimates used above hold at both parities.
\(\square\)

The actual conditional action is the one in
[the local next-source theorem](research_mixed_three_four_next_local_source.md).
The [typed action floors](research_mixed_three_four_next_binomial_end_bound.md),
Section 5, give
\[
 \Re\mathcal P_0^+(-2,z)>2
       \quad\hbox{for an ordinary next three},\qquad
 \Re\mathcal P_0^+(-2,z)>52/25
       \quad\hbox{for a terminal next three}.
 \tag{21}
\]
After shrinking their complex neighborhoods, their real parts
remain greater than \(199/100\). Therefore (19) implies, for
every fixed jet on smaller neighborhoods,
\[
 e^{-N\mathcal P_0^+(w,z)}B_N(w,e^{-2\pi iz})
                         =O(e^{-N/100}).
 \tag{22}
\]
This is an upper bound on an unwanted term, not a lower bound
on the remaining finite sum.

## 4. Relation to the previous physical truncations

The [sectorwise first-end theorem](research_mixed_three_four_next_sectorwise_first_end.md)
already removes \(a\ge\lceil23N/24\rceil\), with a positive
bound on the full corresponding rectangle. The binomial second-end
theorem removes \(b\ge\lceil11N/12\rceil\). Its second deletion
uses the combined finite sum, as does the present theorem.

For a next three, (19) also permits removing the \(b=0\) row
from the remaining physical rectangle. Indeed its difference from
the full \(b=0\) row is part of the previously bounded first-end
rectangle. Its positive bound has rate \(11/6<197/100\).
The remaining physical indices can therefore be taken to be
\[
 0\le a<\lceil23N/24\rceil,\qquad
              1\le b<\lceil11N/12\rceil ,
 \tag{23}
\]
with an error exponentially smaller than the geometric local
contribution.

Neither (19) nor (23) removes a contour interval. Establishing
the same gap for \(1\le b\le\delta N\), with a fixed positive
\(\delta\), would require a uniform estimate for the low Newton
coefficients of the ordinary \(33\) polynomial. Their value at
the single node \(c_0\) does not imply that estimate. The other
parts of the complete next-three sum, and the next-four sum,
still require their own comparisons.
