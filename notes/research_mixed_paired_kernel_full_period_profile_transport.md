# A coherent full-period rate for the original paired kernel

Research deduction, 7 November 2026. The completed three-four
kernel has a fixed contour decomposition whose output and input
dependence consists of two explicit cardinal incidences. Keeping
the already proved losses in that decomposition gives a uniform
two-wire rate for the **whole original kernel**. It supplies a
coherent alternative to the raw physical-row rate in the exterior
Schur comparison. It does not prove that comparison or invariance
of a boundary-function class.

## 1. Exact source and the permitted parameter tube

Write
\[
 K_N(\zeta,\omega)=
 h_N(x_0+\zeta)^TA_{3,N}A_{4,N}h_N(x_0+\omega),\qquad
 K=e^{2\pi ix_0},\quad \rho=|K|.
 \tag{1}
\]
The [completed kernel theorem](research_mixed_contracted_pair_full_kernel.md)
uses the literal source
\[
 \kappa_N^3Nc_xc_y
 \sum_{\substack{i,j,k,l\ge0\\i+j<N,\ j+k<N,\ k+l<N}}
 \frac{X^iY^lQ_N^{jk}P_{i+j}P_{j+k}P_{k+l}}
 {P_j^2P_k^3P_l(X;r)_{i+1}(Y;r)_{l+1}},
 \tag{2}
\]
where \(x=x_0+\zeta,\ y=x_0+\omega\),
\(X=e^{2\pi ix},Y=e^{2\pi iy}\), and all scalars are
exactly those in the [contracted-source theorem](research_mixed_contracted_pair_rectangle.md).
In particular the shared wire has already been contracted before
any modulus. The closed physical support is
\[
 \Omega=\{s,t,p,q\ge0:s+t\le1,\ t+p\le1,\ p+q\le1\}.
 \tag{3}
\]

Keep the enlarged central box and original heights:
\[
 \begin{split}
 C&=[1/4,1/2]\times[1/5,9/20]\times[1/5,21/50]^2,\\
 H_s=H_t&=[-3/100,3/200],\\
 H_p=H_q&=[-11/200,3/200],\\
 z_*&=(z_3,z_3,z_4,z_4),\qquad h=\Im z_*.
 \end{split}                                                    \tag{4}
\]
These are fixed original coordinates; they are not recomputed
as the external parameters move. Put
\[
 F(z)=\mathcal F(z;x_0,x_0),\qquad
 M_{34}=\Re F(z_*),\qquad u_*=\Re z_*.
 \tag{5}
\]
The [enlarged-rectangle proof](research_mixed_contracted_pair_enlarged_rectangle.md)
supplies a fixed \(\mu>0\) with
\(-\Re F''\succeq\mu I_4\) on the entire height product.

For an external shift \(v\), use the exact lifted incidence
\[
 \begin{split}
 \ell_a(x)&=2\pi ix(a-1/2)
  -\frac{\operatorname{Li}_2(e^{2\pi ix}e^{-2\pi ia})
                     -\operatorname{Li}_2(e^{2\pi ix})}{2\pi i},\\
 \Delta_v(a)&=\Re\{\ell_a(x_0+v)-\ell_a(x_0)\}.
 \end{split}                                                    \tag{6}
\]
The linear term uses \(x_0+v\) itself, not a principal
\(\log(e^{2\pi i(x_0+v)})\). Choose once and for all
\(\sigma>0\) so small that
\[
 \sigma<\Im x_0/2,\qquad
                  \rho e^{2\pi\sigma+.03\pi}<.7 .
 \tag{7}
\]
Such a choice exists by the original strict modulus bound.
For
\[
 \mathcal T_\sigma=\{v:|\Re v|\le3/4,\ |\Im v|\le\sigma\},
 \tag{8}
\]
every external denominator argument for (4) has modulus less
than \(.7\), uniformly in both parameters. On the real physical
support its modulus is at most \(\rho e^{2\pi\sigma}<1\).
The two dilogarithms in (6) therefore stay in fixed compact
subsets of their unit disks. The original factorial strips
are unchanged.

In the exact phase, all external dependence is
\(\ell_s(x)+\ell_q(y)\). Hence every fixed source profile
changes by exactly
\[
                        \Delta_\zeta(s)+\Delta_\omega(q).
 \tag{9}
\]
The cardinal factors, including \(1-X^N,1-Y^N\), are kept.
Their remaining symbols are uniformly bounded on (8); the
linear exponential in (6) is not hidden in those symbols.

## 2. The fixed coherent profile family

Use the exact identity
\[
                 K_N=\mathcal P_N+\mathcal M_N
                                      -\mathcal J_N+\mathcal A_N
 \tag{10}
\]
of [simultaneous contour transport](research_mixed_contracted_pair_simultaneous_contour.md),
on the enlarged box (4). Define the following compact source
domains \(D_\alpha\) and original real profiles \(P_\alpha\),
retaining their first and last coordinates \(s_\alpha,q_\alpha\).

* The main sheet has \(u\in C\),
  \(P_{\rm m}(u)=\Re F(u+ih)\), and
  \((s_{\rm m},q_{\rm m})=(u_s+ih_s,u_q+ih_q)\). Thus
  \[
  P_{\rm m}(u)\le M_{34}-\frac{\mu}{2}\|u-u_*\|^2,
                     \qquad P_{\rm m}(u_*)=M_{34}.               \tag{11}
  \]
* The physical complement has \(u\in
  \Omega\setminus\operatorname{int}C\), with profile
  \(P_{\rm ph}(u)=E(u;K,K)\) of equation (14) in the
  contracted-source theorem, and physical \(s,q\in[0,1]\).
  The already certified complete complement gives
  \[
  P_{\rm ph}\le M_{34}-\delta_P,\qquad
                              \delta_P=19/3750.                 \tag{12}
  \]
  Every original support wall and coordinate end is retained.
  Prohibited sum-\(N\) rows are zero; their continuous upper
  rate remains valid.
* For each of the \(4^4-1=255\) nonmain products of
  \(I,A^-,A^+,V\), use its original domain \(u+iv\).
  An \(I\) coordinate has height zero, \(A^\pm\) has the
  corresponding fixed height in (4), and \(V\) has real part
  at either endpoint with its full height interval. Splitting
  the two \(V\) sides gives the original 624 domains. The profile is
  \[
     P_{\rm a}(u,v)=\Re F(u+iv)-2\pi\sum_j|v_j|.                 \tag{13}
  \]
  Its first and last coordinates are those of \(u+iv\).
  The original vertical subtraction and every finite horizontal
  denominator are still present. At the original parameters the
  established height-reset proof gives loss at least \(\delta_P\)
  when \(V\) occurs, and at least \(\delta_A=1/20\) for the
  80 purely horizontal products.
* For each of the eight common-height joining faces take
  \(u\in\partial C\) on that face, \(0\le a\le1\), and
  \[
                    P_{\rm j}(u,a)=\Re F(u+iah).                \tag{14}
  \]
  There is no alias penalty. Put
  \(d=\operatorname{dist}(u_*,\partial C)>0\). The original
  simultaneous convexity proof gives loss at least
  \[
                    \delta_J=\min(\delta_P,\mu d^2/2)>0.         \tag{15}
  \]
  All four heights use the same multiplier \(a\).

These profiles bound the fixed components of (10) before an
external shift. We do not repeat the old clips or height resets
after the shift, when their derivative signs might change.
Instead the original \(s_\alpha,q_\alpha\), including their
heights and joint support restrictions, are kept in (9).

## 3. The resulting whole-kernel rate

Define
\[
 \mathcal B_{\rm coh}(\zeta,\omega)=
 \max_\alpha\ \max_{\xi\in D_\alpha}
 \{P_\alpha(\xi)+\Delta_\zeta(s_\alpha(\xi))
                            +\Delta_\omega(q_\alpha(\xi))\}.
 \tag{16}
\]
This is a continuous real function on
\(\mathcal T_\sigma^2\), specified entirely by original
source functions and fixed compact domains. No new maximum or
function value is evaluated here.

**Theorem 1.** There exist fixed \(C_0,A,N_0\) such that
\[
       |K_N(\zeta,\omega)|
          \le C_0N^A e^{N\mathcal B_{\rm coh}(\zeta,\omega)}
       \quad(\zeta,\omega\in\mathcal T_\sigma,\ N\ge N_0).
 \tag{17}
\]
Every fixed external derivative obeys the same rate with a
possibly larger power of \(N\).

*Proof.* The exact decomposition (10) is valid throughout
(8), since (7) preserves its denominator and interpolation
domains. The original regular-row estimates have uniform
symbols and polynomial prefactors there. The supported
physical rows have the zero-safe factorial upper bound with
\(O(\log N)\) errors, uniformly up to all of (3). Their
outgoing products are uniformly regular by (7). Thus, unlike
an arbitrary-tolerance cap envelope, this factorial source
requires only a fixed polynomial loss.

Each summand or current in (10) has exactly its original
profile plus (9). The number of physical rows is polynomial,
and the number of contour pieces is fixed. Half-grid shifts
inside the regular strips cost bounded factors. The exact
horizontal denominators are bounded away from zero and the
vertical kernels have their original exponential penalties.
These facts and (16) prove (17). Fixed derivatives of the
regular external factors cost only powers of \(N\), uniformly
on a slightly smaller parameter tube. Alternatively first
choose a slightly larger tube in (7) and apply Cauchy's
formula on disks of radius proportional to \(N^{-1}\);
the profiles have uniformly bounded external derivatives.
Both level parities are included. \(\square\)

For an equivalent two-index description retain the joint deficit
\[
 D_\alpha(a,b)=M_{34}-
 \max_{\substack{\xi\in D_\alpha\\
                  s_\alpha(\xi)=a,\ q_\alpha(\xi)=b}}P_\alpha(\xi),
 \tag{18}
\]
with value \(+\infty\) off its image. Then
\[
 \mathcal B_{\rm coh}(\zeta,\omega)=M_{34}+
 \max_\alpha\sup_{a,b}
 \{\Delta_\zeta(a)+\Delta_\omega(b)-D_\alpha(a,b)\}.               \tag{19}
\]
No independent enlargement of the two boundary indices is
implicit in (18). In particular
\[
 D_{\rm m}(a,b)\ge\frac{\mu}{2}
 \{(\Re a-\Re z_3)^2+(\Re b-\Re z_4)^2\},                        \tag{20}
\]
on its two original critical-height intervals. Every other
deficit has its positive floor from (12)--(15).

At the reference all these gaps are retained:
\[
                        \mathcal B_{\rm coh}(0,0)=M_{34}.
 \tag{21}
\]
The unique interior main maximizer and its negative Hessian
give, by the implicit function theorem, a smooth maximizing
point for sufficiently small real \((\zeta,\omega)\). The
other profiles remain separated by their positive gaps.
Consequently the two real first derivatives of (16) at zero
equal
\[
             \Re\Phi_{34,x}(x_0,x_0),\qquad
             \Re\Phi_{34,y}(x_0,x_0),                            \tag{22}
\]
with their original momenta and action constants.

## 4. Period matching and the local coherent replacement

The kernel changes by \((-1)^{N-1}\) if either external
coordinate is shifted by one. The individual complex-height
profiles do not: for an integer \(n\),
\[
                    \Delta_{v+n}(a)=\Delta_v(a)-2\pi n\Im a.
 \tag{23}
\]
To obtain matching period ends, let
\(\chi(u)=(3/4-|u|)_+\) and use the normalized weights
\[
 a_n(v)=\frac{\chi(\Re v+n)}
                    {\sum_j\chi(\Re v+j)}.
 \tag{24}
\]
Define
\[
 \mathcal B_{\rm per}(\zeta,\omega)=
  \sum_{n,m}a_n(\zeta)a_m(\omega)
                  \mathcal B_{\rm coh}(\zeta+n,\omega+m).
 \tag{25}
\]
Only at most four positive-weight terms occur. All lie in
(8) when \(|\Im\zeta|,|\Im\omega|\le\sigma\).
Take the geometric mean of the corresponding common-prefactor
bounds (17). Exact parity makes their moduli equal, and the
weights sum to one. Thus (17) holds with \(\mathcal B_{\rm per}\)
on the two full periods and their indicated complex tubes.
This rate is continuous and periodic in both real coordinates,
and agrees with (16) when
\(|\Re\zeta|,|\Re\omega|\le1/4\).

On the proved local kernel bidisk, the nonzero asymptotic and
(17) imply
\[
 \Re\Phi_{34}(x_0+\zeta,x_0+\omega)
                            \le\mathcal B_{\rm per}(\zeta,\omega).
 \tag{26}
\]
One may therefore replace \(\mathcal B_{\rm per}\) locally
by the actual phase. More precisely, choose a continuous cutoff
\(0\le b\le1\), supported in that local bidisk and equal to
one on a smaller bidisk. Extend it periodically in both real
coordinates, using the corresponding local representatives for
the phase on its support, and put
\[
 \mathcal B_*=
 b\,\Re\Phi_{34}(x_0+\zeta,x_0+\omega)
                            +(1-b)\mathcal B_{\rm per}.          \tag{27}
\]
The local complete-kernel bound and (26) prove (17) also with
\(\mathcal B_*\), after adjusting the common polynomial.
Where \(b=1\), the sharper original prefactor \(N^{-1/2}\)
and nonzero packet remain available. This patch concerns the
whole kernel, not just its selected Gaussian current.

The raw all-physical-row bound \(B_{\rm phys}\) remains another
valid bound on the same tube. Taking
\(\min(\mathcal B_*,B_{\rm phys})\) is consequently allowed,
with common prefactors. The improvement is substantive already
at the reference: (21) gives \(M_{34}\), whereas the
[saved raw-diagonal obstruction](research_mixed_paired_schur_raw_diagonal_obstruction.md)
proves \(B_{\rm phys}(0,0)>M_{34}+263/25000\).
The high raw physical trials have not been declared small;
they are included coherently in the translated central source.

## 5. The remaining attachment comparison is still explicit

The rates (19), (25), (27) can replace a raw physical rate
wherever the [whole-message Schur criterion](research_mixed_paired_whole_message_schur_criterion.md)
asks for a containing bound for the original paired kernel.
They cover the entire real input/output periods, their local
complex connecting pieces, all original support faces, and every
contour correction. They are not a bound for a different
conditional representation under an unestimated change of basis.

For example the exterior inequality still to be established,
on its specified noncentral contours, is
\[
 W_h(\zeta)+\mathcal B_*(\zeta,\omega)
       \le\Re C(h)+W_{h^+}(\omega)-\delta,\qquad \delta>0,
 \tag{28}
\]
or a sharper inequality using the minimum with \(B_{\rm phys}\).
The first term may now use the actual prepared message's
[full-period profile envelope](research_mixed_prepared_cap_full_period_profile_transport.md),
subject also to the separate phase-class hypothesis. None of
(16)--(27) asserts (28). The transported joint deficits give
concrete source data for that comparison, replacing the
previously available raw-rate-only exterior choice. They do not
establish arbitrary-message stability, a nonzero closing
functional, or a mixed-word finite-exception theorem.
