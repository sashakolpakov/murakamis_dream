# The incompatible shared phases in the R54 singleton

The mixed real spectral point considered here has \(\sigma_{32}=2\)
and \(\sigma_e=-2\) at all other regions. This note locates an
exact phase incompatibility on one original strand edge. It proves
that a common face-variable gauge cannot align all the local
monomials, and that the shared coefficient contains opposite
signs at all sufficiently large even levels. It supplies no
exponential estimate for that signed coefficient.

## 1. Two neighboring regions in the original diagram

Use the source incidence of
[the published singleton theorem](/private/tmp/murakamis_dream-publication/notes/actual_singleton_sector_envelope_obstruction.md).
The chosen LEFT region and one of its central neighbors have
ordered quartets
\[
 e=32:(x,b,c,y)=(0,50,16,29),\qquad
 e=18:(x,b,c,y)=(41,0,44,16).                            \tag{1}
\]
Faces \(50,29\) are protected. The output triangle of region \(32\)
is \((0,29,16)\), while the input triangle of region \(18\) is
\((41,0,16)\). Their common edge \(0\text{--}16\) has opposite
induced orientations. It is a strand edge, not a matching edge:
the matching outer diagonals of these two regions are
\(0\text{--}29\) and \(41\text{--}16\), respectively.
All labels in (1) are the literal original source labels.

For \(N=2m\), \(d=2m-1\), the protected LEFT polynomial has
monomials
\[
       L_0^j L_{16}^{d-j},\qquad 0\le j\le m-1.          \tag{2}
\]
At \(\sigma_{32}=2\), the coefficient of (2) is
\[
                 \omega_N(-1)^j A_{j,N},\qquad
                 A_{j,N}>0,                            \tag{3}
\]
with one common sign \(\omega_N\).
This is the original monomer path:
its lowering steps give \((-1)^j\), every unused factor
\(2-c_r\) is positive, and the sine factors are positive.
No row has been divided out at a spectral zero.

At the even complete endpoint \(-2\), remove the common sign
from a central region. Its polynomial has nonnegative
coefficients and contains
\[
 s_m^2(L_x+L_y)D(L_x,L_b,L_y)D(L_x,L_c,L_y).              \tag{4}
\]
Each \(D\) has strictly positive coefficients on every supported
homogeneous monomial of degree \(m-1\), by the original cofactor
recurrence. In particular the first \(D\) at region \(18\)
has full support in the three ordinary variables
\(L_{41},L_0,L_{16}\).

## 2. No shared phase gauge aligns both factors

Set \(L_f=r_fe^{i\phi_f}\), with \(r_f>0\) on ordinary faces.
To give all consecutive monomials in (2) the same phase, their
ratio in (3) requires
\[
                    \phi_0-\phi_{16}=\pi
                              \pmod {2\pi}.             \tag{5}
\]
For \(m\ge2\), full support of the first \(D\) at region \(18\)
contains two monomials differing by one unit transferred from
face \(0\) to face \(16\). Their coefficients are positive.
Keeping a fixed monomial in the second \(D\) and a fixed ordinary
outer choice in (4) gives the same two supported monomials in
the central polynomial. Equality in its triangle inequality
therefore requires
\[
                    \phi_0-\phi_{16}=0
                              \pmod {2\pi}.             \tag{6}
\]
Equations (5) and (6) are incompatible. This proves the
obstruction for every even \(N\ge4\), before any asymptotic
calculation.

It is important that the same two global variables occur in
both equations. A separate local choice of phase at the two
regions would no longer represent the original common
coefficient extraction. The conflict is already across the
single original strand edge \(0\text{--}16\); it does not
require an abstract long cycle chosen independently of the
diagram.

## 3. Opposite signs survive the original face targets

The published rational witness has strictly positive loads at
every surviving spectator-triangle corner. Its minimum is
\[
                     a_*=\frac{29141577}{40000000000}.    \tag{7}
\]
Let \(j=\lfloor(m-1)\lambda\rfloor\), with the same
\(\lambda=548219162717/10^{12}\) as in the certificate.
Then \(j+1\le m-1\) for \(m\ge2\).

The exact support proof first scales the spectator loads by
\(2(m-1)\), then corrects their column margins along a fixed
spanning tree of the spectator incidence graph. It changes
each corner by at most \(5830\). Choose \(m\) so large that
\[
                         2(m-1)a_*>5832.                \tag{8}
\]
The corrected real table then has every supported entry
greater than \(2\), with integer row and column margins.
Fractional-cycle rounding within each entry's floor/ceiling
interval gives an integral table. This standard rounding
preserves all margins and leaves every supported entry
at least \(2\): move alternating entries along a fractional
cycle until one reaches an integer; a residual fractional
forest is impossible because its leaf has integer margin.

Choose the corresponding monomial from each \(D\) factor
in (4), with the fixed ordinary outer choices used in the
support proof. Together with (2), these are one feasible
original shared array. It has a positive degree at the
face-\(0\) corner of the input triangle of region \(18\).
Now make exactly two changes:

1. At region \(32\), replace \(j\) by \(j+1\).
2. In that one triangle at region \(18\), lower its face-\(0\)
   degree by one and raise its face-\(16\) degree by one.

Both local monomials remain supported. Every triangle row
degree, every region's total degree \(d\), and every original
shared face target are unchanged. The central coefficients
keep their common positive sign. The selected LEFT sign
changes by \(-1\).

Thus the actual shared coefficient at the mixed spectral
point contains positive and negative summands, after a
single global sign is removed. In particular its absolute
value is strictly smaller than the sum of absolute array
weights at each level satisfying (8).
This is a strict finite inequality, with no claimed
uniform multiplicative or exponential loss.

## 4. What is still required for the filled period

The preceding argument identifies why the independently
maximized local coefficient rates need not survive the
original sewing. It does not estimate how much cancellation
occurs. The absolute-array rate can exceed \(\Phi\), so
an unspecified positive loss would still be insufficient:
the final bound must cross below the relevant geometric rate.

Nor does this mixed real spectral point automatically give
a stationary representation or a cone-manifold metric.
That identification would require the full phase equations
and original peripheral words. A global estimate may instead
group these two neighboring polynomials, retain the shared
alternating convolution, or apply the filling functional
before taking absolute values. Those are further analytical
tasks, not consequences of (5)–(6).
