# The complete adjacent kernel with two independent Fourier parameters

Research deduction, 7 November 2026. The complete adjacent power-two
kernel has a nonzero joint asymptotic on a complex neighborhood of
its two original Fourier parameters. The two parameters vary
independently. This conclusion uses an actual deformation of the
finite inner sum and the exact outer contours; it is not an
extension inferred from values on the diagonal.

The theorem estimates the original Fourier kernel and its normalized
Fourier derivatives. A prescribed ordinary closing or normal adapter
must still be expressed in terms of this kernel before the estimate
can be used for that observation. No numerical evaluation is used.

## 1. Statement and original normalization

Let
\[
 V_N(x,y)=h(x)^T A_2^2h(y)
 \tag{1}
\]
be the exact original kernel of
[the merged-source theorem](research_mixed_two_adjacent_merged_source.md).
Its exact finite formula is
\[
 V_N(x,y)=e^{\pi i(N-1)(x+y)}
   \sum_{m=0}^{N-1}P_m\sum_{j=0}^m
      \frac{r^{-j(m-j)}p_j(e^{-2\pi ix})
                         p_{m-j}(e^{-2\pi iy})}
                         {P_j^2P_{m-j}^2},
 \quad r=e^{-2\pi i/N}.
 \tag{2}
\]
As usual \(P_j=(r;r)_j\) and \(p_j(X)=(rX;r)_j\).
There are no additional outside powers of \(N\) or \(\kappa\).

Let \(F(a,s;x,y)\) and \(b(a,s;x,y)\) be the original
two-variable phase and symbol of that exact source:
\[
\begin{split}
 F(a,s;x,y)={}&g(a+s)+g(a+x)+g(s+y)
       -2g(a)-2g(s)-g(x)-g(y)+2\pi ias,\\
 b(a,s;x,y)={}&
 \frac{\mathfrak a(a+s)\mathfrak a(a+x)\mathfrak a(s+y)}
 {\mathfrak a(a)^2\mathfrak a(s)^2\mathfrak a(x)\mathfrak a(y)}.
\end{split}
 \tag{3}
\]
The nondegenerate critical point at \(x=y=x_0\) is
\((a_*,a_*)\). On a sufficiently small bidisk about
\((x_0,x_0)\), denote its original holomorphic continuation by
\[
 (a_\#(x,y),s_\#(x,y)),\qquad F_a=F_s=0.
\]
The implicit branch is the one proved in
[the critical-corridor theorem](research_mixed_two_adjacent_critical_corridor.md).
Define
\[
\begin{split}
 \mathcal S(x,y)
  &=F(a_\#,s_\#;x,y)+\pi i(x+y),\\
 \mathcal C(x,y)
  &=\frac{2\pi e^{-\pi i(x+y)}b(a_\#,s_\#;x,y)}
            {\sqrt{\det[-F''(a_\#,s_\#;x,y)]}} .
\end{split}
 \tag{4}
\]
The square root is continued from the original accretive
Gaussian at \((x_0,x_0)\); it is not chosen afresh pointwise.

**Theorem 1.** There is a fixed open bidisk \(U\) about
\((x_0,x_0)\) on which \(\mathcal C\) is holomorphic and nonzero,
and on every smaller closed bidisk,
\[
 \boxed{\quad
 V_N(x,y)=N^{-1/2}\mathcal C(x,y)e^{N\mathcal S(x,y)}
                         (1+\mathcal R_N(x,y)),\qquad
 \mathcal R_N=O(N^{-1}).
 \quad}
 \tag{5}
\]
Both level parities are included. Every fixed mixed derivative
\(\partial_x^p\partial_y^q\mathcal R_N\) is \(O(N^{-1})\)
on a smaller bidisk. These are derivatives of the actual
original kernel (2), after the displayed normalization.

## 2. The original discarded rows remain smaller

Keep the same fixed physical regions and the same number
\(R<1\) as in
[the complete diagonal outer assembly](research_mixed_two_adjacent_outer_total_assembly.md).
The discarded regions are:
\[
 c=m/N\le1/2,\qquad
 c>1/2,\ |j-m/2|>N/5,\qquad
 c>R.
 \tag{6}
\]
At the original equal parameters their absolute contributions
have fixed strict gaps below
\(\Re\mathcal S(x_0,x_0)\). The estimates are for the
original physical terms, including every endpoint, as
proved in
[the global truncation theorem](research_mixed_two_adjacent_global_central_truncation.md)
and the original diagonal-side theorem.

These gaps persist for independent nearby \(x,y\).
To justify this uniformly in the physical indices, set
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 L_z(t)=\int_0^t\log|1-e^{-2\pi i(z+u)}|\,du.
\]
On the closed physical triangle \(a,s\ge0,\ a+s\le1\),
the full original row, including the outside factor, has
continuous real rate
\[
 \mathcal E_{x,y}(a,s)
 =J(a+s)-2J(a)-2J(s)+L_x(a)+L_y(s)
                         -\pi\Im(x+y).
 \tag{7}
\]
The logarithmic error in its physical factorial estimate is
\(O(\log N)\), uniformly on that whole triangle and on a
small parameter bidisk with \(\Im x,\Im y>0\).
The endpoint estimates for \(P_j\) give this statement also
near zero and the support edge. The two external products
have no zeros there and have uniform smooth logarithms.

Each closed discarded region has a strict rate gap at
\((x_0,x_0)\); the strict cutoff margins in the cited
proofs include its boundary. Uniform continuity of (7),
and continuity of \(\Re\mathcal S(x,y)\), preserve a
common positive gap after the bidisk is decreased.
This uses no perturbed unimodality assertion. Summing
at most \(N^2\) rows absorbs only polynomial factors.

Consequently, with the same integer cut sets
\(L_N=\lfloor N/2\rfloor+1\), \(M_N=\lfloor NR\rfloor\),
\[
\begin{split}
 V_N(x,y)={}&e^{\pi i(N-1)(x+y)}
  \sum_{\sigma=0,1/2}
   \sum_{\substack{L_N\le m\le M_N\\m/2\equiv\sigma\ ({\rm mod}\ 1)}}
            \mathcal H_{\sigma,N}(m/N;x,y)\\
 &+O\!\left(N^b e^{N(\Re\mathcal S(x,y)-\delta_0)}\right)
\end{split}
 \tag{8}
\]
uniformly, for some \(\delta_0>0\). Here
\[
 \mathcal H_{\sigma,N}(c;x,y)
  =\sum_{\substack{d\in\mathbb Z+\sigma\\|d|\le N/5}}
                  T_N(c/2+d/N;c,x,y)
 \tag{9}
\]
is the original central finite source with its independent
parameters and its unchanged factorial row.

## 3. The complete inner packet on the needed outer compact set

[The independent inner theorem](research_mixed_two_adjacent_independent_inner_packet.md)
gives, on every fixed bounded total-height compact needed
below, a common parameter neighborhood on which
\[
 \mathcal H_{\sigma,N}(c;x,y)
    =N^{-1}\mathcal A(c,x,y)e^{N\Phi(c,x,y)}
                               (1+O(N^{-1})).
 \tag{10}
\]
All fixed normalized derivatives are uniform there.
The two parity sources have the same coefficient and phase.

In that theorem \(t=a-c/2\), and the small actual inner
critical point is \(t=\zeta(c,x,y)\). In particular
\[
 \Phi(c,x,y)=F(c/2+\zeta,c/2-\zeta;x,y).
 \tag{11}
\]
The proof of (10) retained its exact finite parity contour,
both horizontal lattice corrections, both side currents,
the complementary inner rows, and the connectors to the
moved inner critical point. Thus (10) is valid on the
complex outer contour itself, before the outer sum is
estimated.

The outer critical point of (11) is
\[
       c_\#(x,y)=a_\#(x,y)+s_\#(x,y).
 \tag{12}
\]
Indeed the inner critical equation fixes the difference
coordinate, and the derivative of (11) is the remaining
critical equation. Local uniqueness identifies this point
with the branch continuing \(c_*=2a_*\).
At the center, its outer Hessian has negative real part.
It remains nonzero with negative real part on a small
parameter bidisk.

## 4. Exact outer contours and uniform infinite tails

Use the same full-grid midpoint cuts \(\ell_N,u_N\),
parity kernels \(k_{\sigma,N}\), and fixed contour height
\(H_*=\Im c_*\) as in the diagonal assembly. Their domains
do not change: for \(1/2\le\Re c\le R+o(1)<1\) and
\(|d/N|\le1/5\), all central factorial arguments stay
in fixed regular real strips, at every imaginary height,
for nearby independent \(x,y\).

The exact residue density is still \(N/2\), and the
complete formula (25) of the diagonal assembly therefore
holds with \(\mathcal H_{\sigma,N}(c;x,y)\) in place of
its diagonal specialization. No pole is crossed on a
lower outer deformation.

For clarity the exact moving upper factorial polynomial,
including the chirp and the finite linear correction,
is now
\[
 \pi i\left\{
 N[x+y-x^2-y^2-c(x+y)]-2d(x-y)-x-y
 \right\}.
 \tag{13}
\]
The additional \(d\)-dependent factor is bounded by
\(e^{C N}\) uniformly for \(|d|\le N/5\) and for the
chosen parameter bidisk. It is independent of the
outer height. Thus the upper parity alias has the
strict slope
\[
                   \pi N(1-\Re x-\Re y)>0.
 \tag{14}
\]
At negative infinite total height the moving factorials
have their original lower constants and the only
height-dependent polynomial is
\[
                  \pi iNc^2/2-2\pi id^2/N.
 \tag{15}
\]
The lower alias slope is therefore unchanged:
\(\pi N(1-\Re c)>0\).
The fixed external factors \(E_N(x)E_N(y)\) have their
uniform compact estimates.

The exact seven-moving-factor remainder estimate of the
diagonal proof is uniform on a fixed parameter bidisk:
\[
                C N(1+T)e^{-\pi T+C},\qquad T=|\Im c|.
 \tag{16}
\]
Equations (13)--(16) prove both fixed-level alias removal
and a uniform remote side bound
\[
       C N^b e^{N(C_0-\lambda T)}
 \tag{17}
\]
for some \(\lambda>0\), after enlarging a fixed tail cut.
This follows from the original factorial tails, rather
than applying (10) on an unbounded parameter set.

Choose a fixed height cut \(T_0\) so that (17), including
the outside factor, is below the original critical rate
by a fixed margin at the diagonal parameters.
Uniformity and continuity allow the same cut and a
smaller fixed margin on the parameter bidisk.

On the remaining bounded side intervals, the diagonal
assembly has a strict rate gap for both entire weighted
side integrands, including the unpenalized intervals
between heights zero and \(H_*\).
Use (10) on an open neighborhood of this whole compact
set. The modulus of each exact parity weight is unchanged.
Continuity of \(\Re\Phi(c,x,y)\), of the outside rate,
and of \(\Re\mathcal S(x,y)\) preserves that strict gap
on all these intervals at once. This is a compact
perturbation of a proved strict comparison; no global
convexity claim for the perturbed phase is required.

Both complete outer side integrals are consequently
exponentially smaller than \(e^{N\Re\mathcal S(x,y)}\),
uniformly on the parameter bidisk.

## 5. The moved principal contour and its coefficient

It remains to estimate the unweighted principal integral
of each parity. Its original path has fixed height \(H_*\).
Translate that finite path by
\[
                \Delta(x,y)=c_\#(x,y)-c_*.
\]
Its two connector segments remain in small neighborhoods
of the original top endpoints, which have a fixed phase
gap. This follows by decreasing the parameter bidisk and
using the compact version of (10). Cauchy's theorem
therefore moves the main path through \(c_\#(x,y)\),
with both connectors retained as exponentially smaller
terms.

On the translated horizontal path the real phase has
its unique nondegenerate maximum at \(c_\#\). Near that
point this follows from the negative real outer Hessian;
on the rest of the compact path it follows from the
original strict gap and continuity.
The original Gaussian evaluation gives, for each parity,
\[
 \frac N2\int \mathcal H_{\sigma,N}(c;x,y)\,dc
  =N^{-1/2}
     \frac{\sqrt{2\pi}\mathcal A(c_\#,x,y)}
                    {2\sqrt{-\Phi_{cc}(c_\#,x,y)}}
        e^{N\Phi(c_\#,x,y)}(1+O(N^{-1})).
 \tag{18}
\]
The normalized error of (10) is estimated on this
actual moved contour, so it does not pass through
unknown cancellation on real physical samples.
The parity coefficients and orientations are identical;
the leading terms add.

In coordinates \(c=a+s,\ t=(a-s)/2\), the inverse linear
coordinate change \(a=c/2+t,\ s=c/2-t\) has determinant \(-1\).
The Hessian determinant identity for eliminating the
inner variable is
\[
 \mathcal F_{tt}\,\Phi_{cc}
       =\det\bigl(\mathcal F''_{(c,t)}\bigr)
       =\det F''_{(a,s)} .
 \tag{19}
\]
Here the outer second derivative is the Schur complement
\(\mathcal F_{cc}-\mathcal F_{ct}^2/\mathcal F_{tt}\),
at the joint critical point. The branches in (19) are
continued from the original diagonal Gaussian, where
their product was already fixed. The nonzero symbol
and Hessians consequently give precisely (4).

Finally restore
\[
 e^{\pi i(N-1)(x+y)}
      =e^{N\pi i(x+y)}e^{-\pi i(x+y)}
\]
and all absolute physical errors in (8).
This proves (5), including its original normalization.
The actual finite kernel (2), its continued action,
and its nonzero coefficient are holomorphic on the
bidisk. Cauchy estimates on nested bidisks give the
claimed fixed mixed derivatives of \(\mathcal R_N\).

The conclusion concerns two independently variable
Fourier boundary states of the original adjacent
operator. It supplies a complete local kernel estimate.
It does not assert that an arbitrary prescribed closing
has nonzero overlap with that kernel, identify ordinary
normal adapters without their exact formulas, or prove
stability under arbitrary short clusters.

