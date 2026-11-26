# Degree-scalar frames of the opposite-polarization source

Private written proof, 18 November 2026.

A scalar function of the conserved total occupation can change the
diagonal framing of an individual opposite-polarization kernel.
There is an exact norm-one condition under which it changes neither
the paired source coupon nor its marked functional. This isolates a
permitted source frame change from an arbitrary normalization of a
period. It does not prove that the actual kernel has one analytic
phase or that the geometric component occurs.

The sole complete direct is J, pinned below. The norm-one group,
its elementary descent, and all covariance calculations are proved
here on the actual finite occupation spaces.

## 1. Finite degrees and the reflection

Fix \(N\ge2\), \(m\ge2\), \(d=N-1\), \(r=m-1\), and \(D=rd\).
The common meridian \(M\) varies near one at the fixed quantum root.
Let \(U_k\) be the finite remaining-head subspace of total integer
occupation \(k\), and let \(P_k\) be its constant projector:
\[
 U=\bigoplus_{k=0}^{D}U_k,\qquad
 \mathsf n|_{U_k}=kI,\qquad
 K_0|_{U_k}=\chi_kI .
 \tag{1}
\]
J proves the exact reflection rules
\[
 T(M)U_k\subset U_{D-k},\qquad J(M)U_k\subset U_{D-k},
 \tag{2}
\]
and generic invertibility of these maps. Its source identities are
\[
 J(M)J(M^{-1})=a_N(M)H(M)^{-1},\qquad
 H(M)=D_N(MK_{\rm r}(M)),
 \tag{3}
\]
\[
 \Phi_0(W_\beta(M))
   =\frac{D_N(M)}{a_N(M)}
       \operatorname{Tr}\bigl(J(M)B_{\beta^{\rm rev}}(M^{-1})
                                      J(M^{-1})\bigr).
 \tag{4}
\]
Every scalar and the original meromorphic continuation in these
formulas are those of J.

For a family of scalar germs \(f=(f_k(M))_{0\le k\le D}\), define
\[
 f^\iota_k(M)=f_{D-k}(M^{-1}),\qquad
 F(M)=\sum_{k=0}^{D}f_k(M)P_k .
 \tag{5}
\]
This is an involution on the finite product of meromorphic germ
fields. Equation (2), applied to each actual integer sector, gives
\[
 J(M)F(M^{-1})=F^\iota(M)J(M),
 \tag{6}
\]
and the identical equation for \(T\).
No coefficient at a noninteger occupation has been defined.

## 2. Exact norm-one frame changes

Let every \(f_k\) be holomorphic and nonzero near one and impose
\[
 f_k(M)f_{D-k}(M^{-1})=1
                      \quad(0\le k\le D).
 \tag{7}
\]
Thus \(F^\iota=F^{-1}\). Define the framed kernels
\[
 J^f(M)=F(M)J(M),\qquad T^f(M)=F(M)T(M).
 \tag{8}
\]
Using (6) twice proves
\[
 J^f(M)J^f(M^{-1})=J(M)J(M^{-1}),\qquad
 T^f(M)T^f(M^{-1})=T(M)T(M^{-1}).
 \tag{9}
\]
The source normalization has not changed. The meridian pole
orders have not increased, since \(F\) and its inverse are
holomorphic at one.

There is a useful dual form of (6):
\[
 J^f(M^{-1})=J(M^{-1})F(M)^{-1}.
 \tag{10}
\]
Consequently for any finite matrix \(B(M)\), whether or not it
preserves degree,
\[
 J^f(M)B(M)J^f(M^{-1})
       =F(M)\bigl(J(M)B(M)J(M^{-1})\bigr)F(M)^{-1}.
 \tag{11}
\]
Its trace is exactly unchanged. If \(B\) preserves degree,
the product between parentheses preserves degree too, so
the matrices themselves agree.

For precision, the paired functional on an arbitrary full
matrix \(A\) uses
\(B=q_F^{\rm ref}\mathscr C^{-1}A\mathscr C i_F^{\rm ref}\).
Moving the rectangular factors through its trace writes
its full source coupon as \(D_N(M)/a_N(M)\) times
\[
 \mathscr C\,i_F^{\rm ref}\,
       J(M^{-1})J(M)\,q_F^{\rm ref}\mathscr C^{-1}.
 \tag{12}
\]
The reversed version of (9) leaves this matrix unchanged.
For an actual unmarked word it is the paired realization
of the original source in (4). For arbitrary marks (11)
preserves the paired marked functional, not only an
unmarked numerical knot value. No inserted coupon is
declared to satisfy a new intertwining equation.
The explicit Ward corrections of a marked presentation
must still be retained when such equations are used.

For an actual degree-preserving braid word \(B_\pm\),
\[
 B_+(M)T^f(M)=T^f(M)B_-(M^{-1})
 \tag{13}
\]
follows from J's intertwining equation and \([B_+,F]=0\).
For arbitrary matrices \(A_\pm\), put
\(\Delta=A_+T-TA_-\). The exact extra row is instead
\[
 \Delta^f=F\Delta+[A_+,F]T .
 \tag{14}
\]
It is not omitted for a mark that mixes degrees.

## 3. Elementary descent and the possible fixed-degree sign

The transformations satisfying (7) form an abelian group.
They act freely on the chosen orbit of \(J\), since \(J\)
is generically invertible. No claim is made that every
operator with the same observable equations belongs to
this degree-scalar orbit.

For any nonzero scalar family \(b\), the formula
\[
                         f=b/b^\iota
 \tag{15}
\]
satisfies (7). Conversely every holomorphic unit solution
of (7) has this form with holomorphic unit \(b\), except
for one explicit possible sign at the fixed degree.
Here is a direct proof, including that qualification.

For a two-element degree orbit \(\{k,D-k\}\), choose
\(b_k(M)=f_k(M)\) and \(b_{D-k}(M)=1\). Equation (7)
then gives (15) on both components.

If \(D\) is even, there is the single fixed degree
\(k_*=D/2\). In the coordinate \(\mu=\log M\), its
condition is \(f(\mu)f(-\mu)=1\), so \(f(0)=\pm1\).
If \(f(0)=1\), take the holomorphic logarithm \(\ell\)
with \(\ell(0)=0\). The identity
\(\exp(\ell(\mu)+\ell(-\mu))=1\) and continuity imply
\(\ell(-\mu)=-\ell(\mu)\). Then \(b=\exp(\ell/2)\)
is a unit solution of (15).

If \(f(0)=-1\), write \(f=-\exp\ell\) with \(\ell\)
odd and \(\ell(0)=0\). No holomorphic unit \(b\) can
give (15), since its ratio at the fixed point is one.
The meromorphic choice
\[
                  b(M)=(M-M^{-1})\exp(\ell/2)
 \tag{16}
\]
does give it. Its simple zero is not to be removed
from a separately used frame. The ratio \(f\) itself
remains a holomorphic unit; the source change (8)
uses that ratio.

Thus the only obstruction for unit frames in this
local finite-degree problem is the fixed-degree
sign. This is an elementary norm-one descent
calculation, not an invocation of a theorem to
fix an unspecified period. In particular a
constant minus sign at a fixed degree is not
silently treated as a unit coboundary.

## 4. Relative resolutions and boundary covariance

Let \(P_{\mathcal C}\) denote J's actual coherent
partial resolution on an oriented chain \(\mathcal C\).
It need not be a projector. At a fixed meridian the
windowed three-kernel expression transforms exactly as
\[
 \begin{split}
 &\operatorname{Tr}\bigl(
 P_{\mathcal C_0}J^f P_{\mathcal C_1}B
                          P_{\mathcal C_2}J^f_{\rm ref}\bigr)\\
 &\quad=\operatorname{Tr}\bigl(
 F^{-1}P_{\mathcal C_0}F\,J P_{\mathcal C_1}B
                          P_{\mathcal C_2}J_{\rm ref}\bigr).
 \end{split}
 \tag{17}
\]
This is (10) and cyclic trace. Thus it is unchanged
if the outer window commutes with degree. No
commutation of the interior windows with \(F\)
is required for (17).

A sufficient geometric condition for this commutation
is that the outer compact coherent chain is invariant,
with its orientation, under
\((w_i,z_i)\mapsto(e^{-i\theta}w_i,e^{i\theta}z_i)\)
simultaneously on all heads. Indeed the coherent
projector transforms by conjugation with
\(\exp(i\theta\mathsf n)\); integrate that identity
over the invariant chain and its invariant measure.
The resulting \(P_{\mathcal C}\) commutes with
\(\exp(i\theta\mathsf n)\) for every \(\theta\),
and hence with \(\mathsf n\) and \(F\).
Fixed-degree projective resolutions also have this
property directly from (1).

For two windows the transport defect is
\[
 P_{\mathcal C}T^f-T^fP_{\mathcal D}
   =F(P_{\mathcal C}T-TP_{\mathcal D})
                         +[P_{\mathcal C},F]T .
 \tag{18}
\]
For a homogeneous outer window only the first
term remains. Neither formula proves that the
original defect vanishes or has a smaller
exponential rate. Boundary transgressions,
complementary chains and their normal terms
remain those of the actual kernels.

## 5. Analytic degree gauges and their cost

The allowed group includes frames with a
specified semiclassical size, without interpolating
a state coefficient. Choose a holomorphic function
\(g(t,\mu)\) on a neighborhood of the compact set
\([0,r]\times\{0\}\), and put
\[
 b_k(M)=\exp\bigl(Ng(k/N,\log M)\bigr),\qquad
 f_k(M)=
 \exp N\left[g(k/N,\log M)
            -g((D-k)/N,-\log M)\right].
 \tag{19}
\]
This is an actual finite diagonal matrix at
every \(N\). Equation (7) holds exactly,
including the \(D/N=r-r/N\) correction.
It is not replaced by a limiting reflection
before the source is paired.

If \(|g|\le C\) on a slightly larger compact
parameter domain, then in the actual orthogonal
occupation-degree basis
\[
                 \|F\|,\ \|F^{-1}\|\le e^{2CN}.
 \tag{20}
\]
Cauchy's formula gives fixed meridian derivatives
bounded by a polynomial in \(N\) times such an
exponential on a smaller domain. These bounds
record a possible cost; they are not a volume
estimate and do not make the frame uniformly
bounded.

If a separately justified phase description
has such a scalar degree factor, (19) can
change its odd part under degree reflection.
Equations (9)--(12) show why this freedom is
irrelevant to the fully paired source.
They do not supply the phase description,
its analytic amplitude or a continuation
of an integer-degree coefficient to a
complex geometric moment.

The exact new conclusion is that the residual
degree-scalar framing is a controlled norm-one
source freedom, with the fixed-degree sign and
relative-window correction stated explicitly.
The geometric-cycle and finite-exception
volume statements remain open.

## Complete proof-source pin

J: notes/research_opposite_polarization_source_kernel.md,
SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.

The complete matching direct was read nontruncated
in this active sequence. The calculations above
use finite degree blocks and exact kernel
composition only. No mathematical program,
numerical experiment, frozen note or public
file was changed.
