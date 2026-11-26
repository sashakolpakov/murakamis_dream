# Removing a fixed low-index interval from the next attachment

Research theorem, 7 November 2026. For either next letter, three or
four, a fixed positive interval of small physical incoming indices
contributes exponentially less than the actual geometric local
contribution. The prefix is the complete original \(34\) polynomial.
The proof sums that prefix coherently before taking a modulus.

This extends the first-node estimate to \(0\le b\le\delta N\),
with one fixed \(\delta>0\). It applies to the ordinary and terminal
next-reference families, at both level parities. It does not estimate
the remaining middle indices or prove that the geometric term survives
in the complete next sum. No numerical evaluation is used.

## 1. Exact sum and the two estimates being combined

Put \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\),
\(P_b=(r;r)_b\), and \(\kappa=q^{D^2/2}\). Keep the original
complete prefix \(F_{34,N}\), conditional kernel \(C_{\beta,N}\),
and conditional action \(\mathcal P_\beta^+\), \(\beta=0,1\).
The [exact next attachment](research_mixed_three_four_next_local_source.md)
is
\[
 \mathcal F_{\beta,N}(w,Z)
    =\sum_{b=0}^{D}\frac{F_{34,N}(w,r^b)}{P_b}
                            C_{\beta,N}(r^b,Z).
 \tag{1}
\]
It is the sum of the two original Fourier coefficients. This
identity, rather than a separate estimate of either coefficient,
is used throughout.

Let
\[
 \ell_{b,N}(w)=(v(w)^TA_3^2)_b,\qquad A_3=JM^3.
 \tag{2}
\]
The [exact coefficient identity](research_mixed_next_lowered_word_dual_observation.md)
gives, at every physical incoming index,
\[
 \frac{F_{34,N}(w,r^b)}{P_b}
                   =\frac{(-q)^b}{\kappa^2N}\ell_{b,N}(w).
 \tag{3}
\]
In particular there is no remaining small factorial divisor to
estimate on the left.

The [low Newton coefficient theorem](research_three_crossing_low_newton_coefficients.md)
proves, for every sufficiently small fixed \(\delta>0\),
\[
 |\ell_{b,N}(w)|
  \le C_\tau N^{A_\tau}
       e^{N\{M_{\mathrm{pend}}+\epsilon(\delta)+\tau\}},
 \quad 0\le b\le\lfloor\delta N\rfloor,\quad -2\le w\le2,
 \qquad \epsilon(\delta)\longrightarrow0 .
 \tag{4}
\]
Its complex-color version has the same rate with an arbitrarily
small extra allowance on a sufficiently small fixed disk about
\(-2\). Its proof retains the inserted source's coherent outer
sums, its boundary forcing, and every contour current. Equation
(4) is not an inference from the single value \(\ell_{0,N}\).

The [low-index kernel bounds](research_mixed_next_low_index_kernel_margin.md)
give, on the respective actual output families,
\[
 |C_{\beta,N}(r^b,Z)|
  \le C_\tau N^{A_\tau}
           e^{N\{m_\beta+\omega(\delta)+\tau\}},
 \qquad
 m_0=\frac{1271}{2500},\quad m_1=\frac7{15},\quad
 \omega(\delta)=\delta\log2-J(\delta)\longrightarrow0 .
 \tag{5}
\]
This is a positive bound on all conditional rows. Its exact physical
support is used only at the physical incoming argument in (5).
Both (4) and (5) hold for all sufficiently large integer levels
of both parities.

## 2. The geometric reserve

Let
\[
 \chi=\frac{117}{800\pi},\qquad
 L_0=2+\chi,\quad L_1=\frac{207}{100},\qquad
                       \Delta=\frac{59}{440000}.
 \tag{6}
\]
The same kernel-margin note proves, on every actual ordinary or
terminal reference of the given next type,
\[
 \Re\mathcal P_\beta^+(-2,z)>L_\beta,\qquad
             L_\beta-M_{\mathrm{pend}}-m_\beta>\Delta .
 \tag{7}
\]
Here the smaller margin is for an ordinary next three. The action
calculation keeps the original \(-g(y)-\beta g(s)\) terms, and
the coefficient estimate uses the already calibrated pendant
action \(M_{\mathrm{pend}}\). The constants refer to the same
conditional normalization as (1).

Choose once and for all \(0<\delta<1/40\), sufficiently small
that
\[
              \epsilon(\delta)+\omega(\delta)<\Delta/8.
 \tag{8}
\]
Such a choice exists by (4)--(5). Choose the common finite-rate
tolerances and complex-parameter neighborhoods so their additional
cost is less than \(\Delta/8\). Uniform compactness of the actual
reference families permits the same choices throughout them.
On smaller neighborhoods also arrange
\[
                \Re\mathcal P_\beta^+(w,z)>
                                  L_\beta-\Delta/4.
 \tag{9}
\]
The parameters and \(\delta\) are fixed before \(N\) tends to infinity.

**Theorem 1.** With these choices,
\[
 \sum_{b=0}^{\lfloor\delta N\rfloor}
   \left|\frac{F_{34,N}(w,r^b)}{P_b}
                         C_{\beta,N}(r^b,Z)\right|
 \le C N^A
        e^{N\{M_{\mathrm{pend}}+m_\beta+\Delta/4\}}.
 \tag{10}
\]
The estimate holds uniformly for all real ordinary colors and on
the stated complete-color complex neighborhoods, and for both actual
next-reference families. On those complex neighborhoods the right
side is at most
\[
                  C N^A
                  e^{N\{\Re\mathcal P_\beta^+(w,z)-\Delta/2\}}.
 \tag{11}
\]

*Proof.* Substitute (3) into the left side of (10).
The phase \((-q)^b/\kappa^2\) has modulus one. Apply (4)--(5)
to every retained physical index, using (8) and the common
allowances. The number of terms and the scalar \(1/N\) change
only a polynomial prefactor. This gives (10). Equations
(7) and (9) give (11). No sign assumption about either
\(\ell_{b,N}\) or the original prefix sum is made.
\(\square\)

If \(\mathcal B_{\beta,N}\) denotes the signed sum over the
same indices, it is an exact holomorphic function of the outside
parameters. For every fixed mixed derivative on smaller complex
neighborhoods, (11) and Cauchy's formula give
\[
 \partial_w^j\partial_z^k
   \left(e^{-N\mathcal P_\beta^+(w,z)}
            \mathcal B_{\beta,N}(w,e^{-2\pi iz})\right)
                         =O(e^{-N\Delta/4}).
 \tag{12}
\]
The weaker displayed exponent absorbs every polynomial prefactor.
Real ordinary-color derivatives have the corresponding absolute
positive bound: apply Markov to each complete coefficient polynomial
in (4) before summing. Fixed output derivatives follow by Cauchy
on the output neighborhoods in (5).

## 3. Combining the low interval with the existing high-index deletions

The [first-coordinate theorem](research_mixed_three_four_next_sectorwise_first_end.md)
removes \(a\ge A_N:=\lceil23N/24\rceil\) separately in each
Fourier coefficient. Its additional positive bound controls
the entire physical rectangle with these first indices.
The [binomial end theorem](research_mixed_three_four_next_binomial_end_bound.md)
removes \(b\ge B_N:=\lceil11N/12\rceil\) after summing over
the first index. Their complete overlap is already paid.

For completeness, write the original double finite sum as
\[
 \mathcal F_{\beta,N}(w,Z)
  =\sum_{a,b=0}^{D}
   \frac{U_{0,N}(w,r^a)\,
       C_{1,N}(r^a,r^b)\,C_{\beta,N}(r^b,Z)}{P_b}.
 \tag{13}
\]
The low-\(b\) theorem first sums all \(a\) in (13), giving
the full \(F_{34,N}(w,r^b)\) in (10). If instead only
\(a<A_N\) are kept, the difference is a subset of the
positive first-end rectangle. Its already proved rate is
\(11/6\), smaller than \(L_\beta\) by a fixed amount.
Thus the low-\(b\) deletion is valid after the first-coordinate
deletion as well. This accounts for its overlap without
assigning an absolute bound to the inner prefix terms.

Consequently the remaining physical rectangle is
\[
 \boxed{\qquad
     0\le a<\lceil23N/24\rceil,\qquad
       \lfloor\delta N\rfloor<b<\lceil11N/12\rceil .
 \qquad}
 \tag{14}
\]
The difference from the original full next sum is exponentially
smaller than the established local geometric contribution, with
fixed normalized jets and both parities. All scalar conventions
remain those of (1) and (13).

## 4. The filtered polynomial retains the local geometric contribution

For a subset \(I\subset\{0,\ldots,D\}\), define the original
cardinal projection on degree-\(D\) polynomials by
\[
 \Pi_I F(Y)=\sum_{b\in I}F(r^b)\mathfrak l_b(Y),\qquad
 \mathfrak l_b(Y)=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu .
 \tag{15}
\]
Thus \(|\mathfrak l_b(Y)|\le1\) on the closed unit disk.
Let \(I_{\rm low}=\{b\le\lfloor\delta N\rfloor\}\),
\(I_{\rm high}=\{b\ge B_N\}\), and \(\Pi=\Pi_{I_{\rm low}\cup I_{\rm high}}\).
Write \(R_N^a\) for the first-coordinate polynomial removed in
the sectorwise theorem, so \(F_{34,N}^{<}=F_{34,N}-R_N^a\).
The exact polynomial representing the middle rectangle is
\[
                 F_N^{\rm mid}=(I-\Pi)F_{34,N}^{<}.
 \tag{16}
\]
At its physical nodes it agrees with \(F_{34,N}^{<}\) in the
middle and is zero at both removed ends. Consequently applying
the complete next transfer to (16) gives precisely (14).

There is a stronger local stability statement than the bound
on the transferred error alone:
\[
 \sup_{|Y|\le1}
      |F_{34,N}(w,Y)-F_N^{\rm mid}(w,Y)|
                              \le C N^A e^{8N/5}.
 \tag{17}
\]
This holds for all real ordinary colors and on a sufficiently
small fixed complex disk about \(-2\).

To prove it, for a low node note that \(S_b\le1\) when
\(b\le\delta N\), since \(\delta<1/6\). Equation (3) and
the coefficient estimate give
\[
 |F_{34,N}(w,r^b)|
       \le C_\tau N^{A_\tau}
              e^{N\{M_{\rm pend}+\epsilon(\delta)+\tau\}}.
 \tag{18}
\]
This rate is less than \(8/5\) for the small \(\delta\) already
chosen, with room for the color tolerance.
For a high node the binomial end theorem, equation (10), bounds
the prefix alone at rate
\[
 \frac{433}{500}+\rho(v)-2J(v)+v\log2,\qquad
       0\le v=1-b/N\le1/12,\quad
 \rho(v)=(1+v)\log(1+v)-v\log v .
 \tag{19}
\]
Its elementary inequalities (12)--(14) bound (19) by
\[
 \frac{433}{500}+\frac{85}{288}
                         +\frac{17}{60}+\frac7{120}<\frac85 .
 \tag{20}
\]
These are bounds for the complete prefix at its physical nodes,
at all real colors and on small complete-color disks.
Cardinal interpolation and (18)--(20) therefore bound \(\Pi F_{34,N}\)
on the entire unit disk at rate \(8/5\), with a strict reserve.
The first-coordinate theorem also gives the unit-disk rate
\(371/720\), with arbitrary small tolerance, for \(R_N^a\).
Its projection \(\Pi R_N^a\) has the same rate, since the cardinal
sum costs at most a factor \(N\). The identity
\[
 F_{34,N}-F_N^{\rm mid}=R_N^a+\Pi F_{34,N}-\Pi R_N^a
 \tag{21}
\]
proves (17).

At every actual matching input \(y=q_{34}(s_3)\), the
[complete following-prefix theorem](research_mixed_three_four_following_complete_prefix.md)
has \(|e^{-2\pi iy}|<1\) and
\(\Re\mathcal P_{34}(-2,y)>7/4\). On fixed smaller neighborhoods
retain the unit-disk condition and the weaker floor \(17/10\).
Equation (17) is then exponentially smaller than the original
prefix, including its fixed normalized derivatives. Hence
\[
 F_N^{\rm mid}(w,e^{-2\pi iy})
   =N^{-3/2}\mathcal A_{34}(w,y)e^{N\mathcal P_{34}(w,y)}
                             (1+O_{\rm hol}(N^{-1})).
 \tag{22}
\]
The action and nonzero coefficient are unchanged. Substitution
of (22) into the actual local next integral preserves its
nonzero \(N^{-2-\beta/2}\) leading term. The full
\(d_N C_{\beta,N}\) factors are still present.

## 5. What remains

The theorem removes a fixed interval of physical second indices
for both \(343\) and \(344\). It does not remove the corresponding
real interval from either coefficient contour. The first-coordinate
deletion was proved separately for each Fourier coefficient;
the two second-coordinate deletions concern their combined sum.
The middle part of (14) can still cancel a local contribution.
Controlling that complete signed remainder, and then performing
the prescribed ordinary closure, remains necessary for a new
knot-level theorem.
