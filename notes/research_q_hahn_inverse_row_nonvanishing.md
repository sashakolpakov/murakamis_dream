# Nonvanishing of actual inverse rows and signed q-Hahn node blocks

Written proof, 24 November 2026.

The complete inverse Clebsch frame contains a coherent subtraction
of the derivative column and a multiple of its ordinary partner.
The calibrated normal amplitude makes this subtraction nonzero
on real strict physical compacts and fixed complex magnetic collars.
Both original inverse rows then have the ordinary exponential action
with their known Christoffel--Darboux measure retained.
The same imaginary-part gap controls both terms of a signed mixed
double-node Jordan contribution, uniformly over every physical
auxiliary color, including its exact color zeros.

The pair degree remains an original physical integer. No continuation
of the finite-dimensional inverse measure in that degree is asserted.
No scalar closing or full contracted coupon lower bound follows.

## 1. Exact columns, measures, and inverse rows

Let \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), \(x=q^d\).
Take physical integer degrees and an actual double pair
\[
 0\le j<l,\qquad j+l=d,\qquad s=l-j,\qquad l\le t\le d.
 \tag{1}
\]
Write \(c_m=q^{2m+1}+q^{-2m-1}\) and
\(\nu_j=(-1)^j q^{j(j+1)}\). Let \(C_j(t,u)\) be the
original column, normalized by \(C_j(t,0)=1\), and retain its
actual generic derivative normal
\[
 w_j(t,u)=\frac{D C_j(q;t,u)-D C_l(q;t,u)}
 {-2N\Delta_j},\qquad
 \Delta_j=q^{2j+1}-q^{-2j-1}.
 \tag{2}
\]
Here the two \(C_m(\zeta;t,u)\) use the original highest weight
\(d\), \(D=\zeta\partial_\zeta\) is evaluated at \(\zeta=q\),
and \(N,t,u\) are fixed during that derivative. For complex \(u\),
use the same finite source and logarithmic lift as [N].
Thus this is a specified magnetic continuation of the actual rows.

Define the real-rooted polynomial and its deleted double factor by
\[
 P_t(Z)=\prod_{m=0}^{t}(Z-c_m),\qquad
 Q_{t,j}(Z)=\frac{P_t(Z)}{(Z-c_j)^2}.
 \tag{3}
\]
Set \(S_t=\prod_{r=1}^{t}2\sin(\pi r/N)\), \(S_0=1\), and
\[
 B_t=(-1)^t S_t^2,\qquad
 \sigma_{t,j}=\frac{x^t\nu_j Q_{t,j}(c_j)}{B_t},\qquad
 \eta_{t,j}=\rho_j+\frac{Q_{t,j}'(c_j)}{Q_{t,j}(c_j)},\quad
 \rho_j=-\frac{s}{2\Delta_j}.
 \tag{4}
\]
In particular \(\sigma_{t,j}\ne0\).
These are the original complex measures, including their phases.

For the complete frame \(V_t\), with double columns ordered as
\((C_j,w_j)\), [H,M] give exactly the bilinear Gram and inverse
\[
 \begin{pmatrix}C_j^T C_j&C_j^T w_j\\
                 w_j^T C_j&w_j^T w_j\end{pmatrix}
       =\sigma_{t,j}\begin{pmatrix}0&1\\1&\eta_{t,j}\end{pmatrix},
 \qquad
 V_t^{-1}=(V_t^TV_t)^{-1}V_t^T .
 \tag{5}
\]
Thus the two actual inverse row entries, at a physical magnetic
index \(u\), are
\[
 \boxed{\quad
 L^{\rm val}_{t,j}(u)=\sigma_{t,j}^{-1}
                      [w_j(t,u)-\eta_{t,j}C_j(t,u)],\qquad
 L^{\rm nor}_{t,j}(u)=\sigma_{t,j}^{-1}C_j(t,u).
 \quad}
 \tag{6}
\]
The first extracts the coefficient of the value column, the second
that of the normal column. There is no Hermitian conjugation in
(5) or (6). At noninteger \(u\), equation (6) defines the literal
continuation of those finite source expressions. The measures are
still those of the physical integer block \(t\).

## 2. Statement on a complex magnetic collar

Let
\[
 {\cal P}=\{(\tau,\nu)\in\mathbb C^2:
       \tfrac12<\Re\tau<1,\quad0<\Re\nu<\Re\tau\},\qquad
 {\cal P}_{\mathbb R}={\cal P}\cap\mathbb R^2 .
 \tag{7}
\]
For every compact \(S\Subset{\cal P}_{\mathbb R}\), there is a
fixed compact complex neighborhood \(K\Subset{\cal P}\) of \(S\),
constants \(\delta,c,C>0\), and \(N_0\), such that the following
hold for \(N\ge N_0\). Take (1), \(s\le\delta N\), \(u\in\mathbb C\),
and \((t/N,u/N)\in K\). Then
\[
 \boxed{\quad
 cN\,\frac{|C_j(t,u)|}{|\sigma_{t,j}|}
 \le |L^{\rm val}_{t,j}(u)|
 \le CN^3\,\frac{|C_j(t,u)|}{|\sigma_{t,j}|},
 \qquad
 |L^{\rm nor}_{t,j}(u)|=
                    \frac{|C_j(t,u)|}{|\sigma_{t,j}|}.
 \quad}
 \tag{8}
\]
There is also a relative asymptotic formula retaining the exact shear:
\[
 L^{\rm val}_{t,j}(u)
     =\frac{C_j(t,u)}{\sigma_{t,j}}
           [N{\cal F}_{\xi}(t/N,u/N)-\eta_{t,j}](1+o(1)),
 \qquad \xi=j/N,
 \tag{9}
\]
\[
 |N{\cal F}_{\xi}-\eta_{t,j}|\ge cN .
 \tag{10}
\]
Here \({\cal F}_\xi\) is the source primitive in [N].
The relative error is uniform in these physical degree blocks
and has all fixed holomorphic \(\nu\) derivatives on smaller collars.
In particular
\[
 \frac1N\left(\log|L^{\rm val}_{t,j}(u)|
                   -\log|C_j(t,u)/\sigma_{t,j}|\right)
                          =O(\log N/N).
 \tag{11}
\]
The normal dual row has the exact comparison in (8).
The ordinary column's nonzero amplitude from [N] can be substituted
in (9), without changing the retained inverse measure or its phase.

The pair degree \(t\) is a physical integer in every assertion.
Only the magnetic coordinate \(u\) varies in its fixed complex collar.

## 3. The exact imaginary part of the inverse shear

The polynomial \(P_t\) in (3) has real coefficients and real roots.
Deleting both occurrences of \(c_j\) leaves \(Q_{t,j}(c_j)\ne0\).
Consequently its logarithmic derivative in (4) is real.
The other term is fixed by the original endpoint normal:
\[
 \rho_j=-\frac{s}{2\Delta_j}
        =\frac{i s}{4\sin(\pi s/N)},\qquad
 \boxed{\quad
 \frac{\Im\eta_{t,j}}N
       =\frac{s}{4N\sin(\pi s/N)}\ge\frac1{4\pi}.
 \quad}
 \tag{12}
\]
For its normalization, the original generic endpoint in [G] is
\(C_m(\zeta;t,t)=(-1)^m
 \zeta^{dt-2Nm+m^2+m}\).
The two endpoint exponents differ by \(Ns\). Dividing their
derivative difference by the actual gap in (2) gives precisely
\(\rho_j\). Also \(2j+1=N-s\), so
\(\Delta_j=2i\sin(\pi s/N)\), with the sign in (12).
The final inequality uses \(\sin a\le a\).
No real part of \(\eta_{t,j}\) is discarded.

We will also use the existing uniform upper bound
\[
                         |\eta_{t,j}|\le CN^3 .
 \tag{13}
\]
For completeness, every distinct node difference factors as
\(|c_j-c_m|=|1-Q^{j-m}|\,|1-Q^{j+m+1}|\ge16/N^2\).
The logarithmic derivative of \(Q_{t,j}\) is a sum of fewer than
\(N\) such reciprocals, counted with multiplicity. The remaining
\(\rho_j\) is \(O(N^2)\). This proves (13), including all parities.

## 4. A strict gap for the calibrated column normal

We verify the real-domain inequality needed here.
In the folded coefficient of [N], set
\[
 c=\cos(\pi\tau),\quad \sigma=e^{\pi i\tau},\quad
 z=e^{\pi i(\tau-2\nu)},\quad W=1-2cz,\quad
 {\cal F}_0=\frac{\sqrt W+i\sigma}{8\pi c}.
 \tag{14}
\]
For real \((\tau,\nu)\in{\cal P}_{\mathbb R}\), put \(b=-c\in(0,1)\)
and \(\theta=\pi(\tau-2\nu)\).
Then \(|\theta|<\pi\tau<\pi\), and \(a=\cos\theta>-b\).
Along this real slice \(W=1+2be^{i\theta}\) avoids the negative
real axis; its source square root has positive real part.
If \(v=\Im\sqrt W\), then
\[
 v^2=\frac{\sqrt{1+4b^2+4ba}-1-2ba}{2}<b^2.
 \tag{15}
\]
Indeed \(1+2ba+2b^2>1\), and its square minus
\(1+4b^2+4ba\) equals \(4b^2(a+b)^2>0\).
It follows that
\[
              0<\Im{\cal F}_0
                     =\frac{1-v/b}{8\pi}<\frac1{4\pi}.
 \tag{16}
\]
On the given compact \(S\), the upper inequality has a positive
margin. Choose a small complex collar \(K\Subset{\cal P}\) so
that the same strict upper margin, slightly decreased, holds for
\(\Im{\cal F}_0\) there.

The source primitives \({\cal F}_\xi\) in [N] depend continuously
on the real parameter \(\xi\) through \(1/2\), uniformly on \(K\).
Take \(\delta\) small enough to obtain the fixed-window amplitude
of [N] on a buffered version of this collar, and also
\[
       \sup_K\Im{\cal F}_\xi\le\frac1{4\pi}-2c
 \tag{17}
\]
for the resulting actual \(\xi=j/N\).
The calibrated amplitude gives
\[
 R_{N,j}=w_j/C_j=N{\cal F}_\xi+o(N),\qquad
             \sup_K\Im(R_{N,j}/N)\le\frac1{4\pi}-c
 \tag{18}
\]
for large \(N\), with every fixed magnetic derivative.
Equations (12),(17),(18) imply
\[
 |R_{N,j}-\eta_{t,j}|\ge cN,\qquad
 |N{\cal F}_\xi-\eta_{t,j}|\ge cN .
 \tag{19}
\]
This uses the actual coherent subtraction, not a lower bound for
its two terms taken separately.
The argument applies in the complex magnetic collar because its
measure and shear still come from the real physical integer block.

## 5. Relative inverse-row amplitude

Since \({\cal F}_\xi\) is bounded on this collar, [N] also gives
\(|R_{N,j}|\le CN\). Equations (13),(19) prove (8).
For the stronger formula, use the exact factorization
\[
 R_{N,j}-\eta_{t,j}
  =(N{\cal F}_\xi-\eta_{t,j})
    \left(1+\frac{R_{N,j}-N{\cal F}_\xi}
                   {N{\cal F}_\xi-\eta_{t,j}}\right).
 \tag{20}
\]
The numerator in the fraction is \(o(N)\), uniformly with
magnetic derivatives; its denominator is at least \(cN\).
At each physical \(t\), the shear is independent of \(u\).
The quotient is analytic on the collar, so buffered Cauchy
estimates prove (9) with all stated relative derivatives.
The remaining inverse normal row is exactly the second formula
in (6). The bounds in (8) immediately give (11).

The original measure can be kept quantitatively visible:
\[
 |\sigma_{t,j}|=
 \frac{N S_{t-j}S_{t+j-d}}
 {S_t^2\,|1-Q^{2j+1}|^2}.
 \tag{21}
\]
All factorial indices are physical integers below \(N\).
Its complex phase remains the one in (4). Neither this measure
nor \(Q_{t,j}'/Q_{t,j}\) has been replaced by an asymptotic surrogate.

## 6. Both crossing signs and every physical auxiliary color

Let \(1\le n\le N\) be an actual integer color. The original mixed
compiler [M] has
\[
 L_n=l_n(\Omega),\qquad
 l_n(Z)=(-1)^{n-1}\mathsf U_{n-1}(Z/2),
 \tag{22}
\]
where \(\mathsf U_r\) is the Chebyshev polynomial of the second kind.
Write \(\kappa=q^{d^2/2}\); the original signed pair crossing
\(\mathscr R^\epsilon\), \(\epsilon\in\{+1,-1\}\), retains
\(\mathscr R(c_j)=\kappa\nu_j\) and its logarithmic derivative
\(\rho_j\). At physical magnetic ports \(u,v\), the sum of both
terms of the double-node contribution to \(\mathscr R^\epsilon L_n\)
is exactly
\[
 {\cal D}_{t,j}^{\epsilon,n}(u,v)
   =\frac{\kappa^\epsilon\nu_j^\epsilon}{\sigma_{t,j}}\,
       C_j(t,u)C_j(t,v)\,{\cal A}_{t,j}^{\epsilon,n}(u,v),
 \tag{23}
\]
\[
 {\cal A}_{t,j}^{\epsilon,n}
    =l_n'(c_j)+l_n(c_j)
          [R_{N,j}(t/N,u/N)+R_{N,j}(t/N,v/N)
                         +\epsilon\rho_j-\eta_{t,j}].
 \tag{24}
\]
Here the prime on \(l_n\) is its polynomial spectral derivative.
Equation (23) is bilinear, with no conjugated column. It follows
from the exact Jordan function
\(\left(\begin{smallmatrix}A(c)&A'(c)\\0&A(c)\end{smallmatrix}\right)\)
and the full inverse block (5); it is [M, equation (7)].
All Cartan, crossing, color, and measure phases shown there remain.
The complex magnetic kernel used below is specified by continuing
these same finite column expressions, with \(t,n\) and all measure
factors still physical.

For any compact real family of triples
\[
 \tfrac12<\tau<1,\qquad 0<\nu<\tau,\qquad0<\omega<\tau,
 \tag{25}
\]
apply the preceding construction to the union of its two
\((\tau,\nu)\) and \((\tau,\omega)\) projections. On a sufficiently
small fixed complex magnetic collar, with \(\tau=t/N\) still
physical and real, shrink \(\delta\) so that
\[
 c\le\Im(R_{N,j}/N)\le\frac1{4\pi}-c,\qquad
 c\le\Im{\cal F}_\xi\le\frac1{4\pi}-c
 \tag{26}
\]
at both ports. This follows from both strict inequalities in (16), continuity,
and [N], just as in (17)--(18).

Let \(q_{t,j}=Q_{t,j}'(c_j)/Q_{t,j}(c_j)\in\mathbb R\).
For \(l_n(c_j)\ne0\), both \(l_n(c_j)\) and \(l_n'(c_j)\) are real.
Using \(\eta_{t,j}=\rho_j+q_{t,j}\), the imaginary part of
\({\cal A}/l_n(c_j)\) is the imaginary part of
\[
 \begin{cases}
 R(t/N,u/N)+R(t/N,v/N),&\epsilon=+1,\\
 R(t/N,u/N)+R(t/N,v/N)-2\rho_j,&\epsilon=-1 .
 \end{cases}
 \tag{27}
\]
It is at least \(2cN\) in the first case and at most \(-2cN\)
in the second, by (12),(26).
Exactly the same bounds hold if each \(R\) is replaced by
\(N{\cal F}_\xi\).

These bounds are uniform through all integer-color cases.
Put \(\theta_j=(2j+1)\pi/N\in(0,\pi)\). The exact color formula is
\(l_n(c_j)=(-1)^{n-1}\sin(n\theta_j)/\sin\theta_j\).
If this value is nonzero, the numerator is a nonzero root-lattice
sine, so
\[
 |l_n(c_j)|\ge\sin(\pi/N)\ge2/N.
 \tag{28}
\]
If it is zero, direct polynomial differentiation gives instead
\[
 |l_n'(c_j)|=\frac{n}{2\sin^2\theta_j}\ge\frac12 .
 \tag{29}
\]
Thus both the exact coefficient and its specified leading version
\[
 {\cal A}^{\rm lead}
  =l_n'(c_j)+l_n(c_j)
       [N({\cal F}_\xi(t/N,u/N)+{\cal F}_\xi(t/N,v/N))
                               +\epsilon\rho_j-\eta_{t,j}]
 \tag{30}
\]
are bounded below in modulus by a positive constant, uniformly
in all \(1\le n\le N\) and both signs. Their upper bound is \(CN^4\):
[M] gives \(|l_n|\le N\), \(|l_n'|\le N(N^2-1)/6\), while
\(R=O(N)\), \(\rho_j=O(N^2)\), and \(\eta_{t,j}=O(N^3)\).

For nonzero \(l_n(c_j)\), the error in replacing the exact
coefficient by (30) is \(|l_n|o(N)\), while its denominator
has modulus at least \(2cN|l_n|\).
When \(l_n(c_j)=0\), that error is identically zero.
Consequently, uniformly over all colors and both signs,
\[
 {\cal D}_{t,j}^{\epsilon,n}(u,v)
  =\frac{\kappa^\epsilon\nu_j^\epsilon}{\sigma_{t,j}}\,
       C_j(t,u)C_j(t,v)\,{\cal A}^{\rm lead}(1+o(1)).
 \tag{31}
\]
Every fixed magnetic derivative of the relative error tends to
zero on smaller collars. In particular the exponential action of
this individual double-node contribution is the sum of its two
ordinary-column actions minus the retained measure action.
The factor \({\cal A}^{\rm lead}\) costs only \(O(\log N)\) in
the logarithm. At complete color \(n=N\), the zero case is kept
exactly, rather than dividing by the vanishing value.

The hypothesis \(\epsilon\in\{+1,-1\}\) is essential to this proof.
For \(\epsilon=0\) the imaginary combination would subtract only
one \(\rho_j\), and may cancel. No assertion is made in that case.

## 7. Scope and complete inputs

The complete frame still includes every other double block and
every unpaired simple block, including the odd self-paired node
when present. No additional normal is assigned to a simple block;
its inverse row remains its original inverse simple measure
times its ordinary column.
The result estimates selected double-block rows, not a quotient
obtained by removing the other channels.

[H,M] already supply the exact full inverse and local coupon
formulas. [O] already supplies strict real half-prefix action and
spectral derivatives. The added conclusion here is the nonzero
complex magnetic packet for the actual dual value-row subtraction
and for an individual signed double-node contribution, at every color.
It is not a new sector estimate or a general assertion about
positivity of the inverse frame.

There is no noninteger-\(t\) version of \(P_t\), \(\sigma_{t,j}\),
or its inverse Gram being asserted. Subsequent turns, wire sums,
source restrictions, caps and exterior factors remain literal.
Nonzero inverse entries and individual node contributions do not
prevent cancellation in the sum over nodes, a complete sewn coupon,
or the original scalar. Nor do they
bound the complete tangential error of a geometric trial for the
quartic minimum. No knot-volume or finite-exception conclusion
is claimed.

The complete chosen inputs and closest coverage are:

| Label | Complete text | SHA256 |
| --- | --- | --- |
| N | [Calibrated normal transport](research_q_hahn_calibrated_normal_transport.md), 582 lines | 07cd14b27ac3743ab28995d4debabae8e54867cd13b72dc2c250a3555618e0a5 |
| H | [Complete Casimir Hermite packet](actual_complete_casimir_hermite_packet.md), 321 lines | a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c |
| G | [Physical-grid partner normal](actual_q_hahn_physical_partner_normal_bound.md), 232 lines | 0725b210bd16899260533cf7a1a7aa9602a7ed0b0e18baf4831efb7a968e07d3 |
| M | [Mixed original-source compiler](actual_mixed_augmented_plat_compiler.md), 258 lines | 607fb4180794c43b51485cbba64159781b2a5b26160e7a6e28d1f61d8c5805b4 |
| O | [Off-spectrum prefix action](actual_casimir_off_spectrum_prefix_action.md), 188 lines | 2a1f8afd64324da1cb39cfd1e235aafaecda40b00cb14abf8f15d45de4945b6f |

Only written mathematics, complete text reads, and metadata hashes
were used. No mathematical program, numerical experiment, test,
build, earlier-final edit, or manuscript change was made.
