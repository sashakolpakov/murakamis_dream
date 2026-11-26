# The actual clock quotient and its canonical affine winding

Private written deduction, 17 November 2026. The singleton compiler of
the original complete signed braid source has an explicit split integral
clock lattice. Its finite fibers are products of intervals with physical
widths, and their exact sums recover the original signed crossing matrices.
The same split identifies the compulsory local Fourier character of the
calibrated physical action. Only after removing that character does the
remaining winding descend to physical-flow coordinates.

This is a fixed-root, complete-color statement, at every level and parity.
It is not a generic-meridian or quantum-normal continuation theorem. It
does not identify the remaining winding lattice with the edge lattice of
an arbitrary geometric triangulation, or select a contributing cycle.

## 1. Actual paths and the finite clock fibers

Fix the original signed braid with \(c\) crossings and \(b\) heads. Set

\[
d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},
\quad \kappa=q^{d^2/2},\quad \eta=q^{-d^2},\quad
S_a=\prod_{t=1}^a2\sin(\pi t/N),\quad S_0=1.
\tag{1}
\]

All signs \(\sigma_j\) are the balanced **physical** signs of the
singleton source [J], not externally reversed diagram conventions.
Use its actual events: one per crossing and all \(b\) closure events.
Its anchor segments contain only under encounters, in their original order.
At crossing \(j\) write \(u_j,v_j\) for its transfer and over-output;
at closure \(i\) write \(a_i\) for its transmitted degree. If \(s\) is
an anchor, its initial degree \(a_s\) is the \(v_j\) or \(a_i\) of its
starting event; its terminal degree \(b_s\) is \(u_j+v_j\) or \(a_i\).
The physical path set \(\mathcal P_d\) is defined by

\[
u_j,v_j\ge0,\quad u_j+v_j\le d,\quad 0\le a_i\le d,
\qquad a_s+\sum_{j\text{ under on }s}u_j=b_s.
\tag{2}
\]

All variables here are integers. The actual under-input is

\[
J_j=a_s+\sum_{\ell\text{ before }j\text{ on }s}u_\ell.
\tag{3}
\]

Thus \(0\le J_j\le J_j+u_j\le d\). These are literal finite
indices: the crossing connects over-input \(u_j+v_j\) and under-input
\(J_j\) to over-output \(v_j\) and under-output \(J_j+u_j\).
No modular replacement of these indices is made.

Let \(C\) be the unsigned event--anchor incidence matrix, retaining
the two parallel middle incidences at each crossing. Its exact source
fiber is \(\mathcal T_d=\{n\ge0:Cn=d\mathbf1\}\). Define

\[
(n_{j0},n_{j1},n_{j2},n_{j3})
 =(d-u_j-v_j,\ u_j-r_j,\ r_j,\ v_j),
\qquad h_j=v_j+r_j,
\tag{4}
\]

and give closure \(i\) the pair \((d-a_i,a_i)\).
Then the projection \(\pi(n)=(u,v,a)\) has exactly the fibers

\[
\boxed{\quad
\mathcal T_d\longleftrightarrow
 \{(p,r):p\in\mathcal P_d,\ r_j\in\{0,\ldots,u_j\}\}.
\quad}
\tag{5}
\]

Indeed the event sums in (4) are \(d\), and the anchor sums are (2).
Conversely \(u=n_1+n_2,v=n_3,r=n_2\) recovers every incidence.
Nonnegativity is precisely (2) and \(0\le r\le u\). The two middle
incidences have the same event and anchor, so their split changes no
endpoint equation. Closure incidences give the displayed \(a_i\).
This proves (5), including zero-width fibers and both parity endpoints.

## 2. The split lattice is integral, including its section

Let \(\Lambda_{\rm inc}=\ker_{\mathbb Z}C\). Let
\(\Lambda_{\rm phys}\) be the integer solutions of the homogeneous
linear path equations (2), without their inequalities. On differences,
the section \(s\) is given crossing by crossing and at closures by

\[
s(\dot u,\dot v,\dot a)_j
 =(-\dot u_j-\dot v_j,\dot u_j,0,\dot v_j),
\qquad s(\dot a)_i=(-\dot a_i,\dot a_i).
\tag{6}
\]

It is the difference of the finite section \(r=0\) in (4). Put
\(k_j=(0,-1,1,0)\) at crossing \(j\), zero elsewhere, and
\(K=\bigoplus_j\mathbb Z k_j\). Then

\[
0\longrightarrow K\longrightarrow\Lambda_{\rm inc}
 \mathop{\longrightarrow}^{\pi}\Lambda_{\rm phys}
 \longrightarrow0,
\qquad
\Lambda_{\rm inc}=K\oplus s\Lambda_{\rm phys}.
\tag{7}
\]

To check the kernel, \(\dot u=\dot v=\dot a=0\) forces each
crossing difference to be \(\dot r_j k_j\). Equation (6) is an
integral right inverse and satisfies all anchor equations. Hence \(K\)
is saturated, with no level-dependent index or division by two.
The dual exact sequence is consequently

\[
0\longrightarrow\Lambda_{\rm phys}^*
 \mathop{\longrightarrow}^{\pi^*}\Lambda_{\rm inc}^*
 \mathop{\longrightarrow}^{\mathrm{res}_K}K^*
 \longrightarrow0.
\tag{8}
\]

Here star means \(\operatorname{Hom}_{\mathbb Z}(-,\mathbb Z)\).
The lattice splitting (7) does not turn the finite fiber (5) into a
fixed box: its widths are the received physical transfers \(u_j\).
At a boundary, some clock directions have no feasible finite move.

## 3. Eliminate the finite fibers before taking a limit

The actual full source of [J, (12)--(13)] is

\[
K_N=\frac{\chi_N}{N}\kappa^{\sum_j\sigma_j}\eta^{b-1}N^{c+b}
 \sum_{n\in\mathcal T_d}\frac{q^{\Phi_N(n)}}{\prod_eS_{n_e}},
\quad
\Phi_N=\sum_j\{[N+\sigma_j(u_j+1+2J_j)]h_j-\sigma_jdJ_j\}
                 -2\sum_{i>1}a_i.
\tag{9}
\]

The line \(\chi_N\), the pivots, and the original averaged first cut
are unchanged. In particular the marked-cut reduction behind (9) was
made on the complete degree-preserving word, not on a separated sector.

For fixed \(p\in\mathcal P_d\), put \(C_j=N+\sigma_j(u_j+1+2J_j)\).
The entire \(j\)-th clock sum is exactly

\[
\begin{split}
\sum_{h=v}^{u+v}\frac{q^{Ch}}{S_{h-v}S_{u-h+v}}
 &=\frac{q^{Cv}}{S_u}(-q^{C+1-u};Q)_u\\
 &=\frac{q^{Cv}}{S_u}
 \begin{cases}(Q^{J+1};Q)_u,&\sigma=1,\\
               (Q^{-J-u};Q)_u,&\sigma=-1.
 \end{cases}
\end{split}
\tag{10}
\]

This is the finite binomial identity
\(\sum_{r=0}^u S_u t^r/(S_rS_{u-r})
=\prod_{k=0}^{u-1}(1+q^{2k-u+1}t)\).
All factors in (10) are nonzero: their exponents lie in
\([1,d]\) or \([-d,-1]\), and \(u=0\) gives the empty product.
It includes every endpoint of the interval (5).

Together with the untouched factorials and \(q^{-\sigma dJ}\),
the positive row is precisely

\[
\kappa x^{-J-v}Q^{vJ}
 \frac{(Q;Q)_{J+u}(Q;Q)_{u+v}}
 {(Q;Q)_u(Q;Q)_J(Q;Q)_v}.
\tag{11}
\]

For the negative row the original antiunitary flip, with its physical
over/under order, gives the conjugate phase and the same factorial
magnitude; [J, (19)--(21)] checks that phase modulo \(2N\).
Thus (10) reconstructs the original signed matrices, not only their
absolute values. Applied independently over (5), it leaves exactly
the physical path contraction with every closing degree and scalar
in (9). Nonzero individual fiber sums do not imply a nonzero final sum.

## 4. The compulsory affine character and its descent

Use the leading scaled variables \(U=u/N,V=v/N,J=J_j/N,H=h/N\).
On the physical strip \(U,V,J>0,\ U+V<1,\ U+J<1\), use the primitive
\(\mathcal J'(z)=\log(2\sin\pi z)\) marked from \(0<z<1\).
With

\[
(x_0,x_1,x_2,x_3)=(1-U-V,U-H+V,H-V,V),
\quad
L_\sigma=-\sum_{a=0}^3\mathcal J(x_a)
          +\pi i[H+\sigma H(U+2J)-\sigma J],
\tag{12}
\]

the calibrated clock graph of [J, (27e)--(27g)] is

\[
H_\sigma=V+\frac U2-\frac{\sigma i}{2\pi}
                   \log\frac{2\sin\pi(J+U)}{2\sin\pi J},
\qquad
\partial_H L_\sigma=\pi i(1+\sigma).
\tag{13}
\]

Set \(\epsilon_j=(1+\sigma_j)/2\) and define the integral covector

\[
\chi_0(\dot n)=\sum_j\epsilon_j\dot h_j
             =\sum_j\epsilon_j(\dot n_{j2}+\dot n_{j3}).
\tag{14}
\]

In particular \(\chi_0(k_j)=\epsilon_j\). The exact primitive
calibration, including its additive constant, is

\[
L_\sigma(U,V,J,H_\sigma)-2\pi i\epsilon H_\sigma
 =G_\sigma(U,V,J),
\tag{15}
\]

where the literal physical crossing action of [J, (27a)] is

\[
\begin{split}
G_\sigma={}&\mathcal J(U+V)+\mathcal J(J+U)
 -\mathcal J(V)-\mathcal J(J)-\mathcal J(U)\\
&+\pi i\sigma[-J-V+2VJ-U/2+U(J+V)+U^2/2].
\end{split}
\tag{15a}
\]

The whole leading incidence action is \(\mathcal S=\sum_jL_{\sigma_j}\)
on the path constraints; the two complementary closure primitives
cancel. These statements continue along a common analytic path only
with those same logarithmic lifts. No globally real interior path for
an arbitrary closed diagram is assumed. All order-one pivot terms
remain in (9), although they are absent from its leading action.

Suppose a point on this **same lifted regular clock graph** is an
exponentiated critical point of the whole incidence action \(\mathcal S\).
Then

\[
\chi(\ell)=\frac{D_\ell\mathcal S}{2\pi i}
       \in\mathbb Z\quad(\ell\in\Lambda_{\rm inc})
\tag{16}
\]

is an integer functional. Equation (13) gives
\(\chi|_K=\chi_0|_K\), so (8) supplies a unique
\(\bar\chi\in\Lambda_{\rm phys}^*\) with

\[
\boxed{\quad\chi-\chi_0=\pi^*\bar\chi,\qquad
\bar\chi(\dot p)=\chi(s\dot p)-\sum_j\epsilon_j\dot v_j.\quad}
\tag{17}
\]

By (15), this is the winding of the reduced physical action.
Indeed the differential of the corrected action annihilates \(K\)
on the clock graph. Its derivative along that graph therefore agrees
with its derivative along the integral section (6); their difference
is a clock tangent. This proves the derivative assertion as well as
the integral descent. An arbitrary character, or a differently lifted
algebraic clock solution, need not have the restriction required in (17).

Extend \(\chi_0\) to all incidence coordinates by the same linear
formula. At the literal finite points,
\[
q^{\Phi_N(n)-2N\chi_0(n)}=q^{\Phi_N(n)},\qquad
\exp[-2\pi i\sum_j\epsilon_jh_j]=1.
\tag{18}
\]
After scaling, this is precisely the correction
\(-2\pi i\chi_0\) to the leading action. It fixes the
source-compatible affine baseline. It is not an
off-root identity of unspecified modules or normal derivatives.

## 5. What this removes, and what it does not

The local clock directions can be removed exactly, both from the finite
sum and from the marked stationary primitive. They are not forbidden
finite-index carries: \(k_j\) changes neither a physical head index
nor any anchor charge. In particular a positive crossing has canonical
clock winding \(1\), not \(0\), while its original degree is conserved.

The residual group in (17) is the dual of the original physical-path
lattice, with its actual cut and closing equations. It is not yet the
logarithmic edge-winding lattice of a positive triangulation. The
existing physical holonomy and rational Bloch comparison do not provide
that integral, marked identification or a relative-cycle transport.
In particular no remaining nonzero character is discarded by the
finite alias argument, and no geometric coefficient or lower bound
follows from (17). This note isolates the residual comparison after
the auxiliary clocks have been removed with their correct affine mark.

## Direct source versions

Both complete written sources were read at these versions; no programs,
tests, or numerical results are used.

| Label | Source | SHA-256 |
| --- | --- | --- |
| J | [Original joint clock phase](research_joint_clock_phase_equations.md) | 71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867 |
| I | [Actual incidence cycle equations](research_incidence_cycle_difference_equations.md) | 8d9b4231b2f3a8795b857f361b2054d50a727392457a378a12adb4fe0430e618 |

Source I fixes the full integer winding convention in (16); the split
(7), its physical section, and the affine restriction (17) make explicit
which part of that convention is eliminated by the actual finite fibers.
