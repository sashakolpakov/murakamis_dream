# A contact term in the overlap of the first and middle face kernels

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

Two already constructed five-point identities share the same ordered
tetrahedron and its positive-quad coordinate. In their specified common
physical frame, however, their finite face kernels differ by a nonzero
matrix contact term, rather than a scalar normalization. That contact
is invisible to one original marked evaluation but becomes visible after
a cyclic face unit is inserted. The coefficient is computed exactly
below at every level.

This tests a particular proposed scalar overlap rule. It does not rule
out a richer face atlas carrying matrix transitions and boundary
sources, and it does not assert a failure of the knot invariant or its
volume conjecture.

## 1. The two kernels on the shared tetrahedron

Fix \(N\ge2\), put \(d=N-1\), and set
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad x=-q^{-1},
                    k=x^N=(-1)^{N-1}.
\]
Use the original balanced physical head basis \(e_0,\ldots,e_d\).
Its clock and a cyclic completion of its raising shift are
\[
 Z_i e_a=Q^a e_a,\qquad
 S_i e_a=e_{a+1}\ (a<d),\qquad S_i e_d=\mu_i e_0.
                                                               \tag{1}
\]
Here \(\mu_1=\mu\ne0\), \(\mu_2=k\mu\). Operators on different
heads commute. On their tensor product define
\[
 Z=Z_1,\qquad T=Z_2,\qquad X=xS_2S_1^{-1}.
\]
Thus \(XZ=QZX\), \(XT=Q^{-1}TX\), and \(X^N=1\).
Every shift in (1) has its recorded wrap factor; no physical nilpotent
matrix has been replaced by an unweighted cyclic one.

Let \(E_j(T)\) be the second-head index-\(j\) projector. The
original first-head lowering matrix gives the actual nilpotent
\[
                n=e_1S_2=(Q-Z^{-1})X,\qquad n^N=0.       \tag{2}
\]
Here the lowercase \(e_1\) in \(e_1S_2\) denotes the physical
Gauss lowering operator, not a basis vector. Equivalently, (2) and
(1) specify the matrix without that notation. It lowers the first
head by one, killing index zero, and cyclically raises the second.
Define its second-head cut by
\[
                     c=n(1-E_d(T)),\qquad c^N=0.         \tag{3}
\]
The matrix \(c\) has a strict second-head raise: its arrow out of
index \(d\) is absent.

For a nilpotent argument of order at most \(N\), write
\[
 P_Q(A)=\sum_{h=0}^d p_hA^h,\qquad
 p_h=\frac{(-1)^hQ^{h(h-1)/2}}{F_h},\qquad
 F_h=(Q;Q)_h=\prod_{j=1}^h(1-Q^j),\qquad F_0=1.        \tag{4}
\]
All denominators in (4) are nonzero. Its inverse is the finite Euler
polynomial \(\sum_{r=0}^d A^r/F_r\). Indeed the coefficient of
\(A^r\), for \(1\le r<N\), in their product is
\(\prod_{j=0}^{r-1}(1-Q^j)/F_r=0\) by the finite binomial identity. Terms of degree
at least \(N\) vanish. In particular both
\(P_Q(n)\) and \(P_Q(c)\) are invertible.

The [first literal certificate](literal_first_full_phi_certificate.md)
has ordered flags \((b,p,p_1,s_M,s_R)\), whereas the
[middle certificate](literal_middle_full_phi_certificate.md)
has \((a,b,p,p_1,s_M)\). They use the same bounded homogeneous
frame and the same four flags \((b,p,p_1,s_M)\) on the shared
tetrahedron. With their specified quad changes its coordinate is
\[
                           n_{\rm cl}=-X(1-Z)/Z.         \tag{5}
\]
In the common positive-quad orientation, the displayed Euler face
factor in the middle certificate is \(P_Q(n)\); in the first it
is \(P_Q(c)\). Formula (3) is the explicit finite difference
between these factors. We test precisely this common-frame overlap,
not an unspecified change to a future positive face polarization.
All the other adapters in the two complete crossing identities
remain part of those identities.

## 2. The overlap is a nontrivial square-zero contact

Define the common-frame ratio
\[
                 \mathcal T_{FM}=P_Q(n)P_Q(c)^{-1}=I+V.  \tag{6}
\]
Give a physical basis vector \(|a,b\rangle\) its ordinary integer
degree \(a+b\). This degree is not reduced modulo \(N\).

**Proposition 1.** The matrix \(V\) lowers this integer degree
by exactly \(N\), is nonzero, and satisfies \(V^2=0\).
Consequently (6) is not a scalar overlap.

**Proof.** The complete cut identity from the first certificate is
\[
 c^h=n^h(1-J_h),\qquad
 J_h=\sum_{j=N-h}^{N-1}E_j(T),\qquad 0\le h<N.           \tag{7}
\]
For \(h=0\) the sum is empty. It also follows directly from (1):
the forbidden inputs are precisely the second-head indices for which
\(h\) raises cross the cyclic endpoint.

Each nonzero entry of \(n^hJ_h\) lowers the first index by
\(h\), raises the second by \(h\), and wraps it once. Thus
\[
 P_Q(n)-P_Q(c)=\sum_{h=1}^d p_h n^hJ_h                 \tag{8}
\]
has integer degree \(-N\). Every power of the strict \(c\)
preserves the integer degree, as does \(P_Q(c)^{-1}\).
Equation (6) therefore gives the same degree \(-N\) for \(V\).
All physical degrees lie between zero and \(2d<2N\), so two
successive such contacts vanish: \(V^2=0\).

There is also a literal nonzero entry. On \(v=|1,d\rangle\),
\(c v=0\), and \(n^h v=0\) for \(h\ge2\). Since
\(p_1=(Q-1)^{-1}\), (1)--(4) give
\[
                  V|1,d\rangle=x\mu_2|0,0\rangle\ne0. \tag{9}
\]
Thus \(I+V\) is a nonidentity unipotent matrix. If it were scalar,
its eigenvalue would have to be one, contradicting (9).
\(\square\)

In particular the contact is not removed by comparing only the
commutative coordinates in (5). The calculation uses the full physical
tensor square, without a distinct-root or eigenline quotient.

The contact vanishes on the local ordinary cup sector: a degree-\(d\)
vector cannot be lowered by \(N\) and remain in the physical space.
This agrees with the exact identity \(c^hp=n^hp\) on the original
cup in the first certificate. It does not make (6) an all-input scalar
identity.

## 3. The same original marked functional detects its return

Keep the original normalized averaged first-cut functional from the
[whole-word period theorem](actual_whole_word_cyclic_dilog_resolvent_period.md),
with two heads:
\[
 \Phi_N(W)=\frac1N\sum_{a,a',b=0}^d
                    g_b W_{(a',b),(a,b)},\qquad
                         g_b=(xQ^{-b})^{1-N}.            \tag{10}
\]
This is the specified original rank-one first-cut coupon and original
pivotal second-head trace. It is fixed on all inserted arrays below.
No equality of different cut conventions on scalar knot endomorphisms
is applied after insertion.

**Proposition 2.** For every \(N\ge2\) and every permitted nonzero
wrap mark,
\[
 \boxed{\quad
       \Phi_N(V)=0,\qquad
       \Phi_N(X^{-1}V)=\frac{Qg_d}{Q-1}\ne0.
       \quad}                                             \tag{11}
\]

**Proof.** Expand (8) times the inverse polynomial in (4).
A term with exponents \(h\ge1\) and \(r\ge0\) lowers the
first head by \(\ell=h+r\) and shifts the second cyclically by
\(\ell\). Terms with \(\ell\ge N\) vanish by first-head
nilpotence. The second-head trace in (10) therefore kills every term
of \(V\), since \(1\le\ell<N\).

After left multiplication by \(X^{-1}\), the second shift is
\(\ell-1\). Its trace can be nonzero only for \(\ell=1\).
Thus only \(h=1,r=0\) survives, with coefficient \(p_1\).
The exact Weyl relation and (2) give
\[
             X^{-1}nE_d(T)=Q(1-Z^{-1})E_d(T).             \tag{12}
\]
This diagonal matrix has the marked value
\[
 \Phi_N\bigl(Q(1-Z^{-1})E_d(T)\bigr)
       =\frac{Qg_d}{N}\sum_{a=0}^d(1-Q^{-a})=Qg_d.
\]
Multiplying by \(p_1\) proves (11). Every cyclic wrap cancels in
(12), so the answer is independent of \(\mu\).
\(\square\)

The same second-head trace gives \(\Phi_N(X^{-1})=0\).
Consequently no scalar \(\lambda\) can replace \(I+V\) by
\(\lambda I\) while preserving the specified marked evaluations
for both the identity exterior and the left face unit \(X^{-1}\).
The source-null space exposed by the first equality of (11) is not
stable under that face unit.

The return coefficient is explicitly polynomial in size. Since
\(|g_d|=1\) and \(|1-Q|=2\sin(\pi/N)\),
\[
 \frac{N}{2\pi}\le |\Phi_N(X^{-1}V)|\le\frac N4.        \tag{13}
\]
This is not an estimate of a whole word with other exponential
factors. A local polynomial-size calculation does not authorize
discarding the contact in such a word.

Here \(X^{-1}\) is the actual cyclic face-coordinate unit used in
the literal flag constructions. We do not claim that this insertion
is a whole physical knot exterior, or that (11) is a new knot example.
It tests the original marked functional on an explicitly permitted
matrix adapter, which is the overlap question at issue.

## 4. The relative coefficient cycle and the geometric limitation

The coefficients in (4) are the same finite Euler coefficients used
in the two literal full-Phi certificates. Their full-function
realizations are the complete circle-minus-radial coefficient
functionals, with the recorded root orientation and logarithmic mark.
Equations (6)--(12) are identities of those finite matrices before
any period approximation. Inserting their exact full-Phi realizations
therefore retains every circle and radial component in its original
order. In particular \(p_1\) in (11) is the exact coefficient;
it has not been replaced by a bare circle moment.

The conclusion is specific. The first and middle common-frame face
factors cannot be glued by declaring their discrepancy a scalar line
factor. Matrix contact transport and its source functional have to
remain, or a different explicitly source-preserving face transform
has to remove them. The result does not exclude all possible positive
face polarizations or a refined operator-valued atlas.

Nor does the physical degree \(-N\) identify this contact with a
boundary face of a correctly marked Rivin angle polytope. The geometric
edge gluing rows have not been identified with these physical degree
rows. In particular, no claim is made that the contact has a boundary
volume gap, or that it is a particular wrong-edge integer alias.
Those assertions require the actual gluing dictionary. The contact
in (8) also retains all bulk values of \(h\), rather than only its
first endpoint coefficient. There is no new geometric lower bound or
short-filling volume identity here.

## Complete direct sources

All three complete matching texts were read:

| Source | SHA-256 |
|---|---|
| [Literal first face certificate](literal_first_full_phi_certificate.md) | 1b8a739ce096a1b2a5942ac85507aacc8f6d0c714a9e029dae0ac6492438314a |
| [Literal middle face certificate](literal_middle_full_phi_certificate.md) | 85681202cfdf788e251dafa560fcaad6468c7058c00c4b1d51f3695a497282d1 |
| [Original whole-word source functional](actual_whole_word_cyclic_dilog_resolvent_period.md) | 9725d8955cb9bf4770566756eb00470d7e990c7e06b9513276509b01a037d59d |

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation,
or edit to a previous final was performed.
