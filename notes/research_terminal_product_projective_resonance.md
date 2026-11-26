# Projective resonance of terminal products under an outer unit turn

Private written proof, 16 November 2026.

For a product of signed terminal characteristic components, the points
at old spectral infinity that map to a finite new physical color are
classified by a signed reciprocal sum. Their phases, normalization
branches and retained double-normal multiplicities can be counted
exactly. The inverse-pullback convention for an actual outer turn is
essential.

This is a statement about the characteristic correspondence. It does
not assert that an actual source participates on any of its branches,
or that a cleared finite matrix has a regular leading coefficient.

## 1. Characteristic coordinates and the actual turn convention

Write \(C\) for the old spectral coordinate and choose the angular
lift \(v+v^{-1}=C\). Near \(C=\infty\), choose the sheet
\[
                    v=C+O(C^{-1}).
 \tag{1}
\]
Set
\[
 g(C)=\frac{C-2}{C+2},\qquad b(C)=\frac8{C+2}.
 \]
For a nonzero full physical shift \(t\), the original commuting
symbols of \(J,D_1\) are
\[
 y=b+g(t+t^{-1}),\qquad
 z=b-g(v^{-1}t+vt^{-1}).
 \tag{2}
\]
These are the physical-value symbols, not the Newton-coefficient
shift symbols. They lie on the original cubic
\[
 C^2+y^2+z^2+Cyz-8(C+y+z)+28=0.
 \tag{3}
\]
Let \(x_n\) denote the symbol of \(D_n\), with
\[
 x_0=C,\quad x_1=z,\quad
 x_{n+2}=8-yx_{n+1}-x_n\qquad(n\in\mathbb Z).
 \tag{4}
\]
The maps
\[
 \mathcal A_n(C,y,z)=(x_n,y,x_{n+1})
 \tag{5}
\]
are polynomial automorphisms of (3), with
\(\mathcal A_n\mathcal A_m=\mathcal A_{n+m}\).
This follows either from the recurrence or from the original
operator conjugation \(V_nCV_{-n}=D_n,\ V_nJ=JV_n\).

For clarity, an actual outer \(U_\sigma=V_\sigma\),
\(\sigma=\pm1\), transports an old equation \(P=0\) to
\(P\circ\mathcal A_\sigma=0\). Therefore its action on
characteristic points is
\[
                 \text{new}=\mathcal A_{-\sigma}(\text{old}).
 \tag{6}
\]
In particular its new spectral coordinate is \(x_{-\sigma}\),
not \(x_\sigma\). Put
\[
 \Phi_\epsilon(C,t)
    =b(C)-g(C)(v^{-\epsilon}t+v^\epsilon t^{-1}),
                  \qquad \epsilon=\pm1.
 \tag{7}
\]
Here \(\Phi_+=x_1\), and \(\Phi_-=x_{-1}\); the latter follows
from \(x_{-1}=8-yC-z\). Thus an actual outer \(U_\sigma\)
uses \(\Phi_{-\sigma}\).

This sign is checked by one factor: \(U_{-1}V_1=I\), so the
positive unit terminal component must contract to the original
endpoint \(C_{\rm new}=2\) under the negative outer turn.

## 2. Labeled terminal products and the statement

For \(m\ge0\) define
\[
 f_0(y)=2,\quad f_1(y)=4-y,\quad
 f_{m+1}(y)=8-yf_m(y)-f_{m-1}(y).
 \tag{8}
\]
The pinned terminal theorem gives the reduced component \(x_n=2\):
\[
 \begin{array}{lll}
 n=m>0:& C=f_m(y),& z=f_{m-1}(y),\\
 n=-m<0:& C=f_m(y),& z=f_{m+1}(y).
 \end{array}                                             \tag{9}
\]
In particular \(f_m\) has degree \(m\) and leading coefficient
\((-1)^m\).

Fix \(r\ge1\) signed nonzero integers \(n_i\). Write
\[
 m_i=|n_i|,\quad \varepsilon_i=\operatorname{sign}(n_i),
 \quad L=\operatorname{lcm}(m_1,\ldots,m_r),\quad
 M=\prod_i m_i,\quad \gamma=\sum_i\frac1{n_i}.
 \tag{10}
\]
The **labeled reduced product correspondence** has the common
coordinate \(C\) and independent coordinates \(y_i\) satisfying
\[
                         f_{m_i}(y_i)=C .
 \tag{11}
\]
For each factor use its signed \(z_i\) from (9), and obtain
its shift \(t_i\) from (2). Its product shift is
\[
                              T=\prod_i t_i .
 \tag{12}
\]
This is the principal full-step tensor rule for ordinary
multiplication. Repeated factors remain labeled. Distinct
labeled branches may have the same product or image; they
are not identified in the counts below.

Normalize the reduced correspondence near the chosen point
\(v=\infty\) of the angular lift. A branch at infinity means
a point of that normalization over \(C=\infty\).

**Theorem 1.** The following statements hold.

1. There are exactly \(M/L\) labeled normalization branches
   at old infinity. On each, \(C\) has pole order \(L\).
   On the common cover \(C=u^{-L}\), label the factor roots
   by \(\zeta_i\in\mu_{m_i}\). Then
   \[
    t_i=-\zeta_i^{\varepsilon_i}
                   C^{1/n_i}(1+o(1)),\qquad
    T=aC^\gamma(1+o(1)),\qquad
    a=(-1)^r\prod_i\zeta_i^{\varepsilon_i}.
    \tag{13}
   \]
   The expansions are convergent Laurent/Puiseux expansions.

2. For the algebraic map \(\Phi_\epsilon\), a branch has
   finite new spectral limit if and only if
   \[
                              \gamma=\epsilon.
    \tag{14}
   \]
   Otherwise \(\Phi_\epsilon\) has pole order
   \(L|\gamma-\epsilon|\) on every normalization branch.
   For the actual outer \(U_\sigma\), (14) is
   \[
                       \boxed{\ \gamma=-\sigma\ }.
    \tag{15}
   \]

3. In the resonant case the phase is constant on each
   normalization branch and ranges over exactly \(-\mu_L\).
   Every phase occurs on precisely \(M/L^2\) labeled
   normalization branches. In particular \(L^2\) divides \(M\).
   The finite physical limits are exactly
   \[
                   \boxed{\ 2\cos(2\pi k/L),\quad
                                  0\le k<L.\ }
    \tag{16}
   \]
   There are \(M/L^2\) branches over \(+2\), and also over
   \(-2\) when \(L\) is even. Each distinct interior value
   in (16) has \(2M/L^2\) branches. There is no branch over
   \(-2\) when \(L\) is odd.

4. Thus an actual outer \(U_\sigma\) has a point at old
   infinity over the new physical interior \((-2,2)\)
   exactly when
   \[
                 \boxed{\ \sum_i1/n_i=-\sigma
                         \quad\hbox{and}\quad L\ge3.\ }
    \tag{17}
   \]
   These counts concern the labeled normalization. They
   are not contact orders, numbers of distinct image
   curves, or quantum source coefficients.

### Proof of the Puiseux and sign assertions

Put \(C=u^{-L}\) and \(y_i=u^{-L/m_i}Y_i\). Multiplying
(11) by \(u^L\) gives at \(u=0\)
\[
                        (-1)^{m_i}Y_i^{m_i}=1.
 \]
Its \(m_i\) roots \(Y_i=-\zeta_i\) are simple. The analytic
implicit-function theorem gives convergent solutions
\[
               y_i=-\zeta_i C^{1/m_i}+O(1).
 \tag{18}
\]
For positive \(n=m\), solving the linear equations (2)
gives
\[
 t=\frac{z+v y-(1+v)b}{g(v-v^{-1})}.
 \tag{19}
\]
On (9), \(z=O(y^{m-1})\), with \(z=2\) when \(m=1\);
also \(C=f_m(y)\), \(v\sim C\), \(g\to1\), \(b\to0\).
Equation (19) yields \(t/y\to1\).
The signed negative terminal equation is obtained from
the positive one by \(t\mapsto t^{-1}\). Indeed \(y\)
is unchanged, \(\Phi_+(C,t^{-1})=\Phi_-(C,t)\), and
the recurrence (4) then gives
\(x_{-m}(C,t)=x_m(C,t^{-1})\).
Hence the negative shift is the reciprocal of the positive
shift at the same \(y\) branch. This proves (13), including
its phase and sign.

The roots in (18), and the rational expression (19), are
meromorphic in \(u\). Their leading coefficients are nonzero.
Thus all the limits used here belong to actual local
algebraic branches, not just formal balances.

On a loop around \(C=\infty\), the labels are permuted by
\[
        (\zeta_i)_i\longmapsto
              (\zeta_i e^{2\pi i/m_i})_i ,
 \tag{20}
\]
up to reversing the chosen orientation of the loop.
This permutation has order \(L\) and acts freely: a power
fixes a tuple exactly when it is divisible by every \(m_i\).
There are \(M\) tuples, so the number of local normalization
branches is \(M/L\), each with ramification index \(L\)
over \(C\). Equivalently \(\gcd_i(L/m_i)=1\), which shows
that \(u\) is a primitive local parameter on each orbit.

For \(\Phi_\epsilon\), let \(B=T/v^\epsilon\). By (1),(13),
\[
                    B=aC^{\gamma-\epsilon}(1+o(1)),
 \qquad \Phi_\epsilon=b-g(B+B^{-1}).
 \tag{21}
\]
If \(\gamma-\epsilon>0\), the term \(-B\) gives a pole
of order \(L(\gamma-\epsilon)\), with nonzero leading
coefficient \(-a\). If it is negative, \(-B^{-1}\) gives
the stated pole and coefficient \(-a^{-1}\).
The exponents have opposite signs, so they cannot cancel.
If \(\gamma=\epsilon\), \(B\) is an analytic unit with
limit \(a\), and
\[
                         \Phi_\epsilon(\infty)=-(a+a^{-1}).
 \tag{22}
\]
This proves parts 1--2.

### Proof of the phase and branch counts

The signed product homomorphism
\[
 \prod_i\mu_{m_i}\longrightarrow\mu_L,\qquad
              (\zeta_i)\longmapsto\prod_i\zeta_i^{\varepsilon_i}
 \tag{23}
\]
is onto: its images generate the subgroups \(\mu_{m_i}\),
whose joint order is \(L\). Equivalently, its integer
exponents \(\varepsilon_iL/m_i\) have gcd \(1\).
Each phase fiber has \(M/L\) tuples.

The deck generator (20) multiplies \(a\) by
\(\exp(2\pi i\gamma)\). Under (14), this is \(1\).
Thus each phase fiber contains whole free deck orbits
of size \(L\), proving the exact count \(M/L^2\) and
its integrality. This also proves the count is positive;
there is no divisibility assumption being imposed separately.

The phase image initially is \((-1)^r\mu_L\).
If \(L\) is even, \(-1\in\mu_L\), so this is \(-\mu_L\).
If \(L\) is odd, every \(L/m_i\) is odd. Reducing the
resonance identity
\[
                 \sum_i\varepsilon_i L/m_i=\epsilon L
 \tag{24}
\]
modulo \(2\) shows that \(r\) is odd. The image is again
\(-\mu_L\). Substitute \(a=-e^{2\pi ik/L}\) into (22)
to obtain (16).

The phase \(a=-1\) always occurs and gives \(+2\).
The phase \(a=1\) occurs exactly when \(L\) is even and
gives \(-2\). Every other value has exactly two phases,
\(a,a^{-1}\); distinct inverse pairs give distinct real
cosines. This proves all counts and (17). \(\square\)

The opposite angular sheet \(v\sim C^{-1}\) replaces all
shifts by their reciprocals. It is the inversion identification
of the same spectral correspondence, not an extra factor of
two in the counts.

## 3. Double normals, contraction and the meaning of multiplicity

The reduced counts do not delete the original normal channel.
At a generic point of the punctured neighborhood of infinity,
each signed terminal factor has local algebra
\(\mathbb C[\epsilon_i]/(\epsilon_i^2)\), over the field of
the chosen reduced branch. To check the extension of the
pinned double-root statement to this neighborhood, use
\[
 C=f_m(y)+\delta U_{m-1}(-y/2),\qquad \delta^2=0.
 \tag{25}
\]
Both \(f_m'(y)\) and \(U_{m-1}(-y/2)\) are nonzero for
large \(y\). The physical parametrization (2) is nonsingular
away from \(C=\pm2\). Hence the physical shift remains an
actual double local coordinate, exactly as in the pinned
terminal proof.

Let \(\mathbb K\) be the field of meromorphic germs on the
chosen reduced branch. For the labeled tensor product, the
local normal algebra is
\[
 \mathcal R=\mathbb K[\epsilon_1,\ldots,\epsilon_r]/
                     (\epsilon_1^2,\ldots,\epsilon_r^2),
                  \qquad \dim_{\mathbb K}\mathcal R=2^r,
 \tag{26}
\]
over that branch field. One can normalize the coordinates
so that \(t_i=t_{i,\rm red}(1+\epsilon_i)\). Then
\[
 \frac{T}{T_{\rm red}}=\prod_i(1+\epsilon_i)
                 =\exp\left(\sum_i\epsilon_i\right).
 \tag{27}
\]
The product-shift characteristic polynomial on this local
regular representation is
\((\lambda-T_{\rm red})^{2^r}\).
Its minimal nilpotent order is \(r+1\), because
\((\sum_i\epsilon_i)^r=r!\prod_i\epsilon_i\ne0\), while
the next power is zero. Thus \(2^r\) is the retained
scheme length, not a claim of one Jordan chain of that size.

The branch count \(M/L\), old ramification index \(L\),
and generic tensor length \(2^r\) are separate quantities.
Their product is \(M2^r\), the degree of the labeled
terminal tensor characteristic over a generic old \(C\).
Coincident products or image curves can combine these
labeled contributions. Taking a reduced image would lose
this bookkeeping, and cannot be used to select a source.

There is also an exact formula for the new projection
on every reduced resonant branch. With \(B=T/v^\epsilon\),
\[
 \boxed{\quad
       \Phi_\epsilon=2-g(C)\frac{(B+1)^2}{B}.
 \quad}                                                   \tag{28}
\]
It follows directly from \(b-2=-2g\).
If \(B\not\equiv-1\) and its limiting phase is \(-1\),
the contact order with \(C_{\rm new}=2\) is twice the
zero order of \(B+1\) in the local parameter \(u\).
If \(B\equiv-1\), the entire reduced branch contracts
identically to \(C_{\rm new}=2\).
More generally contraction to any specified constant \(c_*\)
means the exact identity
\[
                  g(C)(B+1)^2/B\equiv 2-c_* ,
 \tag{29}
\]
not merely the phase condition (22). Theorem 1 counts
domain branches and finite limits, not such contact orders
or distinct nonconstant image branches.

Two general exact checks show why contraction cannot be
ignored.

First, for a unit factor the terminal shift is
\[
                         t_{+1}=-v,\qquad t_{-1}=-v^{-1}.
 \tag{30}
\]
Indeed \(\Phi_+(C,t)=2\) is
\((t+v)^2=0\) up to a nonzero generic coefficient;
the negative identity follows by reciprocity.
If all active powers are units and \(\gamma=\epsilon\),
then \(r\) is odd and \(T=-v^\epsilon\).
Every reduced resonant branch in that case contracts to \(2\).
For the actual outer turn this is consistent with
\(U_\sigma V_{-\sigma}=I\).

Second, for any fixed \(m\ge1\), the product of all \(m\)
distinct reduced \(+m\) terminal shifts at the same old
color is exactly
\[
                  \prod_{\ell=1}^m t_{\ell,+m}=-v,
       \qquad \prod_{\ell=1}^m t_{\ell,-m}=-v^{-1}.
 \tag{31}
\]
For a proof, the recurrence (4) and (2) give the extreme
coefficients of \(x_m-2\) as
\[
                   [t^m](x_m-2)=(-g)^m/v,\qquad
                   [t^{-m}](x_m-2)=(-g)^m v .
 \tag{32}
\]
After multiplication by \(t^m\), the product of its
\(2m\) roots is \(v^2\). Each reduced root is double,
so the square of the reduced product is \(v^2\).
Its infinity asymptotic, using all phases in \(\mu_m\),
is
\[
                 \prod_{\zeta\in\mu_m}(-\zeta C^{1/m})
                                  =-C\sim-v .
 \]
This fixes the sign and proves the first identity in (31);
the second is its reciprocal. Choosing a complete set of
these roots among repeated labeled factors therefore
produces contracted components, without using \(m=1\).
The identities do not assert their coefficient in a finite
source.

## 4. A general exclusion criterion

For a specified active product and an actual outer \(U_\sigma\),
Theorem 1 gives an exact support criterion: all old-infinity
points over the new physical interior are absent if and only if
\[
            \sum_i1/n_i\ne-\sigma
               \quad\hbox{or}\quad
            \operatorname{lcm}_i|n_i|\le2 .
 \tag{33}
\]
If one also permits the separate source branch \(J=2\)
at an input, its reduced physical shift is \(1\), by (2).
It contributes neither a reciprocal slope nor a phase.
Consequently a finite union of terminal/source choices
has no such interior points exactly when every nonempty
active subset \(S\) satisfying
\[
                         \sum_{i\in S}1/n_i=-\sigma
 \tag{34}
\]
has \(\operatorname{lcm}_{i\in S}|n_i|\le2\).
The empty subset has slope zero and is never resonant.
Any additional nilpotent multiplicities of a source block
leave this reduced support test unchanged.

Useful sufficient conditions requiring no subset enumeration are:

* all active powers have the same sign as the outer \(\sigma\);
* the opposite-sign reciprocal budget is strictly less than one,
  \[
                     \sum_{\sigma n_i<0}|n_i|^{-1}<1;
    \tag{35}
  \]
* all possible active magnitudes are at most two, if only
  interior old-infinity points are to be excluded.

The first is contained in the second. To prove (35), multiply
(34) by \(-\sigma\). Opposite-sign factors contribute
positively, same-sign factors negatively. The total cannot
reach \(1\) if all available positive contributions sum to
less than \(1\). This criterion allows arbitrary fixed
numbers and magnitudes of powers and makes no knot-specific
assumption.

Absence of these projective points removes this particular
source of interior degree loss in the reduced correspondence.
It does not prove that a chosen cleared finite matrix has
an invertible leading coefficient. Its extra factors,
finite-level perturbations, endpoints and actual source
initialization still need their own estimates. Conversely,
the existence of a projective point does not prove source
growth, a nonzero coefficient, or a failure of an upper bound.

## 5. Coverage and direct sources

The all-power terminal note classifies individual terminal
curves and their double normals, but does not tensor their
branches over old infinity. The full-step interface gives
the source-preserving tensor and ordered operator transport,
while leaving the composed leading coefficient open.
The older two-run selected scalar-period resonance concerns
a different auxiliary monodromy and a selected cap pairing;
its cancellation statement is not used here.

Both complete direct sources were read at the matching pins,
with their directly used implications and hashes checked:

* [All-power terminal characteristic geometry](research_terminal_twist_characteristic_geometry.md),
  SHA256 3606f43995336bc0481acf9e04a96da5efd65f67706bef42cc9b1b1011694d1b:
  signed reduced parametrization, recurrence, polynomial leading
  terms, physical shift chart and retained double local algebra.
* [Full-step repeated-turn tensor interface](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398:
  canonical full-normal multiplication, exact ordered outer-turn
  substitution and the distinction from a regular transfer theorem.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or compilation
was run. Frozen notes and public manuscripts are unchanged.
