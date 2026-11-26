# The exact doubled grid for a half-step of the outer operator

Private exact-source deduction, 9 November 2026. The two oriented
principal factors require a square root of the original shift character.
A literal half-step does not act on the original Hermite quotient. It
does act on a specified doubled angular algebra, whose reflection
invariants are the product of the original and opposite spectral
quotients. The endpoint multiplicities and the additional forcing of
the canonical complete inner source can both be computed exactly.

This proves a finite algebra in which a proposed half-step construction
could be tested. It does not factor the original operator, descend an
oriented factor to the original source, or improve an observation bound.
No mathematical numerical evaluation or frozen-source change is used.

## 1. Original convention and the half-step obstruction

Let
\[
 N\ge3,\qquad \theta=\pi/N,\quad q=e^{i\theta},\quad
 \epsilon=(-1)^N,\quad \eta=(-1)^{N-1}=-\epsilon,
 \quad X(\zeta)=-\zeta-\zeta^{-1},\qquad
 P_N(X)=2T_N(X/2)+2.
\tag{1}
\]
Thus \(\zeta=e^{iu}\) and \(X=-2\cos u\). The original algebra
is \(\mathcal A_N=\mathbb C[X]/(P_N)\). Its original
Askey--Wilson operators use the shifts \(u\mapsto u\pm2\theta\),
as in [current-free crossing transport, (3),(6)](research_current_free_aw_crossing_transport.md).

The Chebyshev identity gives the following Laurent identities:
\[
\begin{split}
 P_N(X(\zeta))
   &=\epsilon\zeta^{-N}(\zeta^N+\epsilon)^2,\\
 P_N(X(\zeta))-4
   &=\epsilon\zeta^{-N}(\zeta^N-\epsilon)^2,\\
 P_N(X(\zeta))\bigl(P_N(X(\zeta))-4\bigr)
   &=\zeta^{-2N}(\zeta^{2N}-1)^2.
\end{split}
\tag{2}
\]
Indeed \(2T_N(X(\zeta)/2)=\epsilon(\zeta^N+\zeta^{-N})\).
Since \(q^N=-1\), the literal half-step obeys
\[
                  P_N(X(q\zeta))=4-P_N(X(\zeta)).
\tag{3}
\]
It therefore exchanges the original spectral level zero with level
four. In particular substitution \(\zeta\mapsto q\zeta\) does not
preserve the original angular ideal
\(((\zeta^N+\epsilon)^2)\), and it does not induce an endomorphism
of \(\mathcal A_N\). This is an exact ideal obstruction, including
the repeated roots, rather than a comparison of node sets only.

## 2. The doubled angular algebra and its reflection invariants

Define
\[
 \mathcal B_N=
  \mathbb C[\zeta,\zeta^{-1}]/((\zeta^{2N}-1)^2),
 \qquad
 \tau f(\zeta)=f(q\zeta),\qquad sf(\zeta)=f(\zeta^{-1}).
\tag{4}
\]
Both maps are exact algebra automorphisms of \(\mathcal B_N\), and
\[
       \tau^{2N}=s^2=I,\qquad s\tau s=\tau^{-1}.
\tag{5}
\]
The two coprime factors give a Chinese-remainder decomposition
\[
 \mathcal B_N\simeq\mathcal B_N^{\rm orig}\oplus
                         \mathcal B_N^{\rm opp},\qquad
 \mathcal B_N^{\rm orig}
   =\frac{\mathbb C[\zeta^{\pm1}]}{((\zeta^N+\epsilon)^2)},\quad
 \mathcal B_N^{\rm opp}
   =\frac{\mathbb C[\zeta^{\pm1}]}{((\zeta^N-\epsilon)^2)}.
\tag{6}
\]
Reflection preserves the two summands. The half-step interchanges
them, and its square preserves each.

**Theorem 1.** Pullback by \(X=-\zeta-\zeta^{-1}\) gives exact
isomorphisms
\[
\boxed{\quad
 \mathcal B_N^s\simeq
   \frac{\mathbb C[X]}{(P_N(X)(P_N(X)-4))}
   \simeq\mathcal A_N\oplus\mathcal A_N^{\rm opp},\qquad
 \mathcal A_N^{\rm opp}=\frac{\mathbb C[X]}{(P_N-4)}.
\quad}
\tag{7}
\]
Under (7), \((\mathcal B_N^{\rm orig})^s=\mathcal A_N\) and
\((\mathcal B_N^{\rm opp})^s=\mathcal A_N^{\rm opp}\).

*Proof.* An invariant class in \(\mathcal B_N\) has an invariant
Laurent representative: average any representative with its reflection.
Every invariant Laurent polynomial is a polynomial in
\(\zeta+\zeta^{-1}=-X\). It remains to determine the kernel.

At each \(2N\)-th root \(\zeta_0\ne\pm1\), the coordinate map
\(X(\zeta)\) has nonzero derivative. Divisibility by
\((\zeta^{2N}-1)^2\) therefore requires a spectral zero of order two
at the image of the pair \(\zeta_0,\zeta_0^{-1}\). At either fixed
point \(\zeta_0=\pm1\), the function \(X-X(\zeta_0)\) has order
two, so exactly a simple spectral zero is required. The polynomial
\(P_N(P_N-4)\) has these same multiplicities by (2). Its degree
is \(2N\): there are \(N-1\) interior double roots and the two
simple roots \(-2,2\). This proves the kernel assertion. The same
argument for either factor in (6) proves its invariant statement.
The spectral factors are coprime because their difference is four,
which proves the last decomposition in (7). \(\square\)

This also describes all endpoint jets. In the local length-two
angular algebra at \(\zeta_0=\pm1\), reflection negates the first
local coordinate; its invariant subalgebra consists only of the
constant. There is no first spectral normal at that simple endpoint.
At an interior pair, the invariant local algebra has a value and a
first spectral normal, related to the angular derivative by
\[
 \frac{d}{du}f(-2\cos u)=2\sin u\,f'(-2\cos u).
\tag{8}
\]
Thus the construction retains the full original Hermite data.
Explicitly, its spectral multiplicities at both parities are
\[
\begin{array}{c|c|c}
 &\mathcal A_N&\mathcal A_N^{\rm opp}\\ \hline
 N=2m &m\text{ double roots, no endpoints}
      &(m-1)\text{ double roots and simple }-2,2\\
 N=2m+1 &m\text{ double roots and simple }-2
      &m\text{ double roots and simple }2.
\end{array}
\tag{9}
\]

The spectral idempotents are particularly simple:
\[
 e_{\rm orig}=1-P_N/4,\qquad e_{\rm opp}=P_N/4,
 \qquad e_{\rm orig}e_{\rm opp}=0,
 \qquad \tau e_{\rm orig}=e_{\rm opp}.
\tag{10}
\]
These identities hold in \(\mathcal B_N\), where \(P_N^2=4P_N\).

The doubled algebra is a half-step module, but its invariant subring
is not a half-step module by itself. In fact, for \(sf=f\),
\[
                   s\tau f=\tau^{-1}f.
\tag{11}
\]
Thus \(\tau f\) is invariant precisely when \(\tau^2f=f\).
For example \(X(q\zeta)\) is not invariant for \(N\ge3\).
The combinations \(\tau+\tau^{-1}\) do preserve invariants;
a single oriented half-step does not. This reflection issue is
separate from the exchange of the two grids.

## 3. Why an oriented factor does not belong to the old scalar shift algebra

Use \(z=e^{iu}\), \(w=e^{i\pi t}\), \(v=w^2\) for the principal
symbol variables in the [degree-eleven factor theorem](research_mixed_next_outer_degree_eleven_factors.md).
Here its \(z\) is angular, and is distinct from the spectral
coordinate \(X\) above. Retain that theorem's explicit polynomial
\(B(z,v)\) and factors
\[
 \mathscr F_\pm(z,w)=B(z,w^2)\mp2w^3z^4(z-1)^3,
 \quad
 a_+=w^{-3}z^{-6}\mathscr F_+,
 \quad a_-=w^{-3}z^{-5}\mathscr F_-.
\tag{12}
\]
Thus
\[
 a_+=w^{-3}z^{-6}B(z,w^2)-2z^{-2}(z-1)^3,
 \qquad
 a_+(z,-w)=-z^{-1}a_-(z,w).
\tag{13}
\]
The first term in (13) is odd in \(w\), and the second is even;
both are nonzero Laurent polynomials. In particular \(a_+\) does
not descend to a Laurent polynomial in \(v=w^2\). The same is
true of \(a_-\). Multiplication by any monomial \(z^j w^k\)
does not remove this mixed parity.

A scalar operator made from a fixed finite number of the original
integer shifts has symbol \(\sum_j b_j(u)v^j\). This remains true
for fixed finite words in the original Askey--Wilson operators and
scalar multiplication, whenever their principal coefficient limit
is taken. Hence neither specified oriented factor, with any monomial
normalization, is the principal symbol of such an old scalar word.

This assertion is only about that fixed-width scalar class. It does
not exclude an operator on the doubled algebra, a matrix factorization,
a nonlocal map, or a degree growing with \(N\). In particular the
existence of an algebraic square root of a finite matrix would not
supply the missing local source identity. Equations (4)--(11) give
an exact enlarged algebra in which that identity could be sought.

## 4. The canonical complete source on the opposite grid

Let \(D=N-1\), \(\kappa=q^{D^2/2}\), and retain the canonical
ordinary representative
\[
 Q_N^{\rm full}=T(R^3F_N),\qquad
 F_N(X)=K_N^{\rm ord}(-2,X),\qquad \deg Q_N^{\rm full}\le D.
\tag{14}
\]
All scalars, the complete kernel, and the full first normals are
those of the [seven-term source recurrence](research_mixed_next_physical_inner_seven_term_recurrence.md).
Its ordinary operator is
\[
 \mathcal D_{3,N}
  =q^{-2}(\mathcal L^2-I)\mathcal L_1
       +q^{-3}\mathcal L X-8q^{-2}\mathcal L
                         +(8q^{-1}+2)I.
\tag{15}
\]
Here \(X\) denotes multiplication and products are ordered.

**Proposition 2.** The exact ordinary defect is
\[
\boxed{\quad
 \mathcal D_{3,N}Q_N^{\rm full}(X)
   =-\frac{\eta\kappa^3}{N^2}
                     \bigl(P_N(-2)+P_N(X)\bigr).
\quad}
\tag{16}
\]
Consequently it is \(\mathfrak f_N\) on the original full quotient
and \(\mathfrak f_N+4\rho_N\) on the opposite full quotient, where
\[
 \rho_N=-\eta\kappa^3/N^2,\qquad
 \mathfrak f_N=-\eta\kappa^3P_N(-2)/N^2,
\quad
 \mathfrak f_N+4\rho_N=
 \begin{cases}
 8\kappa^3/N^2,&N\text{ even},\\
 -4\kappa^3/N^2,&N\text{ odd}.
 \end{cases}
\tag{17}
\]

*Proof.* The cited source, (5)--(7), proves the ordinary identity
\(\mathcal D_{3,N}Q_N^{\rm full}=\mathfrak f_N+\rho_NP_N\)
with scalar \(\rho_N\). Indeed \(\mathcal L\) preserves ordinary
degree and \(\mathcal L_1\) raises it by at most one, so the left
side has degree at most \(N\).

The original ordinary operators have leading terms
\[
 \mathcal L(X^k)=c_kX^k+O(X^{k-1}),\qquad
 \mathcal L_1(X^k)=-q^{2k+2}X^{k+1}+O(X^k),\qquad
 c_k=q^{2k+1}+q^{-2k-1}.
\tag{18}
\]
The second formula is also recorded in
[finite Newton remainder, (6)](research_mixed_next_outer_finite_newton_remainder.md).
Both follow directly, throughout the range \(N\ge3\) used here,
from the original angular formula, whose limits are
\(A\to-q^{-1}\), \(C\to-q\), \(c_0+A+C\to0\)
as \(\zeta\to\infty\). The two unweighted shifted terms give
the displayed \(c_k\). In \(\mathcal L_1\), only
\(-qC\zeta f(q^2\zeta)\) reaches degree \(k+1\); using
\(X\sim-\zeta\) gives \(-q^{2k+2}\). The first formula works
also at \(k=N\).
Since \(q^{2N}=1\) and \(c_N=c_0\), (15) has degree-\(N\)
coefficient on \(X^D\) equal to
\[
       -q^{-2}(c_0^2-1)+q^{-3}c_0=-1.
\tag{19}
\]
No lower input degree reaches \(N\). As \(P_N\) is monic,
\(\rho_N=-[X^D]Q_N^{\rm full}\).

The leading coefficient of the original complete source is exact.
Use \(\phi_N(f)=\eta N^2[X^D]\operatorname{rem}_{P_N}f\),
the self-adjointness of \(T\), \(T1=e_D\), and the original
socle identities \(R^3e_D=\kappa^3e_D\),
\(F_Ne_D=F_N(c_0)e_D\). Here
\(F_N(c_0)=1\), because every Newton polynomial \(e_j(c_0)\)
with \(j>0\) vanishes. Also \(\phi_N(e_D)=1\): its leading
coefficient is \(\eta/N^2\), using the full product \(S_D=N\).
It follows that
\[
 \phi_N(Q_N^{\rm full})
   =\phi_N(R^3F_Ne_D)=\kappa^3,
 \qquad [X^D]Q_N^{\rm full}=\eta\kappa^3/N^2.
\tag{20}
\]
This proves (16). Finally \(P_N(-2)=2(-1)^N+2\) gives (17).
All identities preceding the last evaluation are ordinary polynomial
or full-quotient identities, so their reductions retain every
required first normal. \(\square\)

In fact the original ordinary \(\mathcal L_n\) preserve both
spectral ideals: \(P_N(X(q^{\pm2}\zeta))=P_N(X(\zeta))\),
and therefore
\(\mathcal L_n((P_N-c)f)=(P_N-c)\mathcal L_nf\) for
\(c=0,4\). Thus (16) is a genuine equation on each spectral
factor of (7), not an assignment at isolated values.

This statement uses the grouped ordinary polynomial operators. Their
separated rational shift coefficients have poles whose removal uses
evenness. We have not extended those separated terms, or the grouped
Askey--Wilson operators, to every non-even element of \(\mathcal B_N\).
Any proposed half-step factor with rational coefficients must prove
its own regularity on its stated domain.

## 5. The remaining source-descent problem

The ordinary representative (14) supplies a specified lift to the
doubled invariant algebra. The source term on its opposite factor
is explicitly nonzero at both parities and has the same polynomial
order as the original even forcing. It must be retained in any
half-step transport. Its small scalar size alone does not bound the
opposite-grid solution or an observation of that solution.
More generally, (16) has modulus at most \(8/N^2\) on the entire
real angular circle, because \(0\le P_N(-2\cos u)\le4\) there
and \(|\kappa|=1\). This is a forcing bound, not an inverse bound.

An arbitrary class in \(\mathcal A_N\) does not determine an
opposite-grid class without a choice of lift: replacing an ordinary
representative by \(f+P_Ng\) changes that opposite class by \(4g\).
The canonical representative in (14) fixes this choice for the actual
source. It does not give an oriented factorization of (15) or of the
grouped adjoint \(\mathcal C_N\), nor does (11) give such a factor
on even tests.

Accordingly, a finite use of the favorable oriented principal roots
still requires an explicit operator and source identity on this cover
or another specified module, followed by descent with the original
trace, all normals, both grid forcings and the original even symmetry.
The present result supplies that algebra and the complete source
defect; it makes no cancellation or finite-exception claim.
