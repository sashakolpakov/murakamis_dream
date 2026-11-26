# A faithful middle-weight model for Conway face operators

21 November 2026. Research note. Earlier final notes and the public
manuscripts remain unchanged.

The second-head wrap correction between the first and middle local
five-point descriptions vanishes on a particular invariant physical
subspace. That subspace still represents the entire Conway boundary
algebra faithfully, including its repeated-root derivatives. Thus the
correction can be removed there before taking any asymptotic estimate.

The original closing and turn must be reconstructed from the complete
boundary packet. The all-array physical trace is not simply restricted
to this subspace. Other endpoint projectors and the full relative
coefficient cycles remain.

## 1. The physical subspace

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
The original two physical heads have basis \(|a,b\rangle\),
\(0\le a,b\le d\). Their clock operators are
\[
 Z|a,b\rangle=Q^a|a,b\rangle,\qquad
 T|a,b\rangle=Q^b|a,b\rangle .
 \tag{1}
\]
Use the actual cyclic face unit \(X=xS_2S_1^{-1}\), with
\(x=-q^{-1}\) and the original nonzero wrap marks. It lowers the
first index and raises the second, cyclically, and satisfies
\[
 XZ=QZX,\qquad XT=Q^{-1}TX.
 \tag{2}
\]
Here \(S_i\) raises head \(i\), with coefficient one before its
last index and wrap coefficient \(\mu_i\ne0\); the original marks
obey \(\mu_2=x^N\mu_1\).
Define
\[
 \mathcal M_N=\operatorname{span}\{v_a=|a,d-a\rangle:0\le a\le d\}.
 \tag{3}
\]
The clock \(ZT\) has eigenvalue \(Q^{a+b}\) at \(|a,b\rangle\).
Because \(0\le a+b\le2N-2\), the congruence
\(a+b\equiv d\pmod N\) forces \(a+b=d\). Consequently
\(\mathcal M_N\) is the entire \(ZT=Q^d\) eigenspace.
Equations (1)--(2) show that \(X,Z,T\), their spectral projectors,
and every expression in these operators preserve \(\mathcal M_N\).
An inverse, when defined on the full space, preserves it as well.
On this subspace,
\[
                         T=Q^{-1}Z^{-1}.
 \tag{4}
\]

## 2. The first/middle wrap correction disappears exactly

In the same physical frame, the first and middle face descriptions use
\[
 n=e_1S_2=(Q-Z^{-1})X,\qquad
 c=n(I-E_d(T)),
 \tag{5}
\]
where \(E_d(T)\) projects onto second-head index \(d\).
Similarly \(E_j(Z)\) projects onto first-head index \(j\).
The right-hand expression in (5) defines \(n\) directly;
\(e_1\) is the original first-head Gauss lowering operator.
The original finite Euler polynomial is
\[
 P_Q(A)=\sum_{h=0}^{d}
 \frac{(-1)^hQ^{h(h-1)/2}}{(Q;Q)_h}A^h.
 \tag{6}
\]
Here \((Q;Q)_h=\prod_{j=1}^{h}(1-Q^j)\), with empty product one.
Both \(n\) and \(c\) are nilpotent of order at most \(N\), and
their Euler matrices are invertible.

**Proposition 1.** On all of \(\mathcal M_N\),
\[
                 n=c,\qquad P_Q(n)=P_Q(c).
 \tag{7}
\]

**Proof.** The only vector of \(\mathcal M_N\) in the range of
\(E_d(T)\) is \(v_0=|0,d\rangle\). The first lowering operator
\(e_1\) kills first-head index zero. Therefore
\(nE_d(T)|_{\mathcal M_N}=0\), which proves the first identity.
Both operators preserve the subspace, so every power agrees there,
giving the second identity. \(\square\)

Equivalently the full-space transition
\(P_Q(n)P_Q(c)^{-1}-I\) restricts to zero. Every local face factor
in the two displayed five-point descriptions preserves this subspace,
so subsequent such factors cannot make that restricted zero visible.
No estimate of the correction's norm or geometric volume is needed
for this representation.

This removes precisely the second-head wrap correction in (5).
It does not remove the strict first-head endpoint already present in
\(n\), or the middle factor \(QX(I-E_0(Z))\). The projector
\(E_0(Z)|_{\mathcal M_N}\) is nonzero.

## 3. Why the restriction retains the full boundary algebra

Let \(\Omega_d\) be the original pair Casimir on \(\mathcal M_N\).
In the ordered basis \(v_0,\ldots,v_d\), it is irreducible
tridiagonal. The complete source theorem gives its characteristic
and minimal polynomial
\[
 P_N(z)=\prod_{j=0}^{d}(z-c_j)=2T_N(z/2)+2,\qquad
 c_j=2\cos\frac{(2j+1)\pi}{N}.
 \tag{8}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind.
Thus the representation
\[
 \rho_N:H_N=\mathbb C[z]/(P_N)\longrightarrow
                  \operatorname{End}(\mathcal M_N),\qquad
 \rho_N(f)=f(\Omega_d)
 \tag{9}
\]
is injective. In particular it retains the first derivatives at every
double root. It is not the representation by values at distinct roots.
Here a whole Hopf box means an actual two-head operator \(f(\Omega)\)
from the complete Conway compiler. An individual face factor need
not belong to this algebra.

There is an explicit packet isomorphism as well. Put
\[
 s_r=\prod_{j=1}^{r}2\sin(\pi j/N),\qquad
 b_r(z)=s_r^{-2}\prod_{j=0}^{r-1}(c_j-z),\qquad s_0=1,
\]
\[
 C_N=\big[b_0(\Omega_d)v_0\ \cdots\
                         b_d(\Omega_d)v_0\big].
 \tag{10}
\]
A polynomial of degree \(r\) in an irreducible tridiagonal matrix,
applied to \(v_0\), has support only in indices \(0,\ldots,r\).
Its index-\(r\) coefficient is its leading coefficient times the
nonzero unique outer path. Hence \(C_N\) is triangular with nonzero
diagonal and is invertible. The map
\[
 \Xi_N(f)=f(\Omega_d)v_0=C_N\alpha,\qquad
                         f=\sum_{r=0}^{d}\alpha_rb_r
 \tag{11}
\]
is an isomorphism from the full packet space onto \(\mathcal M_N\).

The original marked cap and Frobenius closing, and the genuine
quarter-turn, are therefore exactly
\[
 m_N(y)=\mathbf e_0^{\mathsf T}C_N^{-1}y,\qquad
 \phi_N^{\rm pkt}(y)=\mathbf e_d^{\mathsf T}C_N^{-1}y,\qquad
 J_N^{\rm pkt}=C_NP_{\rm rev}C_N^{-1}.
 \tag{12}
\]
The \(\mathbf e_i\) are standard coordinate vectors, and
\(P_{\rm rev}\alpha\) reverses the \(N\) Newton coefficients;
\(\phi_N^{\rm pkt}\) is a functional, not the scalar used below.
These are the actual original closures and turn, since in Newton
coordinates they are \(\alpha_0,\alpha_d\), and reversal.
The turn is a linear packet operation; it is not asserted to be
multiplicative on matrices.

The Frobenius closing has a particularly simple extension to all
middle-block matrices. Let
\[
 \Lambda_N=\frac{(-1)^dN^2}
            {\prod_{j=0}^{d-1}(\Omega_d)_{j+1,j}},\qquad
             \Phi_N^{\rm end}(A)=\Lambda_N A_{d,0}.
 \tag{12a}
\]
Every factor in the denominator is nonzero. For a polynomial of
degree at most \(d\), only its leading term can reach the outer
entry \((d,0)\). Since the original Frobenius functional is
\((-1)^dN^2[z^d]f\), this proves
\(\Phi_N^{\rm end}(f(\Omega_d))=\phi_N(f)\).
It is the same closing as (12), with its full scalar retained.

Multiplication of whole Hopf boxes is also exact:
\[
 \rho_N(f)\Xi_N(g)=\Xi_N(fg).
 \tag{13}
\]
One may use (13) or reconstruct the original bilinear Newton product
through \(C_N^{-1}\). Together with (12), induction through any fixed
literal Conway expression gives its original full packet and scalar.
All recorded Cartan, framing and peripheral factors remain attached.

For a local crossing factorization, restrict each displayed physical
face factor to \(\mathcal M_N\) and multiply these full \(N\)-by-\(N\)
matrices in the original order. The complete crossing is then the same
whole Hopf box as before. One must not replace an individual non-Hopf
face factor \(A\) by the polynomial packet reconstructed from \(Av_0\):
the identity \((AB)v_0=\rho_N(\Xi_N^{-1}(Av_0))Bv_0\) is not true
for arbitrary face matrices. Formula (13) applies to whole Hopf boxes.

## 4. The factorial interface is an explicit unitary diagonal

Write \(F_a=(Q;Q)_a\), \(0\le a<N\), and retain the original
marked scalar
\[
 \varpi_N=\sqrt N\exp\left\{i\pi
                \left[\frac14-\frac{N+N^{-1}}{12}\right]\right\}.
 \tag{14}
\]
The middle marked clock and the inverse clock used in the first
description are
\[
 \mathcal F_Z=\varpi_N\operatorname{diag}(F_a^{-1}),\qquad
 \mathcal F_T^{-1}=\varpi_N^{-1}\operatorname{diag}(F_b).
 \tag{15}
\]
Their clock marks and endpoint logarithmic lifts are the original
ones. Since \(b=d-a\) on \(\mathcal M_N\),
\[
 F_aF_{d-a}=N\nu_a,\qquad
 \nu_a=(-1)^aQ^{a(a+1)/2}
 \tag{16}
\]
gives the exact interface
\[
 \mathcal F_T^{-1}|_{\mathcal M_N}
       =\frac{N}{\varpi_N^2}D_\nu\,
                              \mathcal F_Z|_{\mathcal M_N}.
 \tag{17}
\]
To prove (16), use \(F_d=N\) and
\(\prod_{j=N-a}^{N-1}(1-Q^j)
       =(-1)^aQ^{-a(a+1)/2}F_a\).
All diagonal entries of \(D_\nu\) and the scalar \(N/\varpi_N^2\)
have modulus one.

The diagonal is retained as an actual finite matrix. Its continuation
satisfies \(\nu_{a+N}=-\nu_a\), so its cyclic conjugation has an
endpoint correction. In the physical middle basis,
\[
 D_\nu X D_\nu^{-1}
                  =-XZ^{-1}(I-2E_0(Z)).
 \tag{18}
\]
At input \(a\ge1\) the diagonal ratio is
\(\nu_{a-1}/\nu_a=-Q^{-a}\); at input zero it is
\(\nu_d/\nu_0=1\). This proves (18), including the wrap.
Multiplying by the actual nilpotent coefficient removes that one
reflection:
\[
 D_\nu nD_\nu^{-1}=-nZ^{-1},
 \tag{18a}
\]
because \(nE_0(Z)=0\) on this subspace. This is an exact identity
for \(n\), not permission to erase the wall in the cyclic unit \(X\).

Also \(\nu_0=\nu_d=1\). Thus the reconstructed Frobenius extension
has, for every middle-block matrix \(A\),
\[
 \Phi_N^{\rm end}(D_\nu A)
 =\Phi_N^{\rm end}(A D_\nu)
 =\Phi_N^{\rm end}(D_\nu A D_\nu^{-1})
 =\Phi_N^{\rm end}(A).
 \tag{18b}
\]
This can be used at those exterior interfaces, or with a fully
conjugated word. It does not delete an interior \(D_\nu\) from an
otherwise unchanged product, and it makes no such assertion for
the other marked cap in (12).

Unitarity in this paragraph concerns the literal physical basis
\(v_a\). The Newton-coordinate matrix \(C_N^{-1}D_\nu C_N\)
need not be unitary or uniformly conditioned. No energy estimate
is inferred from the unit-modulus diagonal alone.

## 5. Source and geometric scope

The reconstructed source (12) is used on whole Hopf boxes. It is not
the restriction of the all-array physical source
\[
 \Phi(W)=\frac1N\sum_{a,c,b}g_bW_{(c,b),(a,b)}
 \tag{19}
\]
to arbitrary face matrices, where \(g_b=(xQ^{-b})^{1-N}\).
Indeed the projector onto
\(|1,d\rangle\) has zero middle block but (19) has value \(g_d/N\ne0\).
Thus (19) cannot be recovered from a middle block on all arrays.
The Hopf reconstruction is indispensable.

Every local full-function coefficient realization remains its original
circle-minus-radial functional. Restricting a finite matrix identity
commutes with these exact finite-dimensional coefficient integrals.
It does not select one component of their cycles or replace a
full-function moment by a scalar evaluation.

The result gives an exact, smaller local representation in which the
specified first/middle wrap correction disappears, without losing
any repeated-root Casimir direction. This is a fixed-root statement,
not an off-root quantum-family identity. It neither places every geometric point
in a common positive face polarization nor proves that the turn
kernel transports a Rivin contour. The surviving first-head walls,
marked relative cycles, source coefficient, and coordinate-change
costs still require their own geometric estimates. No new volume
identity or finite-exception theorem follows here.

## Complete proof sources

All four complete matching texts were read. The first supplies the
faithful Casimir block, full Newton source and genuine turn. The next
two supply the actual face operators and marked factorials. The last
specifies the all-array source whose scope is distinguished in (19).

| Source | SHA-256 |
|---|---|
| [Newton source and physical Casimir blocks](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [First local five-point description](literal_first_full_phi_certificate.md) | 1b8a739ce096a1b2a5942ac85507aacc8f6d0c714a9e029dae0ac6492438314a |
| [Middle local five-point description](literal_middle_full_phi_certificate.md) | 85681202cfdf788e251dafa560fcaad6468c7058c00c4b1d51f3695a497282d1 |
| [Whole-word cyclic period and original source](actual_whole_word_cyclic_dilog_resolvent_period.md) | 9725d8955cb9bf4770566756eb00470d7e990c7e06b9513276509b01a037d59d |

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical calculation, build, git operation,
or earlier-final edit was performed.
